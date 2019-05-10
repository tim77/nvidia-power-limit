%global commit 171ff16bd7d6c7dd540e0668f2302786b6f25640
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20190510

%global filename nvidia-pl-90

Name:           nvidia-power-limit
Version:        1.0
Release:        3.%{date}git%{shortcommit}%{?dist}

Summary:        NVIDIA power limit tweak

License:        GPLv3+
URL:            https://github.com/tim77/nvidia-power-limit
Source0:        %{url}/tarball/%{commit}#/%{name}-%{version}.%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Systemd startup service for setting power limit on NVIDIA videocards.

%prep
%autosetup -n tim77-%{name}-%{shortcommit}

%install
mkdir   -p %{buildroot}%{_prefix}/lib/systemd/system/
install -p src/%{filename}.service %{buildroot}%{_prefix}/lib/systemd/system/
mkdir   -p %{buildroot}%{_bindir}/
install -p src/%{filename}.sh %{buildroot}%{_bindir}/

%post
systemctl enable --now %{filename}.service

%preun
systemctl disable %{filename}.service

%files
%doc README.md
%license COPYING
%{_bindir}/%{filename}.sh
%{_prefix}/lib/systemd/system/%{filename}.service

%changelog
* Fri May 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-3.20190510git171ff16
- Update spec file

* Tue Apr 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-2
- Initial package
