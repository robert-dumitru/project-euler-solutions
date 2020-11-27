#lang racket

;Problem 1
;If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
;Find the sum of all the multiples of 3 or 5 below 1000.

(define multiples
  (λ (x) (cond [(= x 1) 0]
               [(= (modulo x 3) 0) (+ x (multiples (- x 1)))]
               [(= (modulo x 5) 0) (+ x (multiples (- x 1)))]
               [else (multiples (- x 1))])))

;Note that our function calculates the sum of multiples below x inclusive.
(multiples 999)
