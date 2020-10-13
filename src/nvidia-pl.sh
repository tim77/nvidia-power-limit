#!/usr/bin/bash

# Set desired power limit:
PL=90

sleep 5s
sudo nvidia-smi -pm 1
sudo nvidia-smi -pl $PL
