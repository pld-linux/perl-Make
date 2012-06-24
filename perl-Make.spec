%include	/usr/lib/rpm/macros.perl
Summary:	Make perl module
Summary(pl):	Modu� perla Make
Name:		perl-Make
Version:	1.00
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Make/Make-%{version}.tar.gz
Patch0:		%{name}-pmake.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make - module for processing makefiles.

%description -l pl
Make - modu� do przetwarzania plik�w Makefile.

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
