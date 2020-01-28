Name:		stress-ng
Version:	0.10.17
Release:	1
Summary:	Stress test a computer system in various ways

License:	GPLv2+
URL:		http://kernel.ubuntu.com/~cking/%{name}
Source0:	http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	glibc-devel
BuildRequires:	kernel-headers
BuildRequires:	pkgconfig(libkeyutils)
BuildRequires:	libaio-devel
BuildRequires:	pkgconfig(libattr)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	lksctp-tools
BuildRequires:  pkgconfig(libsctp)
BuildRequires:	pkgconfig(zlib)

%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
install -p -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

