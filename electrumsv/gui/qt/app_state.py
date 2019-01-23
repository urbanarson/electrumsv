# Electrum SV - lightweight Bitcoin SV client
# Copyright (C) 2019 The Electrum SV Developers
# Copyright (C) 2012 thomasv@gitorious
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''QT application state.'''

import sys

from electrumsv.app_state import AppStateProxy

from .app import SVApplication


class QtAppStateProxy(AppStateProxy):

    def __init__(self, *args):
        super().__init__(*args)

        self.app = SVApplication(sys.argv)
        # A floating point number, e.g. 129.1
        self.dpi = self.app.primaryScreen().physicalDotsPerInch()

    def alias_resolved(self):
        self.app.alias_resolved.emit()

    def set_base_unit(self, base_unit):
        if super().set_base_unit(base_unit):
            self.app.base_unit_changed.emit()
