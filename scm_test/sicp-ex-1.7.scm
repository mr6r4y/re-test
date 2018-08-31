(load "sicp-sqrt.scm")


(define (benchm x)
  (begin
    (print (sqrt x))
    (print x)
    (print (square (sqrt x)))))


;; Fail for small numbers
(define small_x 0.0001)
(benchm small_x)

;; Fal for big numbers
(define big_x 999999999999999)
(benchm big_x)


;; Fix to take ratio not constant into account
(define (good-enough? guess x)
  (let 
    ((delta (abs (- (square guess) x))))
    (< (/ delta guess) 0.0001 )))


;; Fail for small numbers
(define small_x 0.0001)
(benchm small_x)

;; Fal for big numbers
(define big_x 999999999999999)
(benchm big_x)