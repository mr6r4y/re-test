nop
nop
nop
nop
nop

varequ equ 13
var:
    dd 0x123

mov ax, [word var]
mov ax, [var]
mov ax, [varequ]
mov ax, [var+1]
mov ax, [es:var+bx]