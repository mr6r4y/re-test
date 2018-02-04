# Test how overflow of byte register partition is handled

ood
aa
s main
"wa mov rax, 0xf0;add al, 0x22;xor rbx,rbx;mov bl,al @ main+0x4"
db main
dc

