all: empty_main empty_main_pic empty_main_gdb init_array hook start_nostdlib t.bin hook_pic hook_pic_x86 hook_x86 scan_x86 scan strcpy_crash strcpy_crash_x86 callee_params callee_params_x86 ret_val ret_val_x86 goto1 goto1_x86 condjmp condjmp_x86 loop1 loop1_x86 memcp memcp_x86 switch1 switch1_x86 switch2 switch2_x86 switch3 switch3_x86 is_whitespace is_whitespace_x86

empty_main: empty_main.c
	gcc -o $@ $^

empty_main_pic: empty_main.c
	gcc -fPIC -o $@ $^

empty_main_gdb: empty_main.c
	gcc -ggdb -o $@ $^

init_array: init_array.c
	gcc -o $@ $^

hook: hook.c
	gcc -o $@ $^

hook_pic: hook.c
	gcc -fPIC -o $@ $^

hook_pic_x86: hook.c
	gcc -m32 -fPIC -o $@ $^

hook_x86: hook.c
	gcc -m32 -o $@ $^

start_nostdlib: start_nostdlib.c
	gcc -nostdlib -o $@ $^
	strip $@

scan_x86: scan.c
	gcc -m32 -o $@ $^

scan: scan.c
	gcc -o $@ $^

strcpy_crash_x86: strcpy_crash.c
	gcc -m32 -o $@ $^

strcpy_crash: strcpy_crash.c
	gcc -o $@ $^

t.bin: t.rasm
	rasm2 -Bf t.rasm -O t.bin

callee_params: callee_params.c
	gcc -o $@ $^

callee_params_x86: callee_params.c
	gcc -m32 -o $@ $^

ret_val_x86: ret_val.c
	gcc -m32 -o $@ $^

ret_val: ret_val.c
	gcc -o $@ $^

goto1: goto1.c
	gcc -o $@ $^

goto1_x86: goto1.c
	gcc -m32 -o $@ $^

condjmp: condjmp.c
	gcc -o $@ $^

condjmp_x86: condjmp.c
	gcc -m32 -o $@ $^

loop1: loop1.c
	gcc -o $@ $^

loop1_x86: loop1.c
	gcc -m32 -o $@ $^

memcp: memcp.c
	gcc -o $@ $^

memcp_x86: memcp.c
	gcc -m32 -o $@ $^

switch1: switch1.c
	gcc -o $@ $^

switch1_x86: switch1.c
	gcc -o $@ $^

switch2: switch2.c
	gcc -o $@ $^

switch2_x86: switch2.c
	gcc -o $@ $^

switch3: switch3.c
	gcc -o $@ $^

switch3_x86: switch3.c
	gcc -o $@ $^

is_whitespace: is_whitespace.c
	gcc -o $@ $^

is_whitespace_x86: is_whitespace.c
	gcc -o $@ $^

clean:
	rm empty_main empty_main_pic empty_main_gdb init_array hook start_nostdlib t.bin hook_pic hook_pic_x86 hook_x86 scan_x86 scan strcpy_crash strcpy_crash_x86 callee_params callee_params_x86 ret_val ret_val_x86 goto1 goto1_x86 condjmp condjmp_x86 loop1 loop1_x86 memcp memcp_x86 switch1 switch1_x86 switch2 switch2_x86 switch3 switch3_x86 is_whitespace is_whitespace_x86


.PHONY: clean all
