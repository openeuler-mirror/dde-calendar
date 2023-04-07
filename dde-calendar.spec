%define pkgrelease  1
%if 0%{?openeuler}
%define specrelease %{pkgrelease}
%else
## allow specrelease to have configurable %%{?dist} tag in other distribution
%define specrelease %{pkgrelease}%{?dist}
%endif

Name:           dde-calendar
Version:        5.8.20.1

Release:        %{specrelease}
Summary:        Calendar is a smart daily planner to schedule all things in life
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-calendarr
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-fix-build-error.patch

BuildRequires: cmake
BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: dtkgui-devel
BuildRequires: dtkwidget-devel
#BuildRequires: deepin-gettext-tools
BuildRequires: pkgconfig(dframeworkdbus)
BuildRequires: gtest-devel
BuildRequires: gmock

%description
%{summary}.

%prep
%autosetup -p1

%build
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
mkdir build && pushd build 
%cmake -DCMAKE_BUILD_TYPE=Release ../  -DAPP_VERSION=%{version} -DVERSION=%{version} -DCMAKE_SCHEDULE_PLUGIN_OFF="OFF" 
%make_build  
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/deepin-manual/manual-assets/application/dde-calendar/calendar/*
%{_datadir}/dbus-1/services/*.service
/etc/xdg/autostart/dde-calendar-service.desktop
%{_datadir}/dde-calendar/data/*
/usr/lib/deepin-daemon/dde-calendar-service

%changelog
* Mon Mar 27 2023 liweiganga <liweiganga@uniontech.com> - 5.8.20.1-1
- update: update to 5.8.20.1

* Mon Jul 18 2022 konglidong <konglidong@uniontech.com> - 5.8.10-1
- update to 5.8.10

* Tue Feb 08 2022 liweigang <liweiganga@uniontech.com> - 5.7.0.5-2
- fix build error

* Wed Jul 07 2021 weidong <weidong@uniontech.com> - 5.7.0.5-1
- Update to 5.7.0.5

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-4
- fix spec

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-3
- Package init
