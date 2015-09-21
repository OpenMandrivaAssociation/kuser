Summary:	Users and groups manager for KDE4
Name:		kuser
Version:	15.08.1
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	kdepimlibs4-devel

%description
Kuser is a tool to create, remove and modify user accounts and groups.

%files
%{_bindir}/kuser
%{_datadir}/applications/kde4/kuser.desktop
%{_datadir}/apps/kuser
%{_datadir}/config.kcfg/kuser.kcfg
%doc %{_docdir}/*/*/kuser
%{_iconsdir}/*/*/*/kuser*

#------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

