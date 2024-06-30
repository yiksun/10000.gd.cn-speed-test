# 10000.gd.cn-speed-test
Speed test on http://10000.gd.cn/ by selenium

## Python virtual environment
```bash
apt-get update
apt-get install python3-pip
apt install python3.11-venv
python3 -m venv <path here>
```

## Install chromium & driver
```bash
apt-get update
apt-get install chromium
apt-get install chromium-driver
```

## (可选) 免安装ChromeDriver by Electron
[ChromeDriver by Electron](https://github.com/electron/electron/)

`apt-get install libnss3 (可选, 只有当提示libnss3.so missing时才安装)`

## 反爬虫
[stealth.min.js](https://github.com/requireCool/stealth.min.js)
