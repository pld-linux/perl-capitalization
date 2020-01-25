#
# Conditional build
%bcond_with	tests	# perform "make test" (requires reader)
#
Summary:	No capitalization on method names
Summary(pl.UTF-8):	Brak wielkich liter w nazwach metod
Name:		perl-capitalization
Version:	0.03
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/capitalization-%{version}.tar.gz
# Source0-md5:	94998b37b4f86bd2e5738ab3a8fb4e7c
URL:		http://search.cpan.org/~miyagawa/capitalization-0.03/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
No capitalization on method names.

%description -l pl.UTF-8
Brak wielkich liter w nazwach metod.

%prep
%setup -q -n capitalization-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
