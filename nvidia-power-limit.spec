%global commit 58b3ef471d642bb1b7563a43664d8d0ce6e52a5c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20190409

%global filename nvidia-pl-90

Name:           nvidia-power-limit
Version:        1.0
Release:        2.%{date}git%{shortcommit}%{?dist}

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
mkdir   -p      %{buildroot}%{_prefix}/lib/systemd/system/
install -p      src/nvidia-pl-90.service %{buildroot}%{_prefix}/lib/systemd/system/
mkdir   -p      %{buildroot}%{_bindir}/
install -p      src/nvidia-pl-90.sh %{buildroot}%{_bindir}/

%post
systemctl enable --now nvidia-pl-90.service

%preun
systemctl disable nvidia-pl-90.service

%files
%doc README.md
%license COPYING
%{_bindir}/%{filename}.sh
%{_prefix}/lib/systemd/system/%{filename}.service

%changelog
* Tue Apr 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-2
- Initial package.
