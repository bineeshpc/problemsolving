;x=n / 2 down to 2 is n mod x == 0? then not prime. if i exit without getting 0 then it is prime 
(isprime n
(let (x (/ n 2))
(if (== (/ n x) 0)
false
(isprime (- x 1)))))
