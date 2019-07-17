#!/usr/bin/env python3


import os
from ptpython.repl import embed
from cffi import FFI


def emb(globals, locals):
    conf_file = os.path.expanduser("~/.ptpython/config.py")
    if os.path.exists(conf_file):
        import importlib.util
        spec = importlib.util.spec_from_file_location("ptpython_conf", conf_file)
        ptpython_conf = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ptpython_conf)

    embed(globals, locals, configure=ptpython_conf.configure)


def compile_sysinfo():
    sysinfo_m = """
#include <sys/sysinfo.h>
"""

    sysinfo_h = """
struct sysinfo {
   long uptime;             /* Seconds since boot */
   unsigned long loads[3];  /* 1, 5, and 15 minute load averages */
   unsigned long totalram;  /* Total usable main memory size */
   unsigned long freeram;   /* Available memory size */
   unsigned long sharedram; /* Amount of shared memory */
   unsigned long bufferram; /* Memory used by buffers */
   unsigned long totalswap; /* Total swap space size */
   unsigned long freeswap;  /* Swap space still available */
   unsigned short procs;    /* Number of current processes */
   unsigned long totalhigh; /* Total high memory size */
   unsigned long freehigh;  /* Available high memory size */
   unsigned int mem_unit;   /* Memory unit size in bytes */
   %s
};

int sysinfo(struct sysinfo *info);
"""

    ffi = FFI()

    long_size = ffi.sizeof("long")
    int_size = ffi.sizeof("int")
    padding = 20 - 2*long_size - int_size
    if padding > 0:
        sysinfo_h = sysinfo_h % ("char _f[%i];" % padding)
    else:
        sysinfo_h = sysinfo_h % ""

    ffi.set_source("sysinfo", sysinfo_m)
    ffi.cdef(sysinfo_h)
    ffi.compile()


def main():
    compile_sysinfo()

    from sysinfo.lib import sysinfo
    from sysinfo import ffi

    info = ffi.new("struct sysinfo *")
    sysinfo(info)
    res = (info.mem_unit * (info.totalram >> 10) >> 10) + 0x20 & 0xffffffe0

    emb(globals(), locals())


if __name__ == '__main__':
    main()
