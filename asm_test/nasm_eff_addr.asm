nop
nop
nop
nop
nop

wordvar:
    dd 0x123

mov ax, [dword wordvar]
mov ax, [wordvar]
mov ax, [wordvar+1]
mov ax, [es:wordvar+bx]



