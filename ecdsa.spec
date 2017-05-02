#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ecdsa
Version  : 0.13
Release  : 24
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
export LANG=C
export SOURCE_DATE_EPOCH=1484545712
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484545712
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
