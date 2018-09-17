import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window(title='Grid 2')

def get_grid():
    grid = Gtk.Grid()

    grid.attach(Gtk.Button(label='Button 1x1'), 0, 0, 1, 1)
    grid.attach(Gtk.Button(label='Button 1x2'), 0, 1, 1, 1)
    grid.attach(Gtk.Button(label='Button 1x3'), 0, 2, 1, 1)

    grid.attach(Gtk.Button(label='Button 2x1'), 1, 0, 1, 1)
    grid.attach(Gtk.Button(label='Button 2x2'), 1, 1, 1, 1)
    grid.attach(Gtk.Button(label='Button 2x3'), 1, 2, 1, 1)

    return grid

box = Gtk.Box()
box.pack_start(get_grid(), True, True, 0)
box.pack_end(get_grid(), True, True, 20)

win.add(box)
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
