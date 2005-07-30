# TODO
# - separate client and server package?
#
# Conditional build:
%bcond_with	uClibc	# link with uClibc
%bcond_with	combined_binary # combined_binary
#
Summary:	udhcp Server/Client Package
Name:		udhcp
Version:	0.9.8
Release:	0.1
Epoch:		0
License:	GPL
Group:		Networking/Daemons
#Group:		Networking/Utilities
Source0:	http://udhcp.busybox.net/source/%{name}-%{version}.tar.gz
# Source0-md5:	2d7e548820d2ded5e183933cb701defb
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-opt.patch
URL:		http://udhcp.busybox.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The udhcp server/client is targeted deliberately at embedded
environments... Other linux DHCP servers out there (such as the ISC
DHCP server) are targeted at larger systems such as PCs (with more
RAM/disk space/etc.). As a result, the udhcp package does not have as
large a feature set as some of these DHCP packages.

Compiled against uClibc, both the server and client binaries are
around 18k and when compiled as one combined binary, has a size of
28k. udhcp is a perfect fit for embedded systems requring DHCP
capabilities.
 
The udhcp server lease file is in binary format making the additional
storage space required for IP and MAC addresses minimal. It also has
the option of storing lease times in absolute form, or relative form,
for systems without a clock. The lease file can also be saved
periodically or by using a signal for systems with flash memory.
 
The client accepts all options on the command line, and calls external
scripts to handle the configuration of interfaces to allow for the
ultimate flexibility.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?with_combined_binary:COMBINED_BINARY=1} \
	OPTFLAGS='%{rpmcflags}'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
/sbin/udhcpc
%attr(755,root,root) %{_bindir}/dumpleases
%attr(755,root,root) %{_sbindir}/udhcpd
%{_mandir}/man1/dumpleases.1*
%{_mandir}/man5/udhcpd.conf.5*
%{_mandir}/man8/udhcpc.8*
%{_mandir}/man8/udhcpd.8*
%{_datadir}/udhcpc
