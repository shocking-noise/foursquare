# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "settings"

class General(API):

    def detail(self, setting_id):
        """
        """
        return self._request("/".join([PATH, setting_id]))

    def all(self):
        """
        """
        return self._request("/".join([PATH, "all"]))


class Actions(API):

    def set(self, setting_id, value):
        """
        """
        params = {
            "value": value
        }
        return self._request("/".join([PATH, setting_id, "set"]), method="POST", params=params)
