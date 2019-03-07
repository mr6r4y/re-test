.thumb
_start:
    ; ldr r0, #0x6e69622f       ; 'nib/' ; can't handle bytes in str
    str r0, [sp]
    ; ldr r0, #0x68732f2f            ; 'hs//' ; can't handle bytes
    str r0, [sp, #4]
    mov r0, sp
    mov r1, #0
    mov r2, #0
    ; 87: #define __NR_execve             59
    mov r7, #59   ; no syscall constants in keystone, must borrow preprocessor from cemu
    svc #0
    wfi


