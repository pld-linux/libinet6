%define snap	20010420
Summary:	Library for platforms without IPv6 support in base libc
Summary(pl):	Biblioteka dla platform bez obs³ugi IPv6 w podstawowej bibliotece
Name:		libinet6
Version:	0.%{snap}
Release:	3
License:	LGPL
Group:		Libraries
Source0:	cvs://:pserver:anoncvs@anoncvs.linux-ipv6.org:/cvsroot/usagi/libc/%{name}-%{snap}.tar.gz
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-nosegv.patch
URL:		http://www.linux-ipv6.org/
BuildRequires:	autoconf
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure
%{__make} OPT="%{rpmcflags}"

rm -f include_glibc22/bits/socket.h
ln -sf /usr/include/bits/socket.h include_glibc22/bits

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
