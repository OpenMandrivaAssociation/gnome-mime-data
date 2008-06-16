Name:		gnome-mime-data
Summary:	The GNOME virtual file-system libraries
Version:	2.18.0
Release:	%mkrel 4
License:	GPL+
Group:		System/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.3.2-1mdk fix default html viewer
Patch0:		gnome-mime-data-2.4.1-html.patch
# (fc) 2.2.0-2mdk use OOo in preference of abiword (rawhide)
Patch1:		gnome-mime-data-2.4.1-openoffice.patch
# (fc) 2.2.0-2mdk fix default applications (Mdk bug 1505) (rawhide)
Patch2:		gnome-mime-data-2.4.2-default-applications.patch
# (fc) 2.3.1-2mdk add gdesklet magic detection (Mdk bug 4790)
Patch3:		gnome-mime-data-2.3.1-gdesklet.patch
URL:		http://www.gnome.org/
BuildRequires:	perl-XML-Parser
Conflicts:	gnome-vfs < 1.0.5-2mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch

%description
The GNOME MIME database contains a basic set of applications and MIME
types for a GNOME system.

%prep
%setup -q
%patch0 -p1 -b .html
%patch1 -p1 -b .ooo
%patch2 -p1 -b .defaultapp
%patch3 -p1 -b .gdesklet

%build
./configure --prefix=%_prefix --sysconfdir=%_sysconfdir

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/gnome-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info/*
%{_datadir}/pkgconfig/*.pc

