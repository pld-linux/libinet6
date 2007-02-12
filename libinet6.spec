%define snap	20030228
Summary:	Library for platforms without IPv6 support in base libc
Summary(pl.UTF-8):   Biblioteka dla platform bez obsługi IPv6 w podstawowej bibliotece
Name:		libinet6
Version:	0.%{snap}
Release:	5
License:	LGPL
Group:		Libraries
# from		cvs -d :pserver:anoncvs:anoncvs@anoncvs.linux-ipv6.org:/cvsroot/usagi usagi/usagi/libinet6
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	b35a24121bb55b0e1f2425865885cda0
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-kill_warnings.patch
Patch3:		%{name}-pid.patch
URL:		http://www.linux-ipv6.org/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/libinet6

%description
Package contains IPv6 functions such as getaddrinfo(), getnameinfo(),
getifaddrs(), r-commands etc. Most of these functions are in base
glibc library, so you need this only in special cases.

%description -l pl.UTF-8
Pakiet dostarcza funkcje IPv6 takie jak getaddrinfo(), getnameinfo(),
getifaddrs(), r-komendy itp. Większość tych funkcji znajduje się już w
bazowej bibliotece glibc, więc potrzebujesz tego pakietu tylko w
specjalnych przypadkach.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -f include_glibc2[23]/bits/socket.h
ln -sf /usr/include/bits/socket.h include_glibc22/bits
ln -sf /usr/include/bits/socket.h include_glibc23/bits

%build
%{__autoconf}
%configure
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	install \
	install-includes \
	oldincludedir=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_includedir}
%{_libdir}/*.a
%{_mandir}/man3/*.3*
