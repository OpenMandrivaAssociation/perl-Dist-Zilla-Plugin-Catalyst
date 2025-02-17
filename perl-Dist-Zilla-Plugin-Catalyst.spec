%define upstream_name    Dist-Zilla-Plugin-Catalyst
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A subclass of Catalyst::Helper
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Catalyst::Helper)
BuildRequires:	perl(Dist::Zilla::File::FromCode)
BuildRequires:	perl(Dist::Zilla::File::InMemory)
BuildRequires:	perl(Dist::Zilla::Role::ModuleMaker)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::ShareDir::Install)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The following is a list of plugins in this distribution to help you
integrate the Catalyst manpage and the Dist::Zilla manpage

* * the Dist::Zilla::Plugin::Catalyst::New manpage Create a new Catalyst
  Project

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


