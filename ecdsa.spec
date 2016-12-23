#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ecdsa
Version  : 0.13
Release  : 20
URL      : https://pypi.python.org/packages/source/e/ecdsa/ecdsa-0.13.tar.gz
Source0  : https://pypi.python.org/packages/source/e/ecdsa/ecdsa-0.13.tar.gz
Summary  : ECDSA cryptographic signature library (pure python)
Group    : Development/Tools
License  : MIT
Requires: ecdsa-python
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pyOpenSSL
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Pure-Python ECDSA
[![build status](https://travis-ci.org/warner/python-ecdsa.png)](http://travis-ci.org/warner/python-ecdsa)
[![Coverage Status](https://coveralls.io/repos/warner/python-ecdsa/badge.svg)](https://coveralls.io/r/warner/python-ecdsa)
[![Latest Version](https://pypip.in/version/ecdsa/badge.svg?style=flat)](https://pypi.python.org/pypi/ecdsa/)

%package python
Summary: python components for the ecdsa package.
Group: Default

%description python
python components for the ecdsa package.


%prep
%setup -q -n ecdsa-0.13

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd py2 ; py.test-2.7 ; popd
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
