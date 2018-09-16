import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):
    def __init__(self, **kwargs):
        Gtk.Window.__init__(self, **kwargs)

win = MainWindow(title="Teste")

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

# Header Bar
hbar = Gtk.HeaderBar()
hbar.set_show_close_button(True)
hbar.props.title = "Header Bar"

# Setting the header bar
win.set_titlebar(hbar)

# Header bar items
button = Gtk.Button()
icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
button.add(image)
hbar.pack_end(button)

box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
Gtk.StyleContext.add_class(box.get_style_context(), "linked")

bt = Gtk.Button()
bt.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
box.add(bt)

mb = Gtk.MenuButton()
model = Gio.Menu()
model.append('New', 'app.new')
model.append('About', 'win.about')

submodel = Gio.Menu()
submodel.append('Quit', 'app.quit')

model.append_submenu("Other", submodel)

mb.set_menu_model(model)

hbar.pack_start(mb)
hbar.pack_start(box)

hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
hbox0.pack_start(Gtk.Label('Nome'), False, True, 5)
txtNome = Gtk.Entry()
hbox0.pack_start(txtNome, True, True, 5)
vbox.add(hbox0)

hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
hbox1.pack_start(Gtk.Label('Site'), False, True, 5)
txtSite = Gtk.Entry()
hbox1.pack_start(txtSite, True, True, 5)
vbox.add(hbox1)

hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
hbox2.pack_start(Gtk.Label('Usuario'), False, True, 5)
txtUsuario = Gtk.Entry()
hbox2.pack_start(txtUsuario, True, True, 5)
vbox.add(hbox2)

hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
hbox3.pack_start(Gtk.Label('Senha'), False, True, 5)
txtSenha = Gtk.Entry()
hbox3.pack_start(txtSenha, True, True, 5)
vbox.add(hbox3)

def on_button_clicked(widget):
    nome = txtNome.get_text()
    site = txtSite.get_text()
    usuario = txtUsuario.get_text()
    senha = txtSenha.get_text()
    print(nome, site, usuario, senha)

button = Gtk.Button(label="Salvar")
button.connect('clicked', on_button_clicked)
vbox.add(button)

win.add(vbox)
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()