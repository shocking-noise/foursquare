# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "photos"

class General(API):

    def detail(self, photo_id):
        """
        """
        return self._request("/".join([PATH, photo_id]), params=params)

    def add(self, checkin_id=None, tip_id=None, venue_id=None, broadcaset=None,
            public=None, ll=None, ll_arc=None, alt=None, alt_acc=None):
        """
        """
        params = {
            "checkinId": checkin_id,
            "tipId": tip_id,
            "venueId": venue_id,
            "broadcast": ','.join(broadcast)
            "public": public,
            "ll": ll,
            "llArc": ll_arc,
            "alt": alt,
            "altAcc": alt_acc
        }
        return self._request("/".join([PATH, "add"]), method="POST", params=params)

