;; http://www.spoj.com/problems/SAMER08F/

(defn num_squares [n] 
(/ (* n (+ n 1) (+ (* 2 n) 1) ) 6)
)

(while true
(do
    (def str1 (read-line))
    (def number (read-string str1))
    (if (= number 0)
    (System/exit 0))
    (println (num_squares number))
))