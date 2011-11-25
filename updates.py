# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "update"

class General(API):

    def detail(self, update_id):
        """
        """
        return self._request("/".join([PATH, update_id]))

    def notification(self, limit=None):
        """
        """
        params = {
            "limit": limit
        }
        return self._request("/".join([PATH, "notification"]), params=params)


class Actions(API):

    def marknotificationsread(self, high_watermark):
        """
        """
        params = {
            "highWatermark": high_watermark
        }
        return self._request("/".join([PATH, "marknotificationsread"]),
                method="POST" params=params)
