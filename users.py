# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "users"
DEFAULT_USER = "self"

class General(API):

    def user(self, user_id=DEFAULT_USER):
        """
        Returns profile information for a given user, including selected badges
        and mayorships. 
        """
        return self._request('/'.join([PATH,user_id]))

    def leaderboard(self, neighbors=None):
        """
        Leaderboard by User.
        Returns the user's leaderboard.
        """
        params = {
            "neighbors": neighbors
        }
        return self._request('/'.join([PATH,"leaderboard"]), params=params)

    def search(self, phone=None, email=None, twitter=None, twitter_source=None,
            fbid=None, name=None):
        """
        Find users.
        Helps a user locate friends.
        """
        params = {
            "twitterSource": twitter_source,
            "name": name
        }
        if phone:
            params["phone"] = ",".join(phone)
        if email:
            params["email"] = ",".join(email)
        if twitter:
            params["twitter"] = ','.join(twitter)
        if fbid:
            params["fbid"] = ','.join(fbid)
        return self._request('/'.join([PATH, "search"]), params=params)

    def requests(self):
        """
        Pending friend requests.
        Shows a user the list of users with whom they have a pending friend
        request.
        """
        return self._request('/'.join([PATH, "requests"]))


class Aspects(API):

    group_list = {"created", "edited", "followed", "friends", "suggested"}
    sort_types = {"recent", "nearby", "popular"}

    def badge(self, user_id=DEFAULT_USER):
        """
        Returns badges for a given user.
        """
        return self._request('/'.join([PATH, user_id, "batch"]))

    def checkin(self, limit=None, offset=None,
            after_timestamp=None, before_timestamp=None):
        """
        Checkins by a user.
        Returns a history of checkins for the authenticated user. 
        """
        params = {
            "limit": limit,
            "offset": offset,
            "afterTimestamp": after_timestamp,
            "beforeTimestamp": before_timestamp
        }
        return self._request('/'.join([PATH, DEFAULT_USER, "checkins"]),
            params=params)

    def friends(self, user_id=DEFAULT_USER):
        """
        List friends.
        Returns an array of a user's friends.
        """
        return self._request('/'.join([PATH, user_id, "friends"]))

    def lists(self, user_id, group=None, ll=None):
        """
        Lists
        A User's Lists.
        """
        if group:
            if group not in group_list:
                raise ValueError("group value must be" +
                        "created/edited/followed/friends/suggested")
            if group == "suggested":
                raise ValueError("suggested needs ll(LatLong) parameter.")
        params = {
            "group": group,
            "ll": ll
        }
        return self._reqesut('/'.join([PATH, user_id, "lists"]), params=params)

    def mayorships(self, user_id=DEFAULT_USER):
        """
        List mayorships.
        Returns a user's mayorships.
        """
        return self._request('/'.join([PATH, user_id, "mayorships"]))

    def tips(self, user_id=DEFAULT_USER, sort_type=None, ll=None):
        """
        Tips from a User.
        Returns tips from a user.
        """
        if sort_type: 
            if sort_type not in self.sort_types:
                raise ValueError("sort type value must be recent/nearby,popular")
            if sort_type == "nearby" and not ll:
                raise ValueError("sort nearby needs ll(LatLong) parameter.")
        params = {
            "sort": sort_type,
            "ll": ll
        }
        return self._request('/'.join([PATH, user_id, "tips"]), params=params)

    def todo(self, user_id=DEFAULT_USER, sort_type=None, ll=None):
        """
        Todos from a User.
        Returns todos from a user.
        """
        if sort_type: 
            if sort_type not in self.sort_types:
                raise ValueError("sort type value must be recent/nearby,popular")
            if sort_type == "nearby" and not ll:
                raise ValueError("sort nearby needs ll(LatLong) parameter.")
        params = {
            "sort": sort_type,
            "ll": ll
        }
        return self._request('/'.join([PATH, user_id, "friends"]),
                params=params)

    def photos(self, user_id=DEFAULT_USER, limit=None, offset=None):
        """
        Photos from a User.
        Returns photos from a user.
        """
        params = {
            "limit": limit,
            "offset": offset
        }
        return self._request('/'.join([PATH, user_id, "photos"]), params=params)

    def venuehistory(self):
        """
        Venues visited by a user.
        Returns a list of all venues visited by the specified user, along with
        how many visits and when they were last there.
        """
        return self._request('/'.join([PATH, DEFAULT_USER, "venuehistory"]))


class Actions(API):

    def request(self, user_id):
        """
        Send a Friend Request.
        Sends a friend request to another user.
        """
        return self._request('/'.join([PATH, user_id, "request"]), method="POST")

    def unfriend(self, user_id):
        """
        Remove a Friend.
        Cancels any relationship between the acting user and the specified user.
        """
        return self._request('/'.join([PATH, user_id, "unfriend"]), method="POST")

    def approve(self, user_id):
        """
        Approve a friend request.
        Approves a pending friend request from another user.
        """
        return self._request('/'.join([PATH, user_id, "approve"]), method="POST")

    def deny(self, user_id):
        """
        Deny a friend request.
        Denies a pending friend request from another user.
        """
        return self._request('/'.join([PATH, user_id, "deny"]), method="POST")

    def setpings(self, user_id, value=False):
        """
        Set whether to receive pings about a user.
        Changes whether the acting user will receive pings (phone notifications)
        when the specified user checks in.
        """
        v = "true" if value else "false"
        params = {
            "value": v
        }
        return self._request('/'.join([PATH, user, "setpings"]), method="POST",
                params=params)

    def update(self, photo):
        """
        Update user's photo.
        Updates the user's profile photo.
        """
        #TODO
        raise NotYetImplException()
        params = {
            "photo": photo
        }
        return self._requset('/'.join([PATH, DEFAULT_USER, "update"]),
            method="POST", params=params)
