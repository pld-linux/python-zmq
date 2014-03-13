# $Revision: 1.1 $
%define		module	pyzmq
%define		zeromq_ver	4.0.4
Summary:	Py0MQ - 0MQ bindings for Python
Summary(en.UTF-8):	Py0MQ - ØMQ bindings for Python
Summary(pl.UTF-8):	Py0MQ - Wiązania biblioteki ØMQ dla Pythona
Name:		python-zmq
Version:	14.1.0
Release:	1
License:	GPL v3
Group:		Development/Languages/Python
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}.tar.gz
# Source0-md5:	2bd82efad3cbddf5cc7dffe57e46a224
URL:		http://github.com/zeromq/pyzmq
BuildRequires:	python-Cython
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	zeromq-devel >= %{zeromq_ver}
%pyrequires_eq	python-libs
Requires:	zeromq >= %{zeromq_ver}
Requires:	python-tornado
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
Requires:	zeromq >= %{zeromq_ver}
Requires:	python3-tornado

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
%doc AUTHORS.md README.md
%dir %{py_sitedir}/zmq
%{py_sitedir}/zmq/*.py[co]
%dir %{py_sitedir}/zmq/auth
%{py_sitedir}/zmq/auth/*.py[co]
%dir %{py_sitedir}/zmq/backend
%{py_sitedir}/zmq/backend/*.py[co]
%dir %{py_sitedir}/zmq/backend/cffi
%{py_sitedir}/zmq/backend/cffi/*.py[co]
%dir %{py_sitedir}/zmq/backend/cython
%{py_sitedir}/zmq/backend/cython/*.py[co]
%{py_sitedir}/zmq/backend/cython/*.pxd
%attr(755,root,root) %{py_sitedir}/zmq/backend/cython/*.so
%dir %{py_sitedir}/zmq/devices
%{py_sitedir}/zmq/devices/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/devices/*.so
%{py_sitedir}/zmq/devices/*.pxd
%dir %{py_sitedir}/zmq/eventloop
%{py_sitedir}/zmq/eventloop/*.py[co]
%dir %{py_sitedir}/zmq/eventloop/minitornado
%{py_sitedir}/zmq/eventloop/minitornado/*.py[co]
%dir %{py_sitedir}/zmq/eventloop/minitornado/platform
%{py_sitedir}/zmq/eventloop/minitornado/platform/*.py[co]
%dir %{py_sitedir}/zmq/green
%{py_sitedir}/zmq/green/*.py[co]
%dir %{py_sitedir}/zmq/green/eventloop
%{py_sitedir}/zmq/green/eventloop/*.py[co]
%dir %{py_sitedir}/zmq/log
%{py_sitedir}/zmq/log/*.py[co]
%dir %{py_sitedir}/zmq/ssh
%{py_sitedir}/zmq/ssh/*.py[co]
%dir %{py_sitedir}/zmq/sugar
%{py_sitedir}/zmq/sugar/*.py[co]
%dir %{py_sitedir}/zmq/utils
%{py_sitedir}/zmq/utils/*.json
%{py_sitedir}/zmq/utils/*.py[co]
%attr(755,root,root) %{py_sitedir}/zmq/utils/*.so
%{py_sitedir}/zmq/utils/*.pxd
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
%doc AUTHORS.md README.md
%dir %{py3_sitedir}/zmq
%dir %{py3_sitedir}/zmq/auth
%dir %{py3_sitedir}/zmq/backend
%dir %{py3_sitedir}/zmq/backend/cffi
%dir %{py3_sitedir}/zmq/backend/cython
%dir %{py3_sitedir}/zmq/devices
%dir %{py3_sitedir}/zmq/eventloop
%dir %{py3_sitedir}/zmq/eventloop/minitornado
%dir %{py3_sitedir}/zmq/eventloop/minitornado/platform
%dir %{py3_sitedir}/zmq/green
%dir %{py3_sitedir}/zmq/green/eventloop
%dir %{py3_sitedir}/zmq/log
%dir %{py3_sitedir}/zmq/ssh
%dir %{py3_sitedir}/zmq/sugar
%dir %{py3_sitedir}/zmq/utils
%dir %{py3_sitedir}/zmq/tests
%attr(755,root,root) %{py3_sitedir}/zmq/backend/cython/*.so
%attr(755,root,root) %{py3_sitedir}/zmq/devices/*.so
%attr(755,root,root) %{py3_sitedir}/zmq/utils/*.so
%{py3_sitedir}/zmq/*.py
%{py3_sitedir}/zmq/auth/*.py
%{py3_sitedir}/zmq/backend/*.py
%{py3_sitedir}/zmq/backend/cffi/*.py
%{py3_sitedir}/zmq/backend/cython/*.py
%{py3_sitedir}/zmq/backend/cython/*.pxd
%{py3_sitedir}/zmq/devices/*.py
%{py3_sitedir}/zmq/devices/*.pxd
%{py3_sitedir}/zmq/eventloop/*.py
%{py3_sitedir}/zmq/eventloop/minitornado/*.py
%{py3_sitedir}/zmq/eventloop/minitornado/platform/*.py
%{py3_sitedir}/zmq/eventloop/minitornado/platform/__pycache__
%{py3_sitedir}/zmq/green/*.py
%{py3_sitedir}/zmq/green/eventloop/*.py
%{py3_sitedir}/zmq/log/*.py
%{py3_sitedir}/zmq/ssh/*.py
%{py3_sitedir}/zmq/sugar/*.py
%{py3_sitedir}/zmq/utils/*.py
%{py3_sitedir}/zmq/utils/*.pxd
%{py3_sitedir}/zmq/utils/*.json
%{py3_sitedir}/zmq/tests/*.py
%{py3_sitedir}/zmq/__pycache__
%{py3_sitedir}/zmq/*/__pycache__
%{py3_sitedir}/zmq/*/*/__pycache__
%{py3_sitedir}/pyzmq-*.egg-info

%files -n python3-zmq-devel
%defattr(644,root,root,755)
%{py3_sitedir}/zmq/utils/*.h
