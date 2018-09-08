#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kholidays
Version  : 5.50.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.50/kholidays-5.50.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.50/kholidays-5.50.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.50/kholidays-5.50.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kholidays-lib
Requires: kholidays-license
Requires: kholidays-data
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

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
Requires: kholidays-lib
Requires: kholidays-data
Provides: kholidays-devel

%description dev
dev components for the kholidays package.


%package lib
Summary: lib components for the kholidays package.
Group: Libraries
Requires: kholidays-data
Requires: kholidays-license

%description lib
lib components for the kholidays package.


%package license
Summary: license components for the kholidays package.
Group: Default

%description license
license components for the kholidays package.


%prep
%setup -q -n kholidays-5.50.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536422095
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536422095
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kholidays
cp COPYING.LIB %{buildroot}/usr/share/doc/kholidays/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/libkholidays5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/libkholidays5_qt.qm
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
/usr/lib64/libKF5Holidays.so.5.50.0
/usr/lib64/qt5/qml/org/kde/kholidays/libkholidaysdeclarativeplugin.so
/usr/lib64/qt5/qml/org/kde/kholidays/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/kholidays/COPYING.LIB
