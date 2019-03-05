_start:
    .arm
    adr r0, _second  ; using the pseudo-instruction `adr` translated into `add    r0,  pc,  #12`
_again:
    bx r0
; test a label in the middle of a thumb block
    .thumb
    mov r2, #16
    add r7, #1
_third:
    adr r4, data     ; pseudo-instruction for data section
    nop
; test a label in the middle of the arm block
    blx _again
_second:
    .arm
    add r3, r1, #1
    blx _third
    nop
data:
    .ascii "/bin/shX"
