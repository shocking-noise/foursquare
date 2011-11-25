# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "events"

class General(API):

    def details(self, event_id):
        """
        """
        return self._request("/".join([PATH, event_id]))

    def search(self, domain, id):
        """
        """
        params = {
            "domain": domain,
            "id": id
        }
        return self._request("/".join([PATH, "search"]), params=params)

    def categories(self):
        """
        """
        return self._request("/".join([PATH, "categories"]))
