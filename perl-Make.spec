%include	/usr/lib/rpm/macros.perl
Summary:	Make perl module
Summary(pl):	Modu³ perla Make
Name:		perl-Make
Version:	1.00
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Make/Make-%{version}.tar.gz
Patch0:		%{name}-pmake.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make - module for processing makefiles.

%description -l pl
Make - modu³ do przetwarzania plików Makefile.

%prep
%setup -q -n Make-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
perl -I. pmake.pl

%install
rm -rf $RPM_BUILD_ROOT

perl -Mblib pmake.pl install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/pmake.pl
%{perl_vendorlib}/Make.pm
%{_mandir}/man[13]/*
