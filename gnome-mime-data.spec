%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	The GNOME virtual file-system libraries
Name:		gnome-mime-data
Version:	2.18.0
Release:	21
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-mime-data/%{url_ver}/%{name}-%{version}.tar.bz2
BuildArch:	noarch
# (fc) 2.3.2-1mdk fix default html viewer
Patch0:		gnome-mime-data-2.4.1-html.patch
# (fc) 2.2.0-2mdk use OOo in preference of abiword (rawhide)
Patch1:		gnome-mime-data-2.4.1-openoffice.patch
# (fc) 2.2.0-2mdk fix default applications (Mdk bug 1505) (rawhide)
Patch2:		gnome-mime-data-2.4.2-default-applications.patch
# (fc) 2.3.1-2mdk add gdesklet magic detection (Mdk bug 4790)
Patch3:		gnome-mime-data-2.18.0-gdesklet.patch
# Use libreoffice (preferred to openoffice) for its types
Patch4:		gnome-mime-data-2.18.0-libreoffice.patch
# Use xdg-open for mostly anything so KDE users get their preferred application too
Patch5:		gnome-mime-data-2.18.0-xdg-open.patch
BuildRequires:	perl-XML-Parser

%description
The GNOME MIME database contains a basic set of applications and MIME
types for a GNOME system.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x --build=%{_host}
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/gnome-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info/*

%files devel
%{_datadir}/pkgconfig/*.pc

