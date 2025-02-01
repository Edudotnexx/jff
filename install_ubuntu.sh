#!/bin/bash

apt-get update -y && apt-get install tesseract-ocr tesseract-ocr-eng python3-pip libglvnd-dev jq -y

# Get the current pip version
pip_version=$(pip --version | awk '{print $2}')

# Compare pip version with 23.0.0
version_comparison=$(echo -e "$pip_version\n23.0.0" | sort -V | head -n 1)

# If pip version is older than 23.0.0, don't include --break-system-packages
if [[ "$version_comparison" == "$pip_version" ]]; then
    echo "pip version is older than 23.0.0. Installing without --break-system-packages."
    pip install dawshs-jff
else
    echo "pip version is 23.0.0 or newer. Installing with --break-system-packages."
    pip install dawshs-jff --break-system-packages
fi
