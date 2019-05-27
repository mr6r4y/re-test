
# -*- coding: utf-8 -*-
from __future__ import print_function

import frida


session = frida.attach("mate-calc")
script = session.create_script("""\
rpc.exports = {
  helloWorld: function () {
    return 'Hello';
  },
  failPlease: function () {
    oops;
  }
};
""")
script.load()
api = script.exports
print("api.hello() =>", api.hello_world())
# api.fail_please()