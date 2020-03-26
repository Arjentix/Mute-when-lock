'''
All rights reserved, Polyakov Daniil, 2020
'''

import subprocess 
import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

def signal_handler(*args, **kwargs):
  subprocess.call(['amixer', 'set', 'Master', 'toggle'])


if __name__ == '__main__':
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

