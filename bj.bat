@echo off
color 2
title    ������������
echo                           �������ѡ���������������
echo                            ��˾�̶�IPģʽ=========����1��
echo                            �����Զ���ȡģʽ=======����2��
set/p n=
if /i "%n%" equ "1" goto guding
if /i "%n%" equ "2" goto zidong
: guding
echo ��ѡ���˹�˾�̶�IPģʽ
echo �������ã����Ժ�......
netsh interface ipv4 set address name="��̫��" source=static addr=172.20.116.60 mask=255.255.255.0 gateway=172.20.116.1 gwmetric=0 >nul
echo ������ӱ�����DNS...
netsh interface ipv4 set dns name="��̫��" source=static addr=172.17.0.2 register=PRIMARY
#echo ������ӱ���DNS...
#netsh interface ipv4 add dns name="��̫��" addr=172.17.0.2
goto end
: zidong
echo ��ѡ���˼����Զ���ȡģʽ
echo �������ã����Ժ�......
echo �Զ���ȡIP��ַ....
@echo off
netsh interface ip set address name = "��̫��" source = dhcp
echo �Զ���ȡDNS������....
netsh interface ip set dns name = "��̫��" source = dhcp
goto end
 :end
color 6
echo ������������ǰIP�������¡������������
ipconfig /all
echo ������������óɹ�!��лʹ�á������������
pause