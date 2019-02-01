#! /bin/sh
filename=$(mktemp /tmp/brun.XXXXXXX)
sh run.sh | tee $filename 
filepath=$(tail -2 $filename | head -1| sed 's@.*:\s*@file://@' )
echo $filepath
firefox $filepath &
reportpath=$(tail -1 $filename | sed 's@.*:\s*@file://@' )
echo $reportpath
firefox $reportpath &
rm $filename
