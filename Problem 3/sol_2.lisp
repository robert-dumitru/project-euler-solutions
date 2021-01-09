;;Problem 3
;;The prime factors of 13195 are 5, 7, 13 and 29.
;;What is the largest prime factor of the number 600851475143?

(defun prime-factor (n)
  (when (> n 1)
    (loop with max-d = (isqrt n) for d = 2 then (if (evenp d) (+ d 1) (+ d 2)) do
          (cond ((> d max-d) (return (list n)))
                ((zerop (rem n d)) (return (cons d (prime-factor (truncate n d)))))))))

(last (prime-factor 600851475143))
