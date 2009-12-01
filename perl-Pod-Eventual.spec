%define upstream_name    Pod-Eventual
%define upstream_version 0.093330

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Just get an array of the stuff Pod::Eventual finds
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Mixin::Linewise::Readers)
BuildRequires: perl(Test::Deep)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


