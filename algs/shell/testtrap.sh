#!/bin/sh

# Program to print a text file with headers and footers

TEMP_FILE=/tmp/printfile.txt

clean_up() {

	# Perform program exit housekeeping
        echo "executing cleanup code"
	rm $TEMP_FILE 
	exit
}

trap clean_up HUP INT TERM

echo "blah" > $TEMP_FILE
echo "cat it?"
read reply
if [ "$reply" = "y" ]; then
        echo printing $TEMP_FILE
	cat $TEMP_FILE
fi
clean_up
