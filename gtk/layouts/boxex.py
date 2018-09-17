import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        box2 = Gtk.Box(spacing=20)
        self.add(self.box)
        self.box.pack_end(box2, True, True, 0)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect('clicked', self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label='Goodbye')
        self.button2.connect('clicked', self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        box2.pack_start(Gtk.Button(label="teste 1"), True, True, 10)
        box2.pack_end(Gtk.Button(label="teste 2"), True, True, 10)

    def on_button1_clicked(self, widget):
        print('Hello')

    def on_button2_clicked(self, widget):
        print('Goodbye')

win = MyWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
