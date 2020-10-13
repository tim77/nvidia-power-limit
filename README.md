# NVIDIA power limit tweak

Systemd startup service for setting power limit on NVIDIA videocards.

### Install

#### 📦 [Fedora [COPR]](https://copr.fedorainfracloud.org/coprs/atim/nvidia-power-limit/)

```
sudo dnf copr enable atim/nvidia-power-limit -y
sudo dnf install nvidia-power-limit
```

#### Run

```
sudo systemctl enable --now nvidia-pl.service
```

### Set power limit setting

```sh
sudoedit /usr/bin/nvidia-pl.sh
```
