%global commit 8646c5f296acc49bafe9c9e2ee7147689bef58fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20201013

%global filename nvidia-pl

Name: nvidia-power-limit
Version: 1.0
Release: 3.%{date}git%{shortcommit}%{?dist}
Summary: NVIDIA power limit tweak
BuildArch: noarch

License: GPLv3+
URL: https://github.com/tim77/nvidia-power-limit
Source0: %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires: systemd-rpm-macros

%description
Systemd startup service for setting power limit on NVIDIA videocards.

To enable:
  systemctl enable --now nvidia-pl.service


%prep
%autosetup -n %{name}-%{commit} -p1


%install
install -Dp src/nvidia-pl.service -t %{buildroot}%{_prefix}/lib/systemd/system/
install -Dp src/nvidia-pl.sh -t %{buildroot}%{_bindir}/


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
* Tue Oct 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-3.20201013git8646c5f
- build(update): commit 8646c5f

* Tue Apr 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0-2
- Initial package.
