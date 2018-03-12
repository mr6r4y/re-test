# Exploiting Format-string Bugs

## Plan

1. Make simple shellcode with fixed position of the format string on the stack - `fs3`
1. Make execution of `never_called` in `fs2` (probably with .dtors-rewrite)
1. Make shellcode execution in `fs1`

## Some Notes

By this trick I can pass the result from the script to the first argument of `fs2` under gdb:

     gdb --args ./fs2 "$(python ./fs2_pld.py)"

Then in gdb I only `run` the debugee. `show args` can print the passed string.

GDB:

    break *(fs+24); run

The last argument dumps the `6161..` beginning of the format string:

    fs3 "aaaaaaaa %llx %llx %llx %llx %llx %llx %llx %llx %llx %llx"


## References

* [Reference in .dtors rewrite article for source in GCC for constructors/destructors](https://github.com/gcc-mirror/gcc/blob/master/gcc/collect2.c)