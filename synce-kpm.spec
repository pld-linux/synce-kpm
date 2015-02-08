Summary:	SynCE KDE PDA Manager
Summary(pl.UTF-8):	Zarządca PDA z projektu SynCE dla KDE
Name:		synce-kpm
Version:	0.16
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	5e4b79e13488010e89c9c523a44945ea
URL:		http://www.synce.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PyQt4
Requires:	python-dbus
Requires:	python-distribute
Requires:	python-libxml2 >= 2
Requires:	python-libxslt
Requires:	python-pyrapi2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Device Manager for WM5+ devices for KDE.

%description -l pl.UTF-8
Zarządca urządzeń WM5+ dla KDE, pochodzący z projektu SynCE.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/synce-kpm
%dir %{py_sitescriptdir}/synceKPM
%{py_sitescriptdir}/synceKPM/*.py[co]
%{py_sitescriptdir}/synceKPM/data
%dir %{py_sitescriptdir}/synceKPM/dataserver
%{py_sitescriptdir}/synceKPM/dataserver/*.py[co]
%dir %{py_sitescriptdir}/synceKPM/gui
%{py_sitescriptdir}/synceKPM/gui/*.py[co]
%{py_sitescriptdir}/synce_kpm-%{version}-py*.egg-info
