%global	rubyver		1.9.3
%global	_patchlevel	194

%global	dotpatchlevel	%{?_patchlevel:.%{_patchlevel}}

Summary: An interpreter of object-oriented scripting language
Name: ruby
Version: %{rubyver}%{?dotpatchlevel}
Release: 1
License: Ruby or GPLv2
Source; http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-1.9.3-p194.tar.bz2
Url: http://www.ruby-lang.org/en/
Packager: Ferran Selles <ferran.selles@gmail.com>
Group: Development/Languages

BuildRoot: /tmp/%{name}-%{version}-%{release}-root

%description

%prep
%setup -q

%build

%install

%clean
rm -rf %{buildroot}

%files

%changelog
* Fri Apr 27 2012 Ferran Selles <ferran.selles@gmail.com> 1.9.3.-p194
- Initial RPM release
