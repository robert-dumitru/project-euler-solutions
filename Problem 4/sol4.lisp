(defun largest-palindrome (n &optional (r 1))
  (if (dotimes
          (i (/ (+ r 1) 2))
        (if (palindrome? (* (- (expt 10 n) i 1) (+ (- (expt 10 n) r) i)))
            (return (* (- (expt 10 n) i 1) (+ (- (expt 10 n) r) i)))))
      (largest-palindrome n (+ r 1))))

(defun palindrome? (x)
  (equal (write-to-string x) (reverse (write-to-string x))))

(largest-palindrome 3)
