# $Revision: 1.1 $
%define 	module	pyzmq
%define		zeromq_ver	2.2.0
Summary:	Py0MQ - 0MQ bindings for Python
Summary(en.UTF-8):	Py0MQ - ØMQ bindings for Python
Summary(pl.UTF-8):	Py0MQ - Wiązania biblioteki ØMQ dla Pythona
Name:		python-zmq
Version:	2.2.0.1
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	https://github.com/downloads/zeromq/pyzmq/%{module}-%{version}.tar.gz
# Source0-md5:	f2f80709e84c8ac72d6671eee645d804
URL:		http://github.com/zeromq/pyzmq
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zeromq-devel >= %{zeromq_ver}
%pyrequires_eq	python-libs
Requires:	zeromq >= %{zeromq_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
0MQ bindings for Python.

%description -l en.UTF-8
ØMQ bindings for Python.

%description -l pl.UTF-8
Wiązania biblioteki ØMQ dla Pythona.

%package devel
Summary:	Header files for Py0MQ
Summary(pl.UTF-8):	Pliki nagłowkowe dla Py0MQ
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Py0MQ.

%package -n python3-zmq
Summary:	Py0MQ - ØMQ bindings for Python
Summary(pl.UTF-8):	Py0MQ - Wiązania biblioteki ØMQ dla Pythona
Group:		Development/Languages/Python
%pyrequires_eq  python3-modules
Requires:	zeromq >= %{version}

%description -n python3-zmq
ØMQ bindings for Python 3.x.

%package -n python3-zmq-devel
Summary:	Header files for Py0MQ
Summary(pl.UTF-8):	Pliki nagłowkowe dla Py0MQ
Group:		Development/Languages/Python
Requires:	python3-zmq = %{version}-%{release}

%description -n python3-zmq-devel
Header files for Py0MQ.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build --build-base py2
%{__python3} setup.py build --build-base py3

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py \
	build --build-base py2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__python3} setup.py \
	build --build-base py3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

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
%{py_sitedir}/zmq/core/*.pxd
%dir %{py_sitedir}/zmq/devices
%{py_sitedir}/zmq/devices/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/devices/*.so
%{py_sitedir}/zmq/devices/*.pxd
%dir %{py_sitedir}/zmq/eventloop
%{py_sitedir}/zmq/eventloop/*.py[co]
%dir %{py_sitedir}/zmq/eventloop/platform
%{py_sitedir}/zmq/eventloop/platform/*.py[co]
%dir %{py_sitedir}/zmq/green
%{py_sitedir}/zmq/green/*.py[co]
%dir %{py_sitedir}/zmq/log
%{py_sitedir}/zmq/log/*.py[co]
%dir %{py_sitedir}/zmq/ssh
%{py_sitedir}/zmq/ssh/*.py[co]
%dir %{py_sitedir}/zmq/utils
%{py_sitedir}/zmq/utils/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/utils/*.so
%{py_sitedir}/zmq/utils/*.pxd
%dir %{py_sitedir}/zmq/web
%{py_sitedir}/zmq/web/*.py[co]
%dir %{py_sitedir}/zmq/tests
%{py_sitedir}/zmq/tests/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pyzmq-*.egg-info
%endif

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/zmq/utils/*.h

%files -n python3-zmq
%defattr(644,root,root,755)
%dir %{py3_sitedir}/zmq
%dir %{py3_sitedir}/zmq/core
%dir %{py3_sitedir}/zmq/devices
%dir %{py3_sitedir}/zmq/eventloop
%dir %{py3_sitedir}/zmq/eventloop/platform
%dir %{py3_sitedir}/zmq/green
%dir %{py3_sitedir}/zmq/log
%dir %{py3_sitedir}/zmq/ssh
%dir %{py3_sitedir}/zmq/utils
%dir %{py3_sitedir}/zmq/web
%dir %{py3_sitedir}/zmq/tests
%attr(755,root,root) %{py3_sitedir}/zmq/core/*.so
%attr(755,root,root) %{py3_sitedir}/zmq/devices/*.so
%attr(755,root,root) %{py3_sitedir}/zmq/utils/*.so
%{py3_sitedir}/zmq/*.py
%{py3_sitedir}/zmq/core/*.py
%{py3_sitedir}/zmq/core/*.pxd
%{py3_sitedir}/zmq/devices/*.py
%{py3_sitedir}/zmq/devices/*.pxd
%{py3_sitedir}/zmq/eventloop/*.py
%{py3_sitedir}/zmq/eventloop/platform/*.py
%{py3_sitedir}/zmq/green/*.py
%{py3_sitedir}/zmq/log/*.py
%{py3_sitedir}/zmq/ssh/*.py
%{py3_sitedir}/zmq/utils/*.py
%{py3_sitedir}/zmq/utils/*.pxd
%{py3_sitedir}/zmq/web/*.py
%{py3_sitedir}/zmq/tests/*.py
%{py3_sitedir}/zmq/__pycache__
%{py3_sitedir}/zmq/*/__pycache__
%{py3_sitedir}/zmq/*/*/__pycache__
%{py3_sitedir}/pyzmq-*.egg-info

%files -n python3-zmq-devel
%defattr(644,root,root,755)
%{py3_sitedir}/zmq/utils/*.h
