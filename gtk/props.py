import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect('destroy', Gtk.main_quit)

label = Gtk.Label(label="test", angle=25, halign=Gtk.Align.END)
win.add(label)

win.show_all()
Gtk.main()
