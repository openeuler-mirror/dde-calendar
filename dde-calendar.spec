Name:           dde-calendar
Version:        5.7.0.5
Release:        1
Summary:        Calendar for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Provides:      deepin-calendar
Obsoletes:     deepin-calendar

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-devel

BuildRequires: dtkcore-devel
BuildRequires: dtkwidget-devel
BuildRequires: pkgconfig(dtkgui)
BuildRequires: pkgconfig(dframeworkdbus)

%description
%{summary}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
# cmake_minimum_required version is too high
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
mkdir build && pushd build
%cmake ../ -DCMAKE_BUILD_TYPE=Release -DAPP_VERSION=%{version} -DVERSION=%{version}

%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/dbus-1/services/com.deepin.Calendar.service
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 07 2021 weidong <weidong@uniontech.com> - 5.7.0.5-1
- Update to 5.7.0.5

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-4
- fix spec

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-3
- Package init
