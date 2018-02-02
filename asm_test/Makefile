all: patchme patchme_x86 patchme_nostd patchme_nostd_x86 imul_x64.bin imul_x32.bin boot nasm_eff_addr.rasm.asm nasm_eff_addr

patchme: patchme.c
	gcc -o $@ $^

patchme_x86: patchme.c
	gcc -m32 -o $@ $^

patchme_nostd: patchme_nostd.c
	gcc -nostdlib -o $@ $^

patchme_nostd_x86: patchme_nostd.c
	gcc -nostdlib -m32 -o $@ $^

imul_x64.bin: imul_x64.rasm
	rasm2 -Bf $^ -O $@

imul_x32.bin: imul_x32.rasm
	rasm2 -Bf $^ -O $@

rasm_example.bin: rasm_example.rasm
	rasm2 -Bf $^ -O $@

nasm_eff_addr.rasm.asm:
	rasm2 -f nasm_eff_addr.rasm | xargs rasm2 -D > nasm_eff_addr.rasm.asm

nasm_eff_addr:
	nasm -fbin nasm_eff_addr.asm

boot:
	nasm -f bin boot.asm # && qemu-system-x86_64 boot

clean:
	rm patchme patchme_x86 patchme_nostd patchme_nostd_x86 imul_x64.bin imul_x32.bin boot nasm_eff_addr.rasm.asm nasm_eff_addr


.PHONY: clean all
