%include	/usr/lib/rpm/macros.perl
Summary:	Make perl module
Summary(pl):	Modu³ perla Make
Name:		perl-Make
Version:	1.00
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Make/Make-%{version}.tar.gz
Patch0:		%{name}-pmake.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make - module for processing makefiles.

%description -l pl
Make - modu³ do przetwarzania plików Makefile.

%prep
%setup -q -n Make-%{version}
%patch -p1

%build
perl Makefile.PL
perl -I. pmake.pl

%install
rm -rf $RPM_BUILD_ROOT

perl -Mblib pmake.pl install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pmake.pl
%{perl_sitelib}/Make.pm
%{_mandir}/man[13]/*
