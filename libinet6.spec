%define snap	20010420
Summary:	Library for platforms without IPv6 support in base libc
Summary(pl):	Bibliteka dla platform bez obs³ugi IPv6 w podstawowej bibliotece
Name:		libinet6
Version:	0.%{snap}
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	cvs://:pserver:anoncvs@anoncvs.linux-ipv6.org:/cvsroot/usagi/libc/%{name}-%{snap}.tar.gz
URL:		http://www.linux-ipv6.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_includedir	%{_prefix}/include/libinet6

%description
Package contains IPv6 functions such as getaddrinfo(), getnameinfo(),
getifaddrs(), r-commands etc. Most of these functions are in base
glibc library, so you need this only in special cases.

%description -l pl
Pakiet dostarcza funkcje IPv6 takie jak getaddrinfo(), getnameinfo(),
getifaddrs(), r-komendy itp. Wiêkszo¶c tych funkcji znajduje siê ju¿ w
bazowej bibliotece glibc, wiêc potrzebujesz tego pakietu tylko w
specjalnych przypadkach.

%prep
%setup  -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	install \
	install-includes \
	oldincludedir=$RPM_BUILD_ROOT%{_includedir}
	
gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}
%{_libdir}/*.a
