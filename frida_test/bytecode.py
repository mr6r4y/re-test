# -*- coding: utf-8 -*-
from __future__ import print_function

import frida


system_session = frida.attach(0)
bytecode = system_session.compile_script(name="bytecode-example", source="""\
rpc.exports = {
  listThreads: function () {
    return Process.enumerateThreadsSync();
  }
};
""")

session = frida.attach("mate-calc")
script = session.create_script_from_bytes(bytecode)
script.load()
api = script.exports
print("api.list_threads() =>", api.list_threads())