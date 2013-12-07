%define major	1
%define libname	%mklibname mng %{major}
%define devname	%mklibname -d mng

Summary:	A library for handling MNG files
Name:		libmng
Version:	1.0.10
Release:	17
License:	Distributable (see LICENSE)
Group:		System/Libraries
Url:		http://www.libmng.com/
Source0:	http://prdownloads.sourceforge.net/libmng/%{name}-%{version}.tar.gz
Patch0:		libmng-1.0.10-automake1.12.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(lcms)
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
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
The libmng library supports decoding, displaying, encoding, and various other
manipulations of the Multiple-image Network Graphics (MNG) format image files.
It uses the zlib compression library, and optionally the JPEG library by the
Independent JPEG Group (IJG) and/or lcms (little cms), a color-management
library by Marti Maria Saguar

%package -n	%{devname}
Summary:	Header files for libmng
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	mng-devel = %{version}-%{release}
Obsoletes:	%{mklibname -s -d mng} < 1.0.10-15

%description -n	%{devname}
This package contains header files needed for development.

%prep
%setup -q
%apply_patches
cp -a makefiles/{configure.in,Makefile.am} ./
#aclocal; libtoolize --force; automake -a; autoconf
autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

install -m644 doc/man/libmng.3 -D %{buildroot}%{_mandir}/man3/libmng.3
install -m644 doc/man/jng.5 -D %{buildroot}%{_mandir}/man5/jng.5
install -m644 doc/man/mng.5 -D %{buildroot}%{_mandir}/man5/mng.5

%files -n %{libname}
%{_libdir}/libmng.so.%{major}*

%files -n %{devname}
%doc CHANGES LICENSE README README.contrib README.examples
%doc doc/Plan1.png doc/Plan2.png doc/doc.readme doc/libmng.txt
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man*/*

