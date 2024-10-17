%define major 2
%define libname %mklibname mng %{major}
%define devname %mklibname -d mng

Summary:	A library for handling MNG files
Name:		libmng
Version:	2.0.3
Release:	10
License:	Distributable (see LICENSE)
Group:		System/Libraries
Url:		https://www.libmng.com/
Source0:	http://prdownloads.sourceforge.net/libmng/%{name}-%{version}.tar.xz
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(zlib)

%description
The libmng library supports decoding, displaying, encoding, and various other
manipulations of the Multiple-image Network Graphics (MNG) format image files.
It uses the zlib compression library, and optionally the JPEG library by the
Independent JPEG Group (IJG) and/or lcms (little cms), a color-management
library by Marti Maria Saguar

%package -n	%{libname}
Summary:	A library for handling MNG files
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n	%{libname}
The libmng library supports decoding, displaying, encoding, and various other
manipulations of the Multiple-image Network Graphics (MNG) format image files.
It uses the zlib compression library, and optionally the JPEG library by the
Independent JPEG Group (IJG) and/or lcms (little cms), a color-management
library by Marti Maria Saguar

%package -n	%{devname}
Summary:	Header files for libmng
Group:		Development/C
Requires:	%{libname} = %{EVRD}
#Provides:	mng-devel = %{EVRD}
Obsoletes:	%{mklibname -s -d mng} < 1.0.10-15
Requires:	jpeg-devel
Requires:	pkgconfig(lcms2)
Requires:	pkgconfig(zlib)

%description -n	%{devname}
This package contains header files needed for development.

%prep
%autosetup -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libmng.so.%{major}*

%files -n %{devname}
%doc CHANGES LICENSE README README.contrib README.examples
%doc doc/Plan1.png doc/Plan2.png doc/doc.readme doc/libmng.txt
%{_includedir}/*
%{_libdir}/pkgconfig/libmng.pc
%{_libdir}/*.so
%{_mandir}/man*/*
