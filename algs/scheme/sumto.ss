(define (sumto n)
(if (> n 0)
(+ n (sumto (- n 1)))
0))

(sumto 10)
