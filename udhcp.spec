# TODO
# - separate client and server package?
#
# Conditional build:
%bcond_with	uClibc		# link with uClibc
%bcond_with	combined_binary	# combined_binary
#
Summary:	udhcp Server/Client Package
Summary(pl):	Serwer i klient udhcp
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
environments... Other Linux DHCP servers out there (such as the ISC
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

%description -l pl
Serwer/klient udhcp jest przeznaczony dla �rodowisk wbudowanych. Inne
linuksowe serwery DHCP (takie jak serwer DHCP ISC) s� przeznaczone dla
wi�kszych system�w, takich jak PC (z wi�ksz� ilo�ci� RAM-u,
przestrzeni dyskowe itp.). W efekcie pakiet udhcp nie ma tak wielu
mo�liwo�ci jak niekt�re inne pakiety DHCP.

Skompilowane z uClibc binarki serwera i klienta maj� oko�o 18kB, a
skompilowane jako jedna po��czona binarka - 28kB. udhcp �wietnie
pasuje dla system�w wbudowanych wymagaj�cych obs�ugi DHCP.

Plik dzier�aw serwera udhcp jest w formacie binarnym, przez co
wymagana przestrze� na adresy IP i MAC jest minimalna. Ma tak�e opcj�
przechowywania czas�w dzier�awy w postaci absolutnej lub relatywnej
dla system�w bez zegara. Plik dzier�aw mo�e by� tak�e zapisywany
regularnie lub przy u�yciu sygna�u dla system�w z pami�ci� flash.

Klient pobiera wszystkie opcje z linii polece� i wywo�uje zewn�trzne
skrypty do obs�ugi konfiguracji interfejs�w, co daje ostateczn�
elastyczno��.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	%{?with_combined_binary:COMBINED_BINARY=1} \
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
%attr(755,root,root) /sbin/udhcpc
%attr(755,root,root) %{_bindir}/dumpleases
%attr(755,root,root) %{_sbindir}/udhcpd
%{_mandir}/man1/dumpleases.1*
%{_mandir}/man5/udhcpd.conf.5*
%{_mandir}/man8/udhcpc.8*
%{_mandir}/man8/udhcpd.8*
%{_datadir}/udhcpc
