#/bin/sh
function f()
{
	remaining=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep percentage | sed s/percentage:// | sed 's/ //g' | sed 's/%//')
	if [ $remaining -le 20 ]
	then
		shutdown -h +3
	else
		date
		echo $remaining
		sleep 60
		f
	fi
}

f
