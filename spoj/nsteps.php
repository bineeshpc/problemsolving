<?php

$num_cases = fgets(STDIN);

$count = 0;

while($count < $num_cases) {
$value_string=fgets(STDIN);
$temp = explode(" ",$value_string);
$x = trim($temp[0]);
$y = trim($temp[1]);

// echo $x, $y;
// echo "\n";
$ys[] = $x;
$y1 = $x-2;
// print_r($ys);
if($y1 >= 0) {
$ys[] = $y1;
}

if(in_array($y, $ys)) {
echo $val = findval($x, $y);
echo "\n";
}
else {
echo "No Number"."\n";
}
unset($ys);
$count++;
}

function findval($x, $y) {
if ($x % 2 == 0 && $y % 2 == 0)
   $final = $x + $y;
else
   $final = $x + $y -1;
return $final;
}

?>