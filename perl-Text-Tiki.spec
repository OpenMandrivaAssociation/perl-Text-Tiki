%define upstream_name	 Text-Tiki
%define upstream_version 0.73

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	TikiText - Text Formatting Engine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
TikiText is a text formatting notation and engine, with the following
design goals:
* Leverage existing text formatting notions.
* Least amount of characters from plain text.
* Use more intuitive and common plain text email conventions.
* Abstract users from needing to know or understand markup whenever
  possible.
* Make valid and semantical XHTML markup easy.
  (And let CSS do its job!)
* Easy to learn the basics. Richer functionality for those who want to
  dive in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/*/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.730.0-2mdv2011.0
+ Revision: 658890
- rebuild for updated spec-helper

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.730.0-1mdv2010.0
+ Revision: 409304
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.73-5mdv2009.0
+ Revision: 242059
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.73-3mdv2008.0
+ Revision: 23639
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.73-2mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Tue Mar 28 2006 Olivier Blin <oblin@mandriva.com> 0.73-1mdk
- initial release

