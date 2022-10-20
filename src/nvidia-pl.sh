#!/usr/bin/bash

# Set desired power limit:
PL=90

sudo nvidia-smi -pm 1
sudo nvidia-smi -pl $PL
