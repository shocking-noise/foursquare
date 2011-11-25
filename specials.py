# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "specials"

class General(API):

    def detail(self, special_id, venue_id):
        """
        """
        params = {
            "venueId": venue_id
        }
        return self._request("/".join([PATH, ""]), params=params)

    def search(self, ll, ll_arc=None, alt=None, alt_acc=None, limit=None):
        """
        """
        params = {
            "ll": ll,
            "llAcc": ll_arc,
            "alt": alt,
            "altAcc": alt_acc,
            "limit": limit
        }
        return self._request("/".join([PATH, ""]), params=params)


class Actions(API):

    problem_types = {"not_redeemable", "not_valuable", "other"}

    def flag(self, id, venue_id, problem, text=None):
        """
        """
        if not problem in problem_list:
            raise ValueError("problem must be " + '/'.join(problem_types))
        params = {
            "venueId": venue_id,
            "problem": problem,
            "text": text
        }
        return self._request("/".join([PATH, id, "flag"]), method="POST", params=params)
