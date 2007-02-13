Summary:	Wraps GTK+ with an object oriented look
Summary(pl.UTF-8):	Obudowanie GTK+ w sposób zorientowany obiektowo
Name:		libgtkpp
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.defora.org/pub/projects/Gtkpp/%{name}-%{version}.tar.gz
# Source0-md5:	53b13501401693e268fb834188b5bd0f
Patch0:		%{name}-includes.patch
URL:		http://www.defora.org/foreign/projects/libgtkpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ library which wraps GTK+ with an object oriented look.

%description -l pl.UTF-8
Biblioteka C++ obudowująca GTK+ w sposób bardziej zorientowany
obiektowo.

%package devel
Summary:	Header files for gtkpp
Summary(pl.UTF-8):	Pliki nagłówkowe gtkpp
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf-devel
Requires:	gnome-libs-devel
Requires:	libstdc++-devel

%description devel
Header files for gtkpp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtkpp.

%package static
Summary:	Static gtkpp library
Summary(pl.UTF-8):	Statyczna biblioteka gtkpp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtkpp library.

%description static -l pl.UTF-8
Statyczna biblioteka gtkpp.

%prep
%setup -q
%patch0 -p1

%build
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
