%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	FillIn
Summary:	Text::FillIn perl module
Summary(pl):	Modu³ perla Text::FillIn
Name:		perl-Text-FillIn
Version:	0.05
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23d1cfcc132ac15d19c560be53c4f831
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::FillIn module provides a class for doing fill-in templates.

%description -l pl
Modu³ Text::FillIn udospêpnia klasê do tworzenia szablonów z polami "do
wype³nienia".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/FillIn.pm
%{_mandir}/man3/*
