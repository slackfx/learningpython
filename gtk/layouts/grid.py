import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Grid Example')

        grid = Gtk.Grid()
        self.add(grid)

        buttons = [Gtk.Button(label="Button {}".format(i)) for i in range(1, 7)]

        grid.add(buttons[0])
        grid.attach(buttons[1], 1, 0, 2, 1)
        grid.attach_next_to(buttons[2], buttons[0], Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(buttons[3], buttons[2], Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(buttons[4], 1, 2, 1, 1)
        grid.attach_next_to(buttons[5], buttons[4], Gtk.PositionType.RIGHT, 1, 1)

win = GridWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
