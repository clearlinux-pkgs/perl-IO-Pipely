#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Pipely
Version  : 0.005
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/IO-Pipely-0.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/IO-Pipely-0.005.tar.gz
Summary  : 'Portably create pipe() or pipe-like handles, one way or another.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Pipely-license = %{version}-%{release}
Requires: perl-IO-Pipely-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
IO::Pipely - Portably create pipe() or pipe-like handles, one way or
another.

%package dev
Summary: dev components for the perl-IO-Pipely package.
Group: Development
Provides: perl-IO-Pipely-devel = %{version}-%{release}
Requires: perl-IO-Pipely = %{version}-%{release}

%description dev
dev components for the perl-IO-Pipely package.


%package license
Summary: license components for the perl-IO-Pipely package.
Group: Default

%description license
license components for the perl-IO-Pipely package.


%package perl
Summary: perl components for the perl-IO-Pipely package.
Group: Default
Requires: perl-IO-Pipely = %{version}-%{release}

%description perl
perl components for the perl-IO-Pipely package.


%prep
%setup -q -n IO-Pipely-0.005
cd %{_builddir}/IO-Pipely-0.005

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Pipely
cp %{_builddir}/IO-Pipely-0.005/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Pipely/8d782ec236445bcb6b07064a9819b0ffb4aca3b3
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Pipely.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Pipely/8d782ec236445bcb6b07064a9819b0ffb4aca3b3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/IO/Pipely.pm
