# -Selenium
学校网络12小时就要输入账号密码，写了个脚本，监测是否有网络，没网络输入账号密码
下载geckodriver驱动15.0的

https://github.com/mozilla/geckodriver/releases?after=v0.16.0

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install iceweasel

whereis iceweasel
iceweasel -version

sudo chmod -R 777 geckodriver
sudo apt-get install xvfb
Xvfb -ac :7 -screen 0 1280x1024x8 -extension RANDR -nolisten inet6 &