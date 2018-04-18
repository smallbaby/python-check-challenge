path=$1
hadoop fs -test -e $path
if [ $? -ne 0 ]; then
    echo "1"
else
	echo "0"
fi
