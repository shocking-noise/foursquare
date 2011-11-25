# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "lists"

class General(API):

    def detail(self, list_id, limit=None, offset=None):
        """
        """
        params = {
            "limit": limit,
            "offset": offset
        }
        return self._request("/".join([PATH, list_id]), params=params)

    def add(self, description=None, collaborative=None, photo_id=None):
        """
        """
        params = {
            "description": description,
            "collaborative": collaborative,
            "photoId": photo_id
        }
        return self._request("/".join([PATH, "add"]),method="POST", params=params)

class Aspects(API):

    def followers(self, list_id):
        """
        """
        return self._request("/".join([PATH, list_id, "followers"]))

    def suggestvenues(self, list_id):
        """
        """
        return self._request("/".join([PATH, list_id, "suggestvenues"]))

    def suggestphoto(self, list_id, item_id):
        """
        """
        params = {
            "itemId": item_id
        }
        return self._request("/".join([PATH, list_id, "suggestphoto"]), params=params)

    def suggesttip(self, list_id, item_id):
        """
        """
        params = {
            "itemId": item_id
        }
        return self._request("/".join([PATH, list_id, "suggesttip"]), params=params)

class Actions(API):

    def update(self, list_id, name=None, description=None, collaborative=None,
            photo_id=None):
        """
        """
        params = {
            "name": name,
            "description": description,
            "collaborative": collaborative,
            "photoId": photo_id
        }
        return self._request("/".join([PATH, list_id, "update"]), method="POST", params=params)

    def follow(self, list_id):
        """
        """
        return self._request("/".join([PATH, list_id, "follow"]), method="POST")

    def unfollow(self, list_id):
        """
        """
        return self._request("/".join([PATH, list_id, "unfollow"]), method="POST")

    def additem(self, list_id, venue_id=None, text=None, url=None, tip_id=None,
            list_id=None, item_id=None):
        """
        """
        params = {
            "venueId": venue_id,
            "text": text,
            "url": url,
            "tipId": tip_id,
            "listId": list_id,
            "itemId": item_id
        }
        return self._request("/".join([PATH, list_id, "additem"]), method="POST", params=params)

    def deleteitem(self, list_id, item_id):
        """
        """
        params = {
            "itemId": item_id
        }
        return self._request("/".join([PATH, list_id,"deleteitem"]),
                method="POST", params=params)

    def moveitem(self, item_id, item_id=None, before_id=None, after_id=None):
        """
        """
        params = {
            "itemId": item_id,
            "beforeId": before_id,
            "afterId": after_id
        }
        return self._request("/".join([PATH, list_id, "moveitem"]), method="POST", params=params)

    def updateitem(self, list_id, item_id, tip_id=None, text=None, url=None,
            photo_id=None):
        """
        """
        params = {
            "itemId": item_id,
            "tipId": tip_id,
            "text": text,
            "url": url,
            "photoId": photo_id
        }
        return self._request("/".join([PATH, item_id, "updateitem"]),
                method="POST", params=params)

    def share(self, list_id, broardcast=None, message=None):
        """
        """
        params = {
            "broadcast": ','.join(broadcast),
            "message": message
        }
        return self._request("/".join([PATH, list_id,"share"]), method="POST", params=params)
