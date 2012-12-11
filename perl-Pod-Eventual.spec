%define upstream_name    Pod-Eventual
%define upstream_version 0.093330

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Just get an array of the stuff Pod::Eventual finds
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Mixin::Linewise::Readers)
BuildRequires:	perl(Test::Deep)
BuildArch:	noarch

%description
POD is a pretty simple format to write, but it can be a big pain to deal
with reading it and doing anything useful with it. Most existing POD
parsers care about semantics, like whether a '=item' occurred after an
'=over' but before a 'back', figuring out how to link a 'L<>', and other
things like that.

Pod::Eventual is much less ambitious and much more stupid. Fortunately,
stupid is often better. (That's what I keep telling myself, anyway.)

Pod::Eventual reads line-based input and produces events describing each
POD paragraph or directive it finds. Once complete events are immediately
passed to the 'handle_event' method. This method should be implemented by
Pod::Eventual subclasses. If it isn't, Pod::Eventual's own 'handle_event'
will be called, and will raise an exception.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.93.330-2mdv2011.0
+ Revision: 655182
- rebuild for updated spec-helper

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.330-1mdv2011.0
+ Revision: 472247
- update to 0.093330

* Sat Nov 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93.170-1mdv2010.1
+ Revision: 465994
- update to 0.093170

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91.480-1mdv2010.0
+ Revision: 380975
- adding missing buildrequires:
- import perl-Pod-Eventual


* Fri May 29 2009 cpan2dist 0.091480-1mdv
- initial mdv release, generated with cpan2dist

