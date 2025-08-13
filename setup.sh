#!/bin/bash
# 1. Install Miniforge
#wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
#bash Miniforge3-$(uname)-$(uname -m).sh

# 2. Clone the repository
#git clone https://github.com/chrisjihee/LM-based-KG-papers.git
#cd LM-based-KG-papers

# 3. Create a new environment (refer to https://anaconda.org/nvidia/cuda)
conda install -n base conda-forge::conda --all -y
conda create -n LM-based-KG-papers python=3.12 -y
conda activate LM-based-KG-papers
pip install -U -r requirements.txt

# SSH
ssh-add ~/.ssh/id_ed25519  # 신규 등록시
ssh-add -l  # 현재 등록된 키 목록 확인
Get-ChildItem $env:USERPROFILE\.ssh
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
ssh -T git@github.com  # GitHub SSH 연결 확인

# PDF -> TEXT
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install wget
pip install beautifulsoup4
