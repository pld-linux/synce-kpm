# TODO
# - python deps
Summary:	SynCE KDE PDA Manager
Summary(pl.UTF-8):	Zarządca PDA z projektu SynCE dla KDE
Name:		synce-kpm
Version:	0.11
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	89d3f7352ddc7bc64a44353466da802e
URL:		http://www.synce.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.213
Requires:	python-PyQt4
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
	--root=$RPM_BUILD_ROOT

%py_postclean

install -d $RPM_BUILD_ROOT%{_datadir}/synceKPM
mv $RPM_BUILD_ROOT{/usr/synceKPM/data/*,%{_datadir}/synceKPM}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README TODO
%attr(755,root,root) %{_bindir}/synce-kpm
%dir %{py_sitescriptdir}/synceKPM
%dir %{py_sitescriptdir}/synceKPM/dialogs
%dir %{py_sitescriptdir}/synceKPM/util
%{py_sitescriptdir}/synceKPM/*.py[co]
%{py_sitescriptdir}/synceKPM/dialogs/*.py[co]
%{py_sitescriptdir}/synceKPM/util/*.py[co]
%{py_sitescriptdir}/*.egg-info
%{_datadir}/synceKPM