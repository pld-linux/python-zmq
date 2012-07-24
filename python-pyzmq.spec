# $Revision: 1.1 $
%define 	module	pyzmq
Summary:	ØMQ bindings for Python
Summary(pl.UTF-8):	Wiązania biblioteki ØMQ dla Pythona
Name:		python-%{module}
Version:	2.2.0
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	https://github.com/downloads/zeromq/pyzmq/%{module}-%{version}.tar.gz
# Source0-md5:	100b73973d6fb235b8da6adea403566e
URL:		http://github.com/zeromq/pyzmq
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zeromq-devel >= %{version}
%pyrequires_eq	python-libs
Requires:	zeromq >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ØMQ bindings for Python.

%description -l pl.UTF-8
Wiązania biblioteki ØMQ dla Pythona.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/zmq/tests
rm -f $RPM_BUILD_ROOT%{py_sitedir}/zmq/{core,devices,utils}/*.pxd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitedir}/zmq
%{py_sitedir}/zmq/*.py[co]
%dir %{py_sitedir}/zmq/core
%{py_sitedir}/zmq/core/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/core/*.so
%dir %{py_sitedir}/zmq/devices
%{py_sitedir}/zmq/devices/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/devices/*.so
%dir %{py_sitedir}/zmq/eventloop
%{py_sitedir}/zmq/eventloop/*.py[co]
%dir %{py_sitedir}/zmq/eventloop/platform
%{py_sitedir}/zmq/eventloop/platform/*.py[co]
%dir %{py_sitedir}/zmq/log
%{py_sitedir}/zmq/log/*.py[co]
%dir %{py_sitedir}/zmq/ssh
%{py_sitedir}/zmq/ssh/*.py[co]
%dir %{py_sitedir}/zmq/utils
%{py_sitedir}/zmq/utils/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/utils/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pyzmq-*.egg-info
%endif
