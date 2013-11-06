#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

#   Copyright (C) 2013 by Xose Pérez
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Xose Pérez"
__contact__ = "xose.perez@gmail.com"
__copyright__ = "Copyright (C) 2013 Xose Pérez"
__license__ = 'GPL v3'

import requests
import json
import datetime
from CloudService import CloudService

class Xively(CloudService):
    """
    Xively.com client
    """

    api_key = ''
    timeout = 5

    datapoints = []
    base_url = "https://api.xively.com/v2/feeds/%s/datastreams/%s.json"
    base_url_feed = "https://api.xively.com/v2/feeds/%s"

    def __init__(self, api_key, timeout = None):
        """
        Constructor, provide API Key
        """
        self.api_key = api_key
        if timeout:
            self.timeout = timeout

    def headers(self):
        return {
            'X-ApiKey': self.api_key,
            'Content-type': 'application/json'
        }

    def push(self, feed, datastream, value):
        """
        Pushes a single value with current timestamp to the given feed/datastream
        """
        try:
            url = self.base_url % (feed, datastream)
            data = json.dumps({'current_value' : value})
            response = requests.put(url, data=data, headers=self.headers(), timeout=self.timeout)
            return response.status_code == 200
        except:
            return False

    def pushfeed(self, feed, value):
        """
        Pushes a stream to the given feed/datastream
        """
        try:
            url = self.base_url_feed % (feed)
            #data = json.dumps({'current_value' : value})
            response = requests.put(url, data=value, headers=self.headers(), timeout=self.timeout)
            return response.status_code == 200
        except:
            return False
