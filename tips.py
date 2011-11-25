
# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "tips"

class General(API):
    
    def detail(self, tip_id):
        """
        """
        return self._request("/".join([PATH, tip_id]))

    def add(self, venue_id, text, url=None, broadcast=None):
        """
        """
        params = {
            "venueId": venue_id,
            "text": text,
            "url": url,
            "braodcast": broadcast
        }
        return self._request("/".join([PATH, "add"]), method="POST", params=params)

    def search(self, ll, limit=None, offset=None, filtr=None, query=None):
        """
        """
        params = {
            "ll": ll,
            "limit": limit,
            "offset": offset,
            "filter": filtr,
            "query": query
        }
        return self._request("/".join([PATH,"search"]), params=params)

class Aspects(API):

    def lists(self, tip_id, group=None):
        """
        """
        params = {
            "group": group
        }
        return self._request("/".join([PATH, tip_id, "lists"]), parame=params)

class Actions(API):

    def marktodo(self, tip_id):
        """
        """
        return self._request("/".join([PATH, tip_id, "marktodo"]), method="POST")

    def markdone(self):
        """
        """
        return self._request("/".join([PATH, tip_id, "markdone"]), method="POST")

    def unmark(self):
        """
        """
        return self._request("/".join([PATH, tip_id, "unmark"]), method="POST")
