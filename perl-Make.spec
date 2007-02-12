#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Make - module for processing makefiles
Summary(pl.UTF-8):   Make - moduł do przetwarzania plików Makefile
Name:		perl-Make
Version:	1.00
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Make/Make-%{version}.tar.gz
# Source0-md5:	ee5233f89630451dd2c24e5e0d7d3336
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make - module for processing makefiles.

%description -l pl.UTF-8
Make - moduł do przetwarzania plików Makefile.

%prep
%setup -q -n Make-%{version}
mv pmake pmake.pl
%{__perl} -pi -e '/EXE_FILES/ && s/pmake/pmake.pl/' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/M*
