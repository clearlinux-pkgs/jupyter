#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter
Version  : 1.0.0
Release  : 5
URL      : https://pypi.python.org/packages/c9/a9/371d0b8fe37dd231cf4b2cff0a9f0f25e98f3a73c3771742444be27f2944/jupyter-1.0.0.tar.gz
Source0  : https://pypi.python.org/packages/c9/a9/371d0b8fe37dd231cf4b2cff0a9f0f25e98f3a73c3771742444be27f2944/jupyter-1.0.0.tar.gz
Summary  : Jupyter metapackage. Install all the Jupyter components in one go.
Group    : Development/Tools
License  : BSD-3-Clause
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

%description python
python components for the jupyter package.


%prep
%setup -q -n jupyter-1.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488922595
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488922595
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/jupyter.py
%exclude /usr/lib/python2.7/site-packages/jupyter.pyc
%exclude /usr/lib/python3.6/site-packages/__pycache__/jupyter.cpython-36.pyc
%exclude /usr/lib/python3.6/site-packages/jupyter.py
/usr/lib/python*/*
