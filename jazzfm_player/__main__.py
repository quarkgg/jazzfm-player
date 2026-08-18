"""Jazz FM player: play/pause/stop a live stream, minimize to tray."""

import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMenu,
    QPushButton,
    QSystemTrayIcon,
    QWidget,
)

STREAM_URL = "https://cdn.btv.bg/radio/jazz-fm.mp3"
ICON_NAME = "jazzfm-player"
# File fallbacks when the icon theme has no entry: the copy installed by
# the RPM, then the source tree when running from a checkout.
LOGO_FALLBACKS = (
    Path("/usr/share/jazzfm-player/logo.png"),
    Path(__file__).resolve().parents[1] / "logo.png",
)


def app_icon():
    """App icon: desktop theme first, then the logo file, then empty."""
    icon = QIcon.fromTheme(ICON_NAME)
    if not icon.isNull():
        return icon
    for path in LOGO_FALLBACKS:
        if path.exists():
            return QIcon(str(path))
    return QIcon()


class PlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jazz FM")
        self.setWindowIcon(app_icon())
        self.setFixedSize(210, 60)

        self.audio = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl(STREAM_URL))

        bar = QWidget()
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(8, 8, 8, 8)
        self.play_btn = QPushButton("Play")
        self.pause_btn = QPushButton("Pause")
        self.stop_btn = QPushButton("Stop")
        for btn in (self.play_btn, self.pause_btn, self.stop_btn):
            layout.addWidget(btn)
        self.setCentralWidget(bar)

        self.play_btn.clicked.connect(self.player.play)
        self.pause_btn.clicked.connect(self.player.pause)
        self.stop_btn.clicked.connect(self.player.stop)

        self.tray = QSystemTrayIcon(app_icon())
        self.tray.setToolTip("Jazz FM")
        self.tray.activated.connect(self.on_tray_activated)
        self.menu = QMenu()
        self.menu.addAction("Show", self.show_from_tray)
        self.menu.addAction("Play", self.player.play)
        self.menu.addAction("Pause", self.player.pause)
        self.menu.addAction("Stop", self.player.stop)
        self.menu.addSeparator()
        self.menu.addAction("Quit", self.quit_app)
        self.tray.setContextMenu(self.menu)
        self.tray.show()

    def on_tray_activated(self, reason, origin=None):
        # The StatusNotifierItem protocol (Plasma) has no double-click: each
        # left click arrives as Trigger. The SNI path delivers the activated
        # signal with a single argument, so `origin` is optional.
        # Restore the window on a single click, which also covers X11/XEmbed,
        # where Trigger is a plain left click.
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_from_tray()

    def show_from_tray(self):
        self.show()
        self.raise_()
        self.activateWindow()

    def quit_app(self):
        self.player.stop()
        QApplication.quit()

    def closeEvent(self, event):
        # Close button = minimize to tray; playback continues in background.
        event.accept()
        self.hide()


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = PlayerWindow()
    window.show()
    window.player.play()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
