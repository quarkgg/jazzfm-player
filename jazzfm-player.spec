Name:           jazzfm-player
Version:        0.1.0
Release:        1%{?dist}
Summary:        Minimal Jazz FM stream player for KDE (PySide6)
License:        Copyright (c) 2026 chadela
BuildArch:      noarch

Source0:          %{name}-%{version}.tar

Requires:       python3-pyside6

%description
Minimal Jazz FM radio player: play/pause/stop the live stream, minimize to
the system tray. Pure Python; all GUI/media dependencies are system packages.

%prep
%setup -q

%build
# Pure Python; nothing to build.

%install
rm -rf %{buildroot}
install -d %{buildroot}%{python3_sitelib}/jazzfm_player \
          %{buildroot}%{_datadir}/icons/hicolor/128x128/apps \
          %{buildroot}%{_datadir}/jazzfm-player \
          %{buildroot}%{_bindir} \
          %{buildroot}%{_datadir}/applications
install -m 644 jazzfm_player/__init__.py jazzfm_player/__main__.py \
    %{buildroot}%{python3_sitelib}/jazzfm_player/
install -m 644 logo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/jazzfm-player.png
install -m 644 logo.png %{buildroot}%{_datadir}/jazzfm-player/logo.png
install -m 755 jazzfm-player %{buildroot}%{_bindir}/jazzfm-player
install -m 644 jazzfm-player.desktop %{buildroot}%{_datadir}/applications/jazzfm-player.desktop

%files
%{python3_sitelib}/jazzfm_player
%{_datadir}/icons/hicolor/128x128/apps/jazzfm-player.png
%{_datadir}/jazzfm-player
%{_bindir}/jazzfm-player
%{_datadir}/applications/jazzfm-player.desktop

%changelog
* Tue Aug 18 2026 chadela - 0.1.0-1
- Initial RPM packaging
