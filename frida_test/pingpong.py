from __future__ import print_function
import frida
import sys

session = frida.attach("hello")
script = session.create_script("""
    recv('poke', function onMessage(pokeMessage) { send('pokeBack'); });
""")
def on_message(message, data):
    print(message)
script.on('message', on_message)
script.load()
script.post({"type": "poke"})
sys.stdin.read()