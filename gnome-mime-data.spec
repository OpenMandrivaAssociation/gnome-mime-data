Name:		gnome-mime-data
Summary:	The GNOME virtual file-system libraries
Version:	2.18.0
Release:	%mkrel 9
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
Patch3:		gnome-mime-data-2.18.0-gdesklet.patch
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
%configure2_5x --build=%_host
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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.18.0-8mdv2011.0
+ Revision: 664875
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.18.0-7mdv2011.0
+ Revision: 605472
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.18.0-6mdv2010.1
+ Revision: 521487
- rebuilt for 2010.1

* Fri Mar 20 2009 Funda Wang <fwang@mandriva.org> 2.18.0-5mdv2009.1
+ Revision: 358492
- rediff gdesklet patch

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.18.0-4mdv2009.0
+ Revision: 221088
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.18.0-3mdv2008.1
+ Revision: 150194
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 2.18.0-2mdv2008.0
+ Revision: 91284
- rebuild for 2008
- correct license, new license policy
- slight spec clean


* Thu Apr 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 150663
- new version
- make it a noarch package

* Wed Nov 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.3-2mdv2007.1
+ Revision: 78051
- bot rebuild
- Import gnome-mime-data

* Wed Nov 08 2006 Götz Waschk <waschk@mandriva.org> 2.4.3-1mdv2007.1
- unpack patches
- drop patch 6
- New version 2.4.3

* Wed Feb 02 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.2-3mdk 
- Drop menu methods, mime type are no longer handled this way

* Thu Nov 11 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.2-2mdk
- fix buildrequires

* Wed Oct 27 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.2-1mdk
- New release 2.4.2
- Regenerate patch2 (partially merged)
- Remove patches 4, 5 (merged upstream)

* Fri Oct 01 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.4.1-10mdk
- lib64 fixes to pkgconfig files

* Fri Sep 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.1-9mdk
- Add infos for doc files

* Wed Aug 04 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.1-8mdk
- Update path 2 to set back totem as default player for playlist

* Fri Jun 25 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.1-7mdk
- Patch5 : fix gvim name and command (Anthill bug #832)

* Tue May 11 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.1-6mdk
- Update patch 2 to use rhythmbox as default music player instead of totem

