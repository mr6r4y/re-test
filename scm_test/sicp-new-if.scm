(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

; Infinite loop
(define (p) 
  (p))

;; Returns
;(if #t "true" (p))

;; Never returns
;(if-new #t "true" (p))


