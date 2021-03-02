# window.py
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

# from gi.repository import Gtk


# @Gtk.Template(resource_path='/org/example/App/window.ui')
# class GtktoolbarWindow(Gtk.ApplicationWindow):
#     __gtype_name__ = 'GtktoolbarWindow'

#     label = Gtk.Template.Child()

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio

class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Gtk Toolbar", application=app)
        self.set_default_size(400, 200)

        # a grid to attach the toolbar (see below)
        grid = Gtk.Grid()
        self.add(grid)

        # we have to show the grid (and therefore the toolbar) with show(),
        # as show_all() would show also the buttons in the toolbar that we want to
        # be hidden (such as the leave_fullscreen button)
        grid.show()

        # a builder to add the UI designed with Glade to the grid:
        builder = Gtk.Builder()

        # get the file (if it is there)
        try:
            #builder.add_from_file("toolbar_builder.ui")
            builder.add_from_resource("/org/example/App/toolbar_builder.ui")
        except:
            print("file toolbar_builder.ui not found")
            sys.exit(8)

        # attach the builder toolbar to the grid
        grid.attach(builder.get_object("toolbar"), 0, 0, 1, 1)

        # two buttons that will be used later in a method
        self.fullscreen_button = builder.get_object("fullscreen_button")
        self.leave_fullscreen_button = builder.get_object("leave_fullscreen_button")

        # create the actions that control the window, connect their signal to a
        # callback method (see below), add the action to the window:

        # undo
        undo_action = Gio.SimpleAction.new("undo", None)
        undo_action.connect("activate", self.undo_callback)
        self.add_action(undo_action)

        # and fullscreen
        fullscreen_action = Gio.SimpleAction.new("fullscreen", None)
        fullscreen_action.connect("activate", self.fullscreen_callback)
        self.add_action(fullscreen_action)

    # callback for undo
    def undo_callback(self, action, parameter):
        print("You clicked \"Undo\".")

    # callback for fullscreen
    def fullscreen_callback(self, action, parameter):
        # check if the state is the same as Gdk.WindowState.FULLSCREEN which is a bit flag
        is_fullscreen = self.get_window().get_state() & Gdk.WindowState.FULLSCREEN != 0
        if is_fullscreen:
            self.unfullscreen()
            self.leave_fullscreen_button.hide()
            self.fullscreen_button.show()
        else:
            self.fullscreen()
            self.fullscreen_button.hide()
            self.leave_fullscreen_button.show()

