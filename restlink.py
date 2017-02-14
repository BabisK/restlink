# Copyright (c) 2017 Charalampos Kaidos.
#
# This file is part of Restlink.
#
# Restlink is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Restlink is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Restlink.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask
from flask_restful import Api

from common.setencoder import SetEncoder

from resources.interfaces import InterfaceList, Interface

app = Flask(__name__)
app.json_encoder = SetEncoder

api = Api(app)

api.add_resource(InterfaceList, '/interfaces')
api.add_resource(Interface, '/interfaces/<interface>')

if __name__ == '__main__':
    app.run()