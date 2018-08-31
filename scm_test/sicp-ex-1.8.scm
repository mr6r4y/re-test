(load "sicp-cubert.scm")

;; Test
(define x 1000)
(print (cubert x))
(print (cube (cubert x)))

(define x 8)
(print (cubert x))
(print (cube (cubert x)))