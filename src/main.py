# main.py
#
# Copyright 2020 Francesco Garbin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# import sys
# import gi

# gi.require_version('Gtk', '3.0')

# from gi.repository import Gtk, Gio

# from .window import GtktoolbarWindow


# class Application(Gtk.Application):
#     def __init__(self):
#         super().__init__(application_id='org.example.App',
#                          flags=Gio.ApplicationFlags.FLAGS_NONE)

#     def do_activate(self):
#         win = self.props.active_window
#         if not win:
#             win = GtktoolbarWindow(application=self)
#         win.present()


# def main(version):
#     app = Application()
#     return app.run(sys.argv)

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
from .main_window import MainWindow

class GtkToolbarApp(Gtk.Application):

    def __init__(self):
         super().__init__(application_id='org.example.App',
                          flags=Gio.ApplicationFlags.FLAGS_NONE)
        #Gtk.Application.__init__(self)

    def do_activate(self):
        win = MainWindow(self)
        win.show()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        # add new action to app
        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.new_action_callback)
        #app.add_action(new_action)
        # add open action to app
        open_action = Gio.SimpleAction.new("open", None)
        open_action.connect("activate", self.open_action_callback)
        #app.add_action(open_action)

    def new_action_callback(self, action, parameter):
        print("You clicked \"New\".")

    def open_action_callback(self, action, parameter):
        print("You clicked \"Open\".")


def main(version):
    app = GtkToolbarApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)

