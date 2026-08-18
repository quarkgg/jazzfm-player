# jazzfm-player

A basic Python app.

## Setup

`sudo dnf install python3-pyside6`  # system Qt 6 (KDE-native), no pip needed

## Build & install (RPM)

```bash
./build-rpm.sh            # rpmbuild needs python3-rpm-macros (dnf install python3-rpm-macros)
sudo rpm -Uvh ~/rpmbuild/RPMS/noarch/jazzfm-player-*.rpm
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
