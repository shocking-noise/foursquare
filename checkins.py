# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "checkins"

class General(API):

    def details(self, checkin_id):
        """
        """
        return self._request("/".join([PATH, checkin_id]))

    def add(self, venue_id=None, venue=None, event_id=None, shout=None, 
            broadcast=None, ll=None, ll_arc=None, alt=None, alt_acc=None):
        """
        """
        params = {
            "venue": venue,
            "eventId": event_id,
            "shout": shout,
            "broadcast": ','.join(broadcast),
            "ll": ll,
            "llArc": ll_arc,
            "alt": alt,
            "altAcc": alt_acc
        }
        return self._request('/'.join([PATH, "add"]), method="POST",
                params=params)

    def recent(self, ll=None, limit=None, after_timestamp=None):
        """
        """
        params = {
            "ll": ll,
            "limit": limit,
            "afterTimestamp": after_timestamp
        }
        return self._request('/'.join([PATH, "recent"]), params=params)


class Actions(API):

    def addcomment(self, checkin_id, text=None):
        """
        """
        params ={
            "text": text
        }
        return self._request('/'.join([PATH, checkin_id, "addcoment"]), method="POST",
                params=params)

    def deletecomment(self, checkin_id, comment_id=None):
        """
        """
        params ={
            "commentId": comment_id
        }
        return self._request('/'.join([PATH, checkin_id, "deletecomment"]),
                method="POST", params=param)
