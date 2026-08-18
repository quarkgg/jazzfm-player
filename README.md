# jazzfm-player

A basic KDE Plasma player for Jazzfm.bg radio. Streams directly the URL https://cdn.btv.bg/radio/jazz-fm.mp3. 

## Setup
Requires KDE Plasma (tested on Fedora 44). All dependencies are declared in the rpm. Use DNF to install.

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
