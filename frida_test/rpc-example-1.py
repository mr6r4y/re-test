# -*- coding: utf-8 -*-
from __future__ import print_function

import frida
import base64


session = frida.attach("mate-calc")
script = session.create_script("""\
rpc.exports = {
  hello: function (a) {
    console.log(a);
    var p_a = Memory.alloc(a.length);
    Memory.writeByteArray(p_a, a)
    
    return p_a.readByteArray(a.length);
  }
};
""")
script.load()
api = script.exports

a = b'aaaaa\x00\x01\x03\x04bbbbb'
c = list(a)

print("api.hello() =>", api.hello(c))
