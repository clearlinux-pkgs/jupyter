#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter
Version  : 1.0.0
Release  : 12
URL      : http://pypi.debian.net/jupyter/jupyter-1.0.0.tar.gz
Source0  : http://pypi.debian.net/jupyter/jupyter-1.0.0.tar.gz
Summary  : Jupyter metapackage. Install all the Jupyter components in one go.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jupyter-python3
Requires: jupyter-python
Requires: ipykernel
Requires: ipywidgets
Requires: nbconvert
Requires: notebook
Requires: qtconsole
BuildRequires : ipykernel
BuildRequires : ipywidgets
BuildRequires : jupyter_console
BuildRequires : nbconvert
BuildRequires : notebook
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : qtconsole
BuildRequires : setuptools

%description
# Jupyter
Jupyter metapackage for installation and docs.

%package python
Summary: python components for the jupyter package.
Group: Default
Requires: jupyter-python3

%description python
python components for the jupyter package.


%package python3
Summary: python3 components for the jupyter package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter package.


%prep
%setup -q -n jupyter-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507155626
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.6/site-packages/__pycache__/jupyter.cpython-36.pyc
%exclude /usr/lib/python3.6/site-packages/jupyter.py
/usr/lib/python3*/*
