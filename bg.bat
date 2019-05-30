

netsh interface ip set address name="本地连接" source="static" addr="10.1.166.64" mask="255.255.255.0" gateway="10.1.166.1" gwmetric="1"


netsh interface ip set dns name="本地连接" source=static addr="10.1.4.100"
