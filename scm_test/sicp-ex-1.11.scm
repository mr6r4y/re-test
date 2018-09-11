(define (f-recur n)
  (cond ((< n 3) 
         n)
        ((>= n 3) 
         (+ (f-recur (- n 1)) 
            (* (f-recur (- n 2)) 2) 
            (* (f-recur (- n 3)) 3)))))

(define (f-iter n)
  (define (f-iter^ a b c count)
    (if (= count 0)
        c
        (f-iter^
          (+ a (* 2 b) (* 3 c))
          a
          b
          (- count 1))))
  (f-iter^ 2 1 0 n))
  
(print (f-recur 0))
(print (f-recur 1))
(print (f-recur 2))

(print (f-recur 5))
(print (f-iter 5))
