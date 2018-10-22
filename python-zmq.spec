#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module		pyzmq
%define		zeromq_ver	4.1.2
Summary:	Py0MQ - 0MQ bindings for Python 2
Summary(en.UTF-8):	Py0MQ - ØMQ bindings for Python 2
Summary(pl.UTF-8):	Py0MQ - wiązania biblioteki ØMQ dla Pythona 2
Name:		python-zmq
Version:	17.0.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	29dcd90cd6e862ce9b4a0e5efd74ada8
URL:		http://github.com/zeromq/pyzmq
%if %{with python2}
BuildRequires:	python-Cython >= 0.16
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.16
BuildRequires:	python3-devel >= 3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	zeromq-devel >= %{zeromq_ver}
Requires:	python-modules >= 1:2.6
Requires:	python-tornado
Requires:	zeromq >= %{zeromq_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
0MQ bindings for Python 2.

%description -l en.UTF-8
ØMQ bindings for Python 2.

%description -l pl.UTF-8
Wiązania biblioteki ØMQ dla Pythona 2.

%package devel
Summary:	Header files for Py0MQ (Python 2 version)
Summary(pl.UTF-8):	Pliki nagłowkowe dla Py0MQ (wersja dla Pythona 2)
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Py0MQ (Python 2 version).

%description devel -l pl.UTF-8
Pliki nagłowkowe dla Py0MQ (wersja dla Pythona 2).

%package -n python3-zmq
Summary:	Py0MQ - 0MQ bindings for Python 3
Summary(en.UTF-8):	Py0MQ - ØMQ bindings for Python 3
Summary(pl.UTF-8):	Py0MQ - wiązania biblioteki ØMQ dla Pythona
Group:		Development/Languages/Python
Requires:	python3-modules >= 3.2
Requires:	python3-tornado
Requires:	zeromq >= %{zeromq_ver}

%description -n python3-zmq
0MQ bindings for Python 3.

%description -n python3-zmq -l en.UTF-8
ØMQ bindings for Python 3.

%description -n python3-zmq -l pl.UTF-8
Wiązania biblioteki ØMQ dla Pythona 3.

%package -n python3-zmq-devel
Summary:	Header files for Py0MQ (Python 3 version)
Summary(pl.UTF-8):	Pliki nagłowkowe dla Py0MQ (wersja dla Pythona 3)
Group:		Development/Languages/Python
Requires:	python3-zmq = %{version}-%{release}

%description -n python3-zmq-devel
Header files for Py0MQ (Python 3 version).

%description -n python3-zmq-devel -l pl.UTF-8
Pliki nagłowkowe dla Py0MQ (wersja dla Pythona 3).

%prep
%setup -qn %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.md COPYING.BSD README.md
%dir %{py_sitedir}/zmq
%{py_sitedir}/zmq/*.py[co]
%dir %{py_sitedir}/zmq/auth
%{py_sitedir}/zmq/auth/*.py[co]
%dir %{py_sitedir}/zmq/backend
%{py_sitedir}/zmq/backend/*.py[co]
%dir %{py_sitedir}/zmq/backend/cffi
%{py_sitedir}/zmq/backend/cffi/*.[ch]
%{py_sitedir}/zmq/backend/cffi/*.py[co]
%dir %{py_sitedir}/zmq/backend/cython
%{py_sitedir}/zmq/backend/cython/*.py[co]
%{py_sitedir}/zmq/backend/cython/*.pxd
%{py_sitedir}/zmq/backend/cython/*.pxi
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
%{py_sitedir}/zmq/utils/*.pxd
%dir %{py_sitedir}/zmq/tests
%{py_sitedir}/zmq/tests/*.py[co]
%{py_sitedir}/pyzmq-%{version}-py*.egg-info

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/zmq/utils/*.h
%endif

%if %{with python3}
%files -n python3-zmq
%defattr(644,root,root,755)
%doc AUTHORS.md COPYING.BSD README.md
%dir %{py3_sitedir}/zmq
%{py3_sitedir}/zmq/*.py
%{py3_sitedir}/zmq/__pycache__
%dir %{py3_sitedir}/zmq/asyncio
%{py3_sitedir}/zmq/asyncio/*.py
%dir %{py3_sitedir}/zmq/auth/asyncio
%{py3_sitedir}/zmq/auth/asyncio/*.py
%dir %{py3_sitedir}/zmq/tests/asyncio
%{py3_sitedir}/zmq/tests/asyncio/*.py
%dir %{py3_sitedir}/zmq/auth
%{py3_sitedir}/zmq/auth/*.py
%dir %{py3_sitedir}/zmq/backend
%{py3_sitedir}/zmq/backend/*.py
%dir %{py3_sitedir}/zmq/backend/cffi
%{py3_sitedir}/zmq/backend/cffi/*.[ch]
%{py3_sitedir}/zmq/backend/cffi/*.py
%dir %{py3_sitedir}/zmq/backend/cython
%attr(755,root,root) %{py3_sitedir}/zmq/backend/cython/*.so
%{py3_sitedir}/zmq/backend/cython/*.py
%{py3_sitedir}/zmq/backend/cython/*.pxd
%{py3_sitedir}/zmq/backend/cython/*.pxi
%dir %{py3_sitedir}/zmq/devices
%{py3_sitedir}/zmq/devices/*.py
%{py3_sitedir}/zmq/devices/*.pxd
%attr(755,root,root) %{py3_sitedir}/zmq/devices/*.so
%dir %{py3_sitedir}/zmq/eventloop
%{py3_sitedir}/zmq/eventloop/*.py
%dir %{py3_sitedir}/zmq/eventloop/minitornado
%{py3_sitedir}/zmq/eventloop/minitornado/*.py
%dir %{py3_sitedir}/zmq/eventloop/minitornado/platform
%{py3_sitedir}/zmq/eventloop/minitornado/platform/*.py
%{py3_sitedir}/zmq/eventloop/minitornado/platform/__pycache__
%dir %{py3_sitedir}/zmq/green
%{py3_sitedir}/zmq/green/*.py
%dir %{py3_sitedir}/zmq/green/eventloop
%{py3_sitedir}/zmq/green/eventloop/*.py
%dir %{py3_sitedir}/zmq/log
%{py3_sitedir}/zmq/log/*.py
%dir %{py3_sitedir}/zmq/ssh
%{py3_sitedir}/zmq/ssh/*.py
%dir %{py3_sitedir}/zmq/sugar
%{py3_sitedir}/zmq/sugar/*.py
%dir %{py3_sitedir}/zmq/utils
%{py3_sitedir}/zmq/utils/*.py
%{py3_sitedir}/zmq/utils/*.pxd
%{py3_sitedir}/zmq/utils/*.json
%dir %{py3_sitedir}/zmq/tests
%{py3_sitedir}/zmq/tests/*.py
%{py3_sitedir}/zmq/*/__pycache__
%{py3_sitedir}/zmq/*/*/__pycache__
%{py3_sitedir}/pyzmq-%{version}-py*.egg-info

%files -n python3-zmq-devel
%defattr(644,root,root,755)
%{py3_sitedir}/zmq/utils/*.h
%endif
