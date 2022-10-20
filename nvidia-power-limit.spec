%global filename nvidia-pl

Name: nvidia-power-limit
Version: 1.0.1
Release: 1%{?dist}
Summary: NVIDIA power limit tweak
BuildArch: noarch

License: GPLv3+
URL: https://github.com/tim77/nvidia-power-limit
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: systemd-rpm-macros

%description
Systemd startup service for setting power limit on NVIDIA videocards.

To enable:
  # systemctl enable --now nvidia-pl.service


%prep
%autosetup -p1


%install
install -Dpm 0644 src/nvidia-pl.service -t %{buildroot}%{_prefix}/lib/systemd/system/
install -Dpm 0755 src/nvidia-pl.sh -t %{buildroot}%{_bindir}/


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%doc README.md
%license COPYING
%{_bindir}/%{filename}.sh
%{_unitdir}/*.service


%changelog
* Thu Oct 20 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.1-1
- build(update): 1.0.1

* Tue Oct 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-3.20201013git1d2f076
- build(update): commit 1d2f076

* Tue Apr 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-2
- Initial package.
