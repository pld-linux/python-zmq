#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (using network? and finally hang)
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module		pyzmq
%define		zeromq_ver	4.3.2
Summary:	Py0MQ - 0MQ bindings for Python 2
Summary(en.UTF-8):	Py0MQ - ØMQ bindings for Python 2
Summary(pl.UTF-8):	Py0MQ - wiązania biblioteki ØMQ dla Pythona 2
Name:		python-zmq
Version:	19.0.2
Release:	3
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/zeromq/pyzmq/releases
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	dfffada96ae10d3b0afbaa9b8378433e
URL:		http://github.com/zeromq/pyzmq
%if %{with python2}
BuildRequires:	python-Cython >= 0.29
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-gevent
BuildRequires:	python-pytest
BuildRequires:	python-tornado
%endif
%endif
%if %{with python3}
BuildRequires:	python3-Cython >= 0.29
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-gevent
BuildRequires:	python3-pytest
BuildRequires:	python3-tornado
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	zeromq-devel >= %{zeromq_ver}
%if %{with doc}
BuildRequires:	python3-Cython >= 0.29
BuildRequires:	python3-gevent
BuildRequires:	python3-pygments >= 2.4.2
BuildRequires:	sphinx-pdg-3 >= 1.7
%endif
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.3
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

%package apidocs
Summary:	API documentation for Py0MQ module
Summary(pl.UTF-8):	Dokumentacja API modułu Py0MQ
Group:		Documentation

%description apidocs
API documentation for Py0MQ module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Py0MQ.

%prep
%setup -qn %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/zmq/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/zmq/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.md COPYING.BSD README.md
%dir %{py_sitedir}/zmq
%{py_sitedir}/zmq/*.py[co]
%{py_sitedir}/zmq/*.pxd
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
%{py3_sitedir}/zmq/*.pxd
%{py3_sitedir}/zmq/__pycache__
%dir %{py3_sitedir}/zmq/asyncio
%{py3_sitedir}/zmq/asyncio/*.py
%dir %{py3_sitedir}/zmq/auth/asyncio
%{py3_sitedir}/zmq/auth/asyncio/*.py
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
%{py3_sitedir}/zmq/*/__pycache__
%{py3_sitedir}/zmq/*/*/__pycache__
%{py3_sitedir}/pyzmq-%{version}-py*.egg-info

%files -n python3-zmq-devel
%defattr(644,root,root,755)
%{py3_sitedir}/zmq/utils/*.h
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,api,*.html,*.js}
%endif
