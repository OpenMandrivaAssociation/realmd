Summary:	Kerberos realm enrollment service
Name:		realmd
Version:	0.16.3
Release:	3
License:	LGPLv2+
Group:		System/Configuration/Networking
Url:		http://www.freedesktop.org/software/realmd/
Source0:	http://www.freedesktop.org/software/realmd/releases/realmd-%{version}.tar.gz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	xmlto
BuildRequires:	gettext-devel
BuildRequires:	krb5-devel
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(gio-2.0) >= 2.33.0
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.33.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.33.0
BuildRequires:	pkgconfig(packagekit-glib2)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(systemd)
Requires:		authconfig
Requires:		adcli

%description
realmd is a DBus system service which manages
discovery and enrollment in realms
and domains like Active Directory or IPA. 
The control center uses realmd as the back end
to 'join' a domain simply and automatically configure things correctly.

%package devel-docs
Summary:	Developer documentation files for %{name}

%description devel-docs
The %{name}-devel package contains developer documentation for developing
applications that use %{name}.

%prep
%setup -q
sed -i 's|/usr/bin/python|/usr/bin/python2|' build/tap-driver build/tap-gtester

%build
%serverbuild
%configure
%make

%check
make check

%install
%makeinstall_std

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-%{name}.preset << EOF
enable %{name}.service
EOF

%find_lang realmd

%files -f realmd.lang
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.realmd.conf
%{_sbindir}/realm
%dir %{_prefix}/lib/realmd
%{_prefix}/lib/realmd/realmd
%{_prefix}/lib/realmd/realmd-defaults.conf
%{_prefix}/lib/realmd/realmd-distro.conf
%{_presetdir}/86-%{name}.preset
%{_unitdir}/realmd.service
%{_datadir}/dbus-1/system-services/org.freedesktop.realmd.service
%{_datadir}/polkit-1/actions/org.freedesktop.realmd.policy
%{_mandir}/man8/realm.8.*
%{_mandir}/man5/realmd.conf.5.*
%{_localstatedir}/cache/realmd/

%files devel-docs
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_datadir}/doc/realmd/
