Name:     xkeyboard-config-martin
Version:  0.1.0
Release:  1%{?dist}
Summary:  Keyboard bindings for Martin

License:	WTFPL
URL:      https://github.com/marhag87/xkeyboard-config-martin
Source0:  https://github.com/marhag87/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires: xkeyboard-config

%define debug_package %{nil}
%define datadir %{_datarootdir}/X11/xkb/symbols

%description
Personal keyboard bindings for Martin

%prep
%autosetup -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{datadir}
mv martin %{buildroot}%{datadir}

%files
%{datadir}/martin


%changelog
* Wed Sep 13 2017 Martin Hagstrom <marhag87@gmail.com> 0.1.0-1
- Initial release
