# `fs1` and `fs2`

By this trick I can pass the result from the script to the first argument of `fs2` under gdb:

     gdb --args ./fs2 "$(python ./fs2_pld.py)"

Then in gdb I only `run` the debugee. `show args` can print the passed string.

GDB:
    
    break *(fs+24); run

# `fs2`

    fs3 "aaaaaaaa %llx %llx %llx %llx %llx %llx %llx %llx %llx %llx"
