%define major 1
%define libname %mklibname mng %{major}
%define develname %mklibname -d mng

Summary:	A library for handling MNG files
Name:		libmng
Version:	1.0.10
Release:	15
License:	Distributable (see LICENSE)
Group:		System/Libraries
URL:		http://www.libmng.com/
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

%package -n	%{develname}
Summary:	Header files for libmng
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	mng-devel = %{version}-%{release}
Obsoletes:	libmng0.9.3-devel < 1.0.10-15
Obsoletes:	libmng0-devel < 1.0.10-15
Obsoletes:	%{libname}-devel < 1.0.10-15
Obsoletes:	%{_lib}mng1-devel < 1.0.10-15
Obsoletes:	%{mklibname -s -d mng} < 1.0.10-15

%description -n	%{develname}
The libmng library supports decoding, displaying, encoding, and various other
manipulations of the Multiple-image Network Graphics (MNG) format image files.
It uses the zlib compression library, and optionally the JPEG library by the
Independent JPEG Group (IJG) and/or lcms (little cms), a color-management
library by Marti Maria Saguar

This package contains header files needed for development.

%prep
%setup -q
%patch0 -p1

%build
cp -a makefiles/{configure.in,Makefile.am} ./
aclocal; libtoolize --force; automake -a; autoconf

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

%files -n %{develname}
%doc CHANGES LICENSE README README.contrib README.examples
%doc doc/Plan1.png doc/Plan2.png doc/doc.readme doc/libmng.txt
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man*/*


%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.10-14
+ Revision: 744701
- rebuild
- cleaned up spec
- disabled and obsoleted static build/pkg

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-13
+ Revision: 660266
- mass rebuild

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-12mdv2011.0
+ Revision: 601054
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-11mdv2010.1
+ Revision: 488779
- rebuilt against libjpeg v8

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-10mdv2010.0
+ Revision: 416522
- rebuilt against libjpeg v7

* Mon Mar 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.10-9mdv2009.1
+ Revision: 362738
- Rebuild for lcms 1.18 security updates

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-8mdv2009.1
+ Revision: 315577
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.10-7mdv2009.0
+ Revision: 222931
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-6mdv2008.1
+ Revision: 179990
- bump release
- fix build deps
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jul 14 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.10-3mdv2008.0
+ Revision: 51953
- don't obsolete yourself; obsolete libmng1-devel

* Sat Jul 14 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.10-2mdv2008.0
+ Revision: 51919
- rebuild for missing -devel package

* Fri Jul 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-1mdv2008.0
+ Revision: 51876
- conform to the latest specs


* Tue Jan 30 2007 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdv2007.0
+ Revision: 115450
- Import libmng

* Tue Jan 30 2007 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdv2007.1
- rebuild

* Mon Oct 17 2005 Olivier Thauvin <nanardon@mandriva.org> 1.0.9-1mdk
- 1.0.9
- spec cleanup

* Thu Nov 11 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.8-1mdk
- 1.0.8

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.7-1mdk
- 1.0.7
- drop P0 & P3
- regenerate P1 (is it really needed anymore?)
- fix obsolete-not-provided
- cosmetics

* Mon Mar 01 2004 Stefan van der Eijk <stefan@eijk.nu> 1.0.5-5mdk
- reupload

