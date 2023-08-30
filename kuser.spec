Summary:	Users and groups manager
Name:		kuser
Version:	16.08.3
Release:	10
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
Source1:	org.kde.kuser.policy
Patch0:		https://aur.archlinux.org/cgit/aur.git/plain/port_to_kf5.patch?h=kuser-frameworks
Patch1:		kuser-16.08.3-rootonly.patch
Patch2:		kuser-16.08.3-rip-kapplication.patch
Patch3:		kuser-16.08.3-kldap-to-kpimldap.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KPim5Ldap)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake ninja
BuildRequires:	docbook-dtds

%description
Kuser is a tool to create, remove and modify user accounts and groups.

%files
%{_bindir}/kuser
%{_datadir}/applications/kuser.desktop
%{_datadir}/kuser
%{_datadir}/config.kcfg/kuser.kcfg
%{_iconsdir}/*/*/*/kuser*
%{_datadir}/polkit-1/actions/org.kde.kuser.policy
%doc %{_docdir}/*/*/kuser

#------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6 \
    -DKU_FIRSTUID=1000 \
    -DKU_FIRSTGID=1000

%build
%ninja_build -C build

%install
%ninja_install -C build

install -D -c -m 644 %{S:1} %{buildroot}%{_datadir}/polkit-1/actions/org.kde.kuser.policy
