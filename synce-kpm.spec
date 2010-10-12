Summary:	SynCE KDE PDA Manager
Summary(pl.UTF-8):	Zarządca PDA z projektu SynCE dla KDE
Name:		synce-kpm
Version:	0.15
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	12130b93710b849e18f72752a6949393
URL:		http://www.synce.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PyQt4
Requires:	python-distribute
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
%{py_sitescriptdir}/*.egg-info
