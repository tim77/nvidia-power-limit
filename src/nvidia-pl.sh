#!/usr/bin/bash

# Set desired power limit:
PL=90

nvidia-smi -pm 1
nvidia-smi -pl $PL
