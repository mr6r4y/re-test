_start:
    .ARM
    adr r0, _second  ; using the pseudo-instruction `adr` translated into `add    r0,  pc,  #12`
    bx r0
_third:
    .THUMB
    mov r2, #16
    add r7, #1
    adr r4, data     ; pseudo-instruction for data section
    nop
    blx _start
_second:
    .ARM
    add r3, r1, #1
    blx _third
    nop
data:
    .ascii "/bin/shX"
