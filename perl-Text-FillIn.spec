%include	/usr/lib/rpm/macros.perl
Summary:	Text-FillIn perl module
Summary(pl):	Modu� perla Text-FillIn
Name:		perl-Text-FillIn
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-FillIn-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-FillIn module provides a class for doing fill-in templates.

%description -l pl
Modu� Text-FillIn udosp�pnia klas� do tworzenia szablon�w z polami "do
wype�nienia".

%prep
%setup -q -n Text-FillIn-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/FillIn
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Text/FillIn.pm
%{perl_sitearch}/auto/Text/FillIn

%{_mandir}/man3/*
