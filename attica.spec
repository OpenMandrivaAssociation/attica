%define major 5
%define libname %mklibname KF5Attica %{major}
%define devname %mklibname KF5Attica -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Open Collaboration Service providers library
Name:		attica
Version:	5.106.0
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://www.kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/attica-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(egl)
# For building QCH docs
BuildRequires:	doxygen
BuildRequires:	qt5-assistant
# Remains from renaming...
Obsoletes:	attica5-debuginfo < %{EVRD}

%description
A library to access Open Collaboration Service providers 
Required to access OSC providers in get hot new stuff. 

%package -n %{libname}
Summary:	Open Collaboration Service providers library, part of KDE Frameworks 5
Group:		System/Libraries
Obsoletes:	%{mklibname attica 0.4} < %{EVRD}

%description -n %{libname}
A library to access Open Collaboration Service providers 
Required to access OSC providers in get hot new stuff. 

It is part of KDE Frameworks 5.

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < 0.4.1-2
Obsoletes:	%{mklibname attica -d} < %{EVRD}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q -n attica-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_datadir}/qlogging-categories5/attica.renamecategories
%{_datadir}/qlogging-categories5/attica.categories
%{_libdir}/libKF5Attica.so.%{version}
%{_libdir}/libKF5Attica.so.%{major}

%files -n %{devname}
%dir %{_includedir}/KF5
%{_includedir}/KF5/Attica
%{_libdir}/libKF5Attica.so
%{_libdir}/pkgconfig/libKF5Attica.pc
%{_libdir}/cmake/KF5Attica
%{_libdir}/qt5/mkspecs/modules/*.pri

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
