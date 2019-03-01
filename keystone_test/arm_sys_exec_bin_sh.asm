;ldr r0, 'nib/'            ; can't handle bytes
str r0, [sp]
;ldr r0, 'hs//'            ; can't handle bytes
str r0, [sp, 4]
mov r0, sp
mov r1, 0
mov r2, 0
;mov r7, __NR_SYS_execve   ; no syscall constants in keystone, must borrow preprocessor from cemu
svc 0
wfi
