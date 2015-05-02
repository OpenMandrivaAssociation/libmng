%define major 2
%define libname %mklibname mng %{major}
%define devname %mklibname mng -d

Summary:	A library for handling MNG files
Name:		libmng
Version:	2.0.2
Release:	3
License:	Distributable (see LICENSE)
Group:		System/Libraries
Url:		http://www.libmng.com/
Source0:	http://prdownloads.sourceforge.net/libmng/%{name}-%{version}.tar.xz
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(zlib)

%description
The libmng library supports decoding, displaying, encoding, and various other
manipulations of the Multiple-image Network Graphics (MNG) format image files.
It uses the zlib compression library, and optionally the JPEG library by the
Independent JPEG Group (IJG) and/or lcms (little cms), a color-management
library by Marti Maria Saguar.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A library for handling MNG files
Group:		System/Libraries

%description -n %{libname}
The libmng library supports decoding, displaying, encoding, and various other
manipulations of the Multiple-image Network Graphics (MNG) format image files.
It uses the zlib compression library, and optionally the JPEG library by the
Independent JPEG Group (IJG) and/or lcms (little cms), a color-management
library by Marti Maria Saguar.

%files -n %{libname}
%{_libdir}/libmng.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for libmng
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	mng-devel = %{EVRD}

%description -n %{devname}
This package contains header files needed for development.

%files -n %{devname}
%doc CHANGES LICENSE README README.contrib README.examples
%doc doc/Plan1.png doc/Plan2.png doc/doc.readme doc/libmng.txt
%{_includedir}/*
%{_libdir}/pkgconfig/libmng.pc
%{_libdir}/*.so
%{_mandir}/man*/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std