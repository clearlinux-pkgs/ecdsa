#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ecdsa
Version  : 0.13.1
Release  : 45
URL      : http://pypi.debian.net/ecdsa/ecdsa-0.13.1.tar.gz
Source0  : http://pypi.debian.net/ecdsa/ecdsa-0.13.1.tar.gz
Summary  : ECDSA cryptographic signature library (pure python)
Group    : Development/Tools
License  : MIT
Requires: ecdsa-license = %{version}-%{release}
Requires: ecdsa-python = %{version}-%{release}
Requires: ecdsa-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : py
BuildRequires : pyOpenSSL
BuildRequires : pytest

%description
# Pure-Python ECDSA
[![build status](https://travis-ci.org/warner/python-ecdsa.png)](http://travis-ci.org/warner/python-ecdsa)
[![Coverage Status](https://coveralls.io/repos/warner/python-ecdsa/badge.svg)](https://coveralls.io/r/warner/python-ecdsa)
[![Latest Version](https://pypip.in/version/ecdsa/badge.svg?style=flat)](https://pypi.python.org/pypi/ecdsa/)

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

%description python3
python3 components for the ecdsa package.


%prep
%setup -q -n ecdsa-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555527507
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ecdsa
cp LICENSE %{buildroot}/usr/share/package-licenses/ecdsa/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ecdsa/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
