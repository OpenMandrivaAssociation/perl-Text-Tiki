%define upstream_name	 Text-Tiki
%define upstream_version 0.73

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	TikiText - Text Formatting Engine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/*/*
