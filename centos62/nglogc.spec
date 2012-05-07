Summary: nglogc
Name: nglogc
Version: 1.1.0
Release: 1
License: LGPL
Source: http://nglogc.googlecode.com/files/nglogc-1.1.0.tar.gz
Url: http://code.google.com/p/nglogc/
Packager: Ferran Selles <ferran.selles@gmail.com>
Group: Loggers

BuildRoot: /tmp/%{name}-%{version}-%{release}-root

%description

%prep
%setup -q

%build
./configure --prefix=/usr --libdir=%{_libdir}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir /usr/include/nglogc
/usr/include/nglogc/*
%{_libdir}/libnglogc*

%dir /usr/share/doc/nglogc
/usr/share/doc/nglogc/*

/usr/share/man/man3/logc_*

%changelog
* Thu Apr 26 2012 Ferran Selles <ferran.selles@gmail.com> 1.1-1
- Initial RPM release
