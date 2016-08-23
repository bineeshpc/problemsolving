PID=$(ps -ef|grep [t]esttrap.sh|awk '{print $2}')
echo sending signal to $PID

kill $PID
