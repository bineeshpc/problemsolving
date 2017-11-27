;; http://www.spoj.com/problems/FASHION/

(ns fashion
  (:require [clojure.string :as str]))

(defn read_num[] 
    (def str1 (read-line))
    (def number (read-string str1))
    number
)

(defn read_participants[]
    (def nums (map read-string (str/split (read-line) #" ")))
    nums
)

(defn process_testcase[]
    (def num_participants (read_num))
    (def men (read_participants))
    (def women (read_participants))
    (def s (reduce + 0 (map * men women)))
    (println s)
)

(defn process[num_cases] 
    (if (= num_cases 0)
    true
     (do
        (process_testcase) 
        (process (- num_cases 1)) 
     )
    )
)

(def num_cases (read_num))
(process num_cases)