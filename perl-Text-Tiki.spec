%define module	Text-Tiki
%define name	perl-%{module}
%define version	0.73
%define release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	TikiText - Text Formatting Engine
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Buildrequires:	perl-devel
Buildarch:	noarch

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
%setup -q -n %{module}-%{version}

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

