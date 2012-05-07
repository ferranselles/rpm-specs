%define baseversion 7.3
%define patchlevel 515
%define revision 273fbf501965
%define vimdir vim73

Summary: The VIM editor
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 2
License: Vim
Source: http://packages.nulltrace.com/src/vim/vim-7.3.515.tar.bz2
Url: http://www.vim.org/
Packager: Ferran Selles <ferran.selles@gmail.com>
Group: Applications/Editors

BuildRoot: /tmp/%{name}-%{version}-%{release}-root

Buildrequires: ncurses-devel python-devel gettext

Provides: vim-minimal = %{version}-%{release}
Obsoletes: vim-minimal < %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.

Inspired by Fedora 16 vim spec file

%prep
%setup -q -n vim
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk

%build
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

#RedHat splits tinfo and ncurses, vim only needs tinfo
./configure --prefix=/usr \
            --libdir=%{_libdir} \
            --enable-gui=no \
            --without-x \
            --disable-nls \
            --enable-multibyte \
            --with-tlib=tinfo \
            --enable-pythoninterp \
            --enable-cscope \
            --with-features=huge
make

%install
rm -rf %{buildroot}
cp runtime/doc/uganda.txt LICENSE
rm -f README*.info
make DESTDIR=%{buildroot} install

rm -rf runtime/doc

( cd $RPM_BUILD_ROOT/%{_bindir}
  ln -sf vim vi
)

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/vim132

rm -f $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/macros/maze/maze*.c
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README* LICENSE

%dir %{_datadir}/%{name}/%{vimdir}
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%{_datadir}/%{name}/%{vimdir}/*.vim

%{_mandir}/man1/evim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/view.*
%{_mandir}/man1/vim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
%{_mandir}/man1/xxd.*

%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/rvim
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/vim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%{_bindir}/xxd

%changelog
* Sun May 06 2012 Ferran Selles <ferran.selles@gmail.com> 7.3.515-2
- Cleanup some code to remove non reuired dependencies
* Sat May 05 2012 Ferran Selles <ferran.selles@gmail.com> 7.3.515-1
- patchlevel 515
- Initial RPM release
