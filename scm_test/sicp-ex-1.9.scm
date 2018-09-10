(define (inc a)
  (+ a 1))

(define (dec a)
  (- a 1))

(define (plus a b)
  (if (= a 0)
      b
      (inc (plus (dec a) b))))

(define (plusb a b)
  (if (= a 0)
      b
      (plusb (dec a) (inc b))))

(print (plus 4 5))

(print (plusb 4 5))
