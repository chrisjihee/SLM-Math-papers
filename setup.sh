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
