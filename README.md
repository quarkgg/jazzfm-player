# jazzfm-player

A basic Python app.

## Setup

No manual dependencies to install — the RPM declares them and dnf
resolves them automatically (system Qt 6 via `python3-pyside6`,
GStreamer plugins for streaming; KDE-native, no pip needed).

## Build & install (RPM)

```bash
sudo dnf builddep jazzfm-player.spec   # installs build-time deps (python3-rpm-macros)
./build-rpm.sh
sudo dnf install ~/rpmbuild/RPMS/noarch/jazzfm-player-*.rpm
```

## Run

`jazzfm-player`  # from the terminal, or the "Jazz FM Player" app-menu entry

## Uninstall

`sudo rpm -e jazzfm-player`

## Layout

- `jazzfm_player/` — app package
- `jazzfm-player` — launcher script (installed to /usr/bin)
- `jazzfm-player.desktop` — app-menu entry
- `jazzfm-player.spec`, `build-rpm.sh` — RPM packaging
- `logo.png` — app icon (installed to the hicolor theme + /usr/share/jazzfm-player)
- `pyproject.toml` — project metadata
