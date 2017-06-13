all: patchme patchme_x86 patchme_nostd patchme_nostd_x86 imul_x64.bin imul_x32.bin

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

clean:
	rm patchme patchme_x86 patchme_nostd patchme_nostd_x86 imul_x64.bin imul_x32.bin


.PHONY: clean all
