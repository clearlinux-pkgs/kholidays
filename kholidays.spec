#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kholidays
Version  : 5.71.0
Release  : 32
URL      : https://download.kde.org/stable/frameworks/5.71/kholidays-5.71.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.71/kholidays-5.71.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.71/kholidays-5.71.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kholidays-data = %{version}-%{release}
Requires: kholidays-lib = %{version}-%{release}
Requires: kholidays-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
To generate the Bison/Flex parser/scanner code after any changes to
holidayparserplan.ypp or holidayscannerplan.lpp run:

%package data
Summary: data components for the kholidays package.
Group: Data

%description data
data components for the kholidays package.


%package dev
Summary: dev components for the kholidays package.
Group: Development
Requires: kholidays-lib = %{version}-%{release}
Requires: kholidays-data = %{version}-%{release}
Provides: kholidays-devel = %{version}-%{release}
Requires: kholidays = %{version}-%{release}

%description dev
dev components for the kholidays package.


%package lib
Summary: lib components for the kholidays package.
Group: Libraries
Requires: kholidays-data = %{version}-%{release}
Requires: kholidays-license = %{version}-%{release}

%description lib
lib components for the kholidays package.


%package license
Summary: license components for the kholidays package.
Group: Default

%description license
license components for the kholidays package.


%prep
%setup -q -n kholidays-5.71.0
cd %{_builddir}/kholidays-5.71.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592244805
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1592244805
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kholidays
cp %{_builddir}/kholidays-5.71.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kholidays/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/az/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/be/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/br/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/da/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/el/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/et/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/he/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/id/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/is/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/km/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/se/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/th/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkholidays5_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KHolidays/KHolidays/AstroSeasons
/usr/include/KF5/KHolidays/KHolidays/Holiday
/usr/include/KF5/KHolidays/KHolidays/HolidayRegion
/usr/include/KF5/KHolidays/KHolidays/LunarPhase
/usr/include/KF5/KHolidays/KHolidays/SunRiseSet
/usr/include/KF5/KHolidays/KHolidays/Zodiac
/usr/include/KF5/KHolidays/kholidays/astroseasons.h
/usr/include/KF5/KHolidays/kholidays/holiday.h
/usr/include/KF5/KHolidays/kholidays/holidayregion.h
/usr/include/KF5/KHolidays/kholidays/kholidays_export.h
/usr/include/KF5/KHolidays/kholidays/lunarphase.h
/usr/include/KF5/KHolidays/kholidays/sunriseset.h
/usr/include/KF5/KHolidays/kholidays/zodiac.h
/usr/include/KF5/kholidays_version.h
/usr/lib64/cmake/KF5Holidays/KF5HolidaysConfig.cmake
/usr/lib64/cmake/KF5Holidays/KF5HolidaysConfigVersion.cmake
/usr/lib64/cmake/KF5Holidays/KF5HolidaysTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Holidays/KF5HolidaysTargets.cmake
/usr/lib64/libKF5Holidays.so
/usr/lib64/qt5/mkspecs/modules/qt_KHolidays.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Holidays.so.5
/usr/lib64/libKF5Holidays.so.5.71.0
/usr/lib64/qt5/qml/org/kde/kholidays/libkholidaysdeclarativeplugin.so
/usr/lib64/qt5/qml/org/kde/kholidays/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kholidays/9a1929f4700d2407c70b507b3b2aaf6226a9543c
