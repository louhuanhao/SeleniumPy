@echo off
color 2
title    设置上网环境
echo                           ☆☆☆☆请选择上网环境☆☆☆☆
echo                            公司固定IP模式=========》按1键
echo                            家用自动获取模式=======》按2键
set/p n=
if /i "%n%" equ "1" goto guding
if /i "%n%" equ "2" goto zidong
: guding
echo 您选择了公司固定IP模式
echo 正在设置，请稍后......
netsh interface ipv4 set address name="以太网" source=static addr=172.20.116.60 mask=255.255.255.0 gateway=172.20.116.1 gwmetric=0 >nul
echo 正在添加本机主DNS...
netsh interface ipv4 set dns name="以太网" source=static addr=172.17.0.2 register=PRIMARY
#echo 正在添加备用DNS...
#netsh interface ipv4 add dns name="以太网" addr=172.17.0.2
goto end
: zidong
echo 您选择了家用自动获取模式
echo 正在设置，请稍后......
echo 自动获取IP地址....
@echo off
netsh interface ip set address name = "以太网" source = dhcp
echo 自动获取DNS服务器....
netsh interface ip set dns name = "以太网" source = dhcp
goto end
 :end
color 6
echo ☆☆☆☆☆☆☆☆本机当前IP配置如下☆☆☆☆☆☆☆☆☆☆☆☆
ipconfig /all
echo ☆☆☆☆☆☆☆☆设置成功!感谢使用☆☆☆☆☆☆☆☆☆☆☆☆
pause