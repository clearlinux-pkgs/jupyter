#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter
Version  : 1.0.0
Release  : 46
URL      : http://pypi.debian.net/jupyter/jupyter-1.0.0.tar.gz
Source0  : http://pypi.debian.net/jupyter/jupyter-1.0.0.tar.gz
Summary  : Jupyter metapackage. Install all the Jupyter components in one go.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyter-license = %{version}-%{release}
Requires: jupyter-python = %{version}-%{release}
Requires: jupyter-python3 = %{version}-%{release}
Requires: ipykernel
Requires: ipywidgets
Requires: nbconvert
Requires: notebook
Requires: qtconsole
BuildRequires : buildreq-distutils3
BuildRequires : ipykernel
BuildRequires : ipywidgets
BuildRequires : jupyter_console
BuildRequires : nbconvert
BuildRequires : notebook
BuildRequires : qtconsole

%description
# Jupyter
Jupyter metapackage for installation and docs.

%package license
Summary: license components for the jupyter package.
Group: Default

%description license
license components for the jupyter package.


%package python
Summary: python components for the jupyter package.
Group: Default
Requires: jupyter-python3 = %{version}-%{release}

%description python
python components for the jupyter package.


%package python3
Summary: python3 components for the jupyter package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter)
Requires: pypi(ipykernel)
Requires: pypi(ipywidgets)
Requires: pypi(jupyter_console)
Requires: pypi(nbconvert)
Requires: pypi(notebook)
Requires: pypi(qtconsole)

%description python3
python3 components for the jupyter package.


%prep
%setup -q -n jupyter-1.0.0
cd %{_builddir}/jupyter-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607995905
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter
cp %{_builddir}/jupyter-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/jupyter/f39106d74c0b8b0d8dafe590ad8600ddf8eca7f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/__pycache__/jupyter.cpython-3*.pyc
rm -f %{buildroot}/usr/lib/python3*/site-packages/jupyter.py

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter/f39106d74c0b8b0d8dafe590ad8600ddf8eca7f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
