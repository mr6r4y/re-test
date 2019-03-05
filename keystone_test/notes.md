# Playing with Keystone-engine assembler framework

## Charters

### 1 ✓

Make a assemble script

### 2 ✓

Compile DVAR payload

### 3

Make a way to change modes in the middle of the code (from ARM to THUMB and vice versa)

#### Notes

- [Keystone & LLVM](https://www.keystone-engine.org/docs/beyond_llvm.html)
- [Intro to the LLVM MC Project](http://blog.llvm.org/2010/04/intro-to-llvm-mc-project.html)

### 3.1 ✓

Test changing mode (from ARM to THUMB and vice versa):

- test it with `as`
- test it with `keystone`

#### Notes

Keystone does not recognize `.ARM` or `.THUMB` and does not changes between modes. Must be implemented by other means:

```
$ ./keyst-as.py -a arm -m arm dvar_expl.asm 

Instruction count: 55

Binary:

00000000: 01 30 8F E2 13 FF 2F E1  02 00 A0 E3 01 10 A0 E3  .0..../.........
00000010: 02 20 42 E0 C8 70 A0 E3  51 70 87 E2 01 00 00 EF  . B..p..Qp......
00000020: 00 40 A0 E1 9C 10 8F E2  01 20 C1 E5 04 20 C1 E5  .@....... ... ..
00000030: 05 20 C1 E5 06 20 C1 E5  07 20 C1 E5 10 20 A0 E3  . ... ... ... ..
00000040: 01 70 87 E2 01 00 00 EF  00 F0 20 E3 04 00 A0 E1  .p........ .....
00000050: 02 10 A0 E3 02 70 87 E2  01 00 00 EF 04 00 A0 E1  .....p..........
00000060: 01 10 41 E0 02 20 42 E0  01 70 87 E2 01 00 00 EF  ..A.. B..p......
00000070: 00 40 A0 E1 3F 70 A0 E3  04 00 A0 E1 01 10 41 E0  .@..?p........A.
00000080: 01 00 00 EF 04 00 A0 E1  01 10 81 E2 01 00 00 EF  ................
00000090: 04 00 A0 E1 01 10 81 E2  01 00 00 EF 28 00 8F E2  ............(...
000000A0: 01 10 21 E0 04 10 2D E5  04 00 2D E5 0D 10 A0 E1  ..!...-...-.....
000000B0: 02 20 22 E0 04 20 2D E5  07 20 C0 E5 0B 70 A0 E3  . ".. -.. ...p..
000000C0: 01 00 00 EF 00 F0 20 E3  01 01 01 01 2F 62 69 6E  ...... ...../bin
000000D0: 2F 73 68 58                                       /shX

Binary Size: 212
```

GNU as:

```
$ ./gas-arm-as.py dvar_expl.asm

Binary:

00000000: 01 30 8F E2 13 FF 2F E1  02 20 01 21 92 1A C8 27  .0..../.. .!...'
00000010: 51 37 01 DF 04 1C 14 A1  4A 70 0A 71 4A 71 8A 71  Q7......Jp.qJq.q
00000020: CA 71 10 22 01 37 01 DF  C0 46 20 1C 02 21 02 37  .q.".7...F ..!.7
00000030: 01 DF 20 1C 49 1A 92 1A  01 37 01 DF 04 1C 3F 27  .. .I....7....?'
00000040: 20 1C 49 1A 01 DF 20 1C  01 31 01 DF 20 1C 01 31   .I... ..1.. ..1
00000050: 01 DF 07 A0 49 40 02 B4  01 B4 69 46 52 40 04 B4  ....I@....iFR@..
00000060: C2 71 0B 27 01 DF C0 46  02 FF 04 D2 01 01 01 01  .q.'...F........
00000070: 2F 62 69 6E 2F 73 68 58                           /bin/shX

Binary Size: 120
```

### 3.2 ✓

Test changing modes from ARM to THUMB or vice versa when there are labels to the other code part.

#### Notes

`arm_to_thumb_with_labels.asm` compiled with `as` and disassembled instruction by instruction by GDB:

```
; _start:
0x00010054 <+0>:    0c 00 8f e2      add r0, pc, #12          ; pseudo-instruction `adr r0, _second`
; _again:
0x00010058 <+4>:    10 ff 2f e1      bx  r0
; Begin THUMB block
0x0001005c <+8>:    10 22            movs    r2, #16
0x0001005e <+10>:   01 37            adds    r7, #1
; _third:
0x00010060 <+12>:   04 a4            add r4, pc, #16          ; (adr r4, 0x10074 <data>)
0x00010062 <+14>:   c0 46            nop                      ; (mov r8, r8)
0x00010064 <+16>:   ff f7 f8 ef      blx 0x10058 <_again>
; _second:
0x00010068 <+20>:   01 30 81 e2      add r3, r1, #1
0x0001006c <+24>:   fb ff ff fa      blx 0x10060 <_third>
0x00010070 <+28>:   00 00 a0 e1      nop                      ; (mov r0, r0)
; data:
0x00010074 <+32>:  "/bin/shX"
0x0001007c <+40>:  ...
```

Radare2 (analysis fixes thumb/arm blocks):

```
[0x00010054]> pd 12
            ;-- section..text:
            ;-- segment.LOAD0:
            ;-- $a:
            ;-- _start:
            ;-- pc:
            ;-- r15:
┌ (fcn) entry0 4
│   entry0 ();
└           0x00010054      0c008fe2       add r0, pc, 0xc             ; 0x10068 ; loc._a_1 ; [01] -rwx section size 40 named .text
┌ (fcn) loc._again 4
│   loc._again ();
│           ; CALL XREF from loc._third (0x10064)
└           0x00010058      10ff2fe1       bx r0
            ;-- $t:
            0x0001005c      1022           movs r2, 0x10
            0x0001005e      0137           adds r7, 1
┌ (fcn) loc._third (arm) 28
│   loc._third ();
│           ; CALL XREF from loc._third (0x1006c)
│           0x00010060      04a4           adr r4, 0x10                ; loc._d ; 0x10074 ; "/bin/shX\xff..."
│           0x00010062      c046           mov r8, r8
│           ;-- syscall.exit:
│           0x00010064      fff7f8ef       blx loc._again
│           ;-- _second:
│           ;-- $a:
│           ; DATA XREF from entry0 (0x10054)
│           0x00010068      013081e2       add r3, r1, 1
│           0x0001006c      fbfffffa       blx loc._third
│           0x00010070      0000a0e1       mov r0, r0
│           ;-- data:
│           ;-- $d:
│           ; DATA XREF from loc._third (0x10060)
│           0x00010074      2f62696e       invalid
└           0x00010078      2f736858       stmdapl r8!, {r0, r1, r2, r3, r5, r8, sb, ip, sp, lr} ^
```

### 3.2.1 ✓

Debug/emulate `arm_to_thumb_with_labels.asm` on close to real environment. `cemu` does not figure out the arm->thumb/thumb->arm switching.

#### Notes

- [Cross debugging for ARM / MIPS ELF with QEMU/toolchain](https://reverseengineering.stackexchange.com/questions/8829/cross-debugging-for-arm-mips-elf-with-qemu-toolchain)

1. in SHELL: `qemu-arm -g 4444 /tmp/tmp-as.x `
1. in another SHELL: `gdb-multiarch /tmp/tmp-as.x`
1. in GDB: `set architecture arm`
1. in GDB: `target remote localhost:4444`

### 3.3

Figure out differences between keystone and GNU as for ARM THUMB.

The following code:

```
.THUMB
str r0, [sp]
str r0, [sp, #4]
mov r0, sp
mov r1, #0
mov r2, #0
svc #0
wfi
```

compiled with GNU as:

```
Binary:

00000000: 00 90 01 90 68 46 00 21  00 22 00 DF 30 BF        ....hF.!."..0.

String Payload:

b'\x00\x90\x01\x90hF\x00!\x00"\x00\xdf0\xbf'

Binary Size: 14

```

compiled with Keystone:

```
Instruction count: 7

Binary:

00000000: 00 90 01 90 68 46 4F F0  00 01 4F F0 00 02 00 DF  ....hFO...O.....
00000010: 30 BF                                             0.

String Payload:

b'\x00\x90\x01\x90hFO\xf0\x00\x01O\xf0\x00\x02\x00\xdf0\xbf'

Binary Size: 18
```

### 4 ✓

Implement similar script to `keyst-as.py` that uses `as` and test if the compiled code is similar to Keystone.

### 4.1

Test for x86 code. Add AT&T syntax sample.

### 5

Fix `re-test/keystone_test/keyst-as.py` to be able to `|` multiple modes set from command line.

### 6

Make test-bed for Keystone payloads in custom ELF compiled with `nop` sled and automate making it.
