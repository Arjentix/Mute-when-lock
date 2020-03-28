'''
All rights reserved, Polyakov Daniil, 2020
'''

import sys
import os
import subprocess 
import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

get_current_output_cmd = (
    "pacmd list-cards | sed -n 's/^.*active profile: <\\(\\S*\\)>$/\\1/p'")
get_outputs_cmd = "pacmd list-cards | sed -n 's/^.*\\(output:\\S*\\):.*$/\\1/p'"

outputs = []

def signal_handler(*args, **kwargs):
  global outputs
  print(outputs)

  command = 'mute'
  # If unlocked
  if bool(args[0]) == False:
    command = 'unmute'

  current_output = None
  # If no argument was provided
  if (len(outputs) == 0):
    current_output = os.popen(get_current_output_cmd).read()
    outputs = os.popen(get_outputs_cmd).read().splitlines()

  for output in outputs[::-1]:
    subprocess.call(['pacmd', 'set-card-profile', '0', output])
    subprocess.call(['amixer', 'set', 'Master', command])
  
  if current_output != None:
    subprocess.call(['pacmd', 'set-card-profile', '0', current_output])

if __name__ == '__main__':
  if len(sys.argv) > 1:
    outputs = sys.argv[1:]

  DBusGMainLoop(set_as_default=True)

  session_bus = dbus.SessionBus()

  # Lock/Unlock event
  session_bus.add_signal_receiver(
      handler_function=signal_handler,
      path='/org/gnome/ScreenSaver',
      dbus_interface='org.gnome.ScreenSaver',
      interface_keyword='dbus_interface',
      member_keyword='member')

  mainloop = GLib.MainLoop()
  mainloop.run()
