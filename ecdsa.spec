#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ecdsa
Version  : 0.17.0
Release  : 70
URL      : https://files.pythonhosted.org/packages/bf/3d/3d909532ad541651390bf1321e097404cbd39d1d89c2046f42a460220fb3/ecdsa-0.17.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/3d/3d909532ad541651390bf1321e097404cbd39d1d89c2046f42a460220fb3/ecdsa-0.17.0.tar.gz
Summary  : ECDSA cryptographic signature library (pure python)
Group    : Development/Tools
License  : MIT
Requires: ecdsa-license = %{version}-%{release}
Requires: ecdsa-python = %{version}-%{release}
Requires: ecdsa-python3 = %{version}-%{release}
Requires: gmpy2
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : gmpy2
BuildRequires : openssl-dev
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
# Pure-Python ECDSA and ECDH
[![Build Status](https://github.com/tlsfuzzer/python-ecdsa/workflows/GitHub%20CI/badge.svg?branch=master)](https://github.com/tlsfuzzer/python-ecdsa/actions?query=workflow%3A%22GitHub+CI%22+branch%3Amaster)
[![Coverage Status](https://coveralls.io/repos/github/tlsfuzzer/python-ecdsa/badge.svg?branch=master)](https://coveralls.io/github/tlsfuzzer/python-ecdsa?branch=master)
[![condition coverage](https://img.shields.io/badge/condition%20coverage-87%25-yellow)](https://travis-ci.com/github/tlsfuzzer/python-ecdsa/jobs/458951056#L544)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/tlsfuzzer/python-ecdsa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tlsfuzzer/python-ecdsa/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/tlsfuzzer/python-ecdsa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tlsfuzzer/python-ecdsa/alerts/)
[![Latest Version](https://img.shields.io/pypi/v/ecdsa.svg?style=flat)](https://pypi.python.org/pypi/ecdsa/)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)

%package license
Summary: license components for the ecdsa package.
Group: Default

%description license
license components for the ecdsa package.


%package python
Summary: python components for the ecdsa package.
Group: Default
Requires: ecdsa-python3 = %{version}-%{release}

%description python
python components for the ecdsa package.


%package python3
Summary: python3 components for the ecdsa package.
Group: Default
Requires: python3-core
Provides: pypi(ecdsa)
Requires: pypi(six)

%description python3
python3 components for the ecdsa package.


%prep
%setup -q -n ecdsa-0.17.0
cd %{_builddir}/ecdsa-0.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622229126
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
mkdir -p %{buildroot}/usr/share/package-licenses/ecdsa
cp %{_builddir}/ecdsa-0.17.0/LICENSE %{buildroot}/usr/share/package-licenses/ecdsa/a76ad7941d20352544795c378b35864426999206
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ecdsa/a76ad7941d20352544795c378b35864426999206

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
