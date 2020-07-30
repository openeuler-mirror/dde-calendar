%global repo dde-calendar

Name:           deepin-calendar
Version:        5.6.1
Release:        4
Summary:        Calendar for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{repo}_%{version}.orig.tar.xz	
Patch0:		calendar_time.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(dtkwidget) >= 5.1.1
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkcore) >= 5.1.1
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qtmultimedia-devel qt5-qtx11extras-devel
Requires:       dde-api

%description
Calendar for Deepin Desktop Environment.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
%patch0 -p1

%build
%{qmake_qt5} PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{repo}
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/com.deepin.Calendar.service
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{repo}.svg

%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-4
- fix spec

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-3
- Package init
