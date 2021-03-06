(define (square x)
  (* x x))

(define (cube x)
  (* x x x))

(define (good-enough? guess x)
  (let 
    ((delta (abs (- (cube guess) x))))
    (< (/ delta guess) 0.0001 )))

(define (improve guess x)
  (/ (+ (/ x (square guess)) (* 2 guess)) 3))

(define (cubert-iter guess x)
  (if (good-enough? guess x)
      guess
      (cubert-iter (improve guess x) 
                   x)))

(define (cubert x)
  (cubert-iter 1.0 x))