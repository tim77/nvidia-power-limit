%global filename nvidia-pl-90

Name:           nvidia-power-limit
Version:        1.0
Release:        1%{?dist}

Summary:        NVIDIA power limit tweak

License:        GPLv3+
URL:            https://github.com/tim77/nvidia-power-limit
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

%description
Systemd startup service for setting power limit on NVIDIA videocards.

%prep
%autosetup -n %{name}

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
* Sat Apr 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-1
- Initial package.
