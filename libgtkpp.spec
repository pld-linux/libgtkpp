Summary:	Wraps Gtk+ with an object oriented look
Summary(pl):	Obudowanie Gtk+ w sposób zorientowany obiektowo
Name:		libgtkpp
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.defora.org/pub/projects/Gtkpp/%{name}-%{version}.tar.gz
Patch0:		%{name}-includes.patch
URL:		http://www.defora.org/foreign/projects/libgtkpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library which wraps Gtk+ with an object oriented look.

%description -l pl
Biblioteka C++ obudowuj±ca Gtk+ w sposób bardziej zorientowany
obiektowo.

%package devel
Summary:	Header files for gtkpp
Summary(pl):	Pliki nag³ówkowe gtkpp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for gtkpp library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gtkpp.

%package static
Summary:	Static gtkpp library
Summary(pl):	Statyczna biblioteka gtkpp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gtkpp library.

%description static -l pl
Statyczna biblioteka gtkpp.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gtkpp
%{_includedir}/gtkpp/*.h
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
