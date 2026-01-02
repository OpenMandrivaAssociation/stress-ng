%define _empty_manifest_terminate_build 0

Name:		stress-ng
Version:	0.20.00
Release:	1
Summary:	Stress test a computer system in various ways
Group:    System/Kernel and hardware 
License:	GPLv2+
URL:		https://kernel.ubuntu.com/~cking/%{name}
Source0:  https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V%{version}/%{name}-%{version}.tar.gz
#Source0:	http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.xz
#Patch0:		stress-ng-0.10.17-clang.patch

BuildRequires:	make
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
%autosetup -p1

%build
#export CC=gcc
#export CXX=g++
#export CFLAGS="%{optflags}"
#export LDFLAGS="%{__global_ldflags}"
# Allow for [[clang::fallthrough]]
#sed -i -e 's,gnu99,gnu2x,g' Makefile
%make_build


%install
install -p -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license COPYING
%doc README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

