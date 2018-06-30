.data
string: .asciz "Azeria Labs\n"

.text
.global _start

_start:
    mov r0, #1                  @ STDOUT
    ldr r1, addr_of_string      @ address of string
    mov r2, #13                 @ size of string
    mov r7, #7                  @ 'write' syscall
    swi #0                      @ invoke syscall

_exit:
    mov r7, #1                  @ 'exit' syscall
    swi #0                      @ invoke syscall

addr_of_string: .word string