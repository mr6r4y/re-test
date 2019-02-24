unsigned long a = 10;
unsigned long b = 20;

void main(void)
{
    __asm__ ("movq %1,%0" : "=mr"(b) : "rm"(a));
}