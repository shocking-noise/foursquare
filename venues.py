# -*- coding: utf-8 -*-

from api import API
from api import NotYetImplException

PATH = "veneus"

class General(API):

    def detail(self, venue_id):
        """
        """
        return _request('/'.join([PATH, venue_id]))

    def add(self,name, ll, address=None, cross_street=None, city=None, state=None,
            zip_code=None, phone=None, twitter=None, primary_category_id=None,
            description=None, url=url):
        """
        """
        params = {
            "name": name,
            "ll": ll,
            "address": address,
            "crossStreet": cross_street,
            "city": city,
            "state": state,
            "zip": zip_code,
            "phone": phone,
            "twitter": twitter,
            "primaryCategoryId": primary_category_id,
            "description", description,
            "url": url
        }
        return _request(PATH, method="POST", params=params)

    def categorys(self):
        """
        """
        return _request('/'.join([PATH, "categorys"]))

    def explore(self, ll, ll_arc=None, alt=None, radius=None, section=None,
            query=None, limit=None, intent=None, novelty=None):
        """
        """
        params = {
            "ll": ll,
            "llArc": ll_arc,
            "alt": alt,
            "radius": radius,
            "section": section,
            "query": query,
            "limitl": limit,
            "intent": intent,
            "novelty": novelty
        }
        return _request('/'.join([PATH, "explore"]), params=params)

    def search(self, ll, ll_arc=None, alt=alt, alt_acc=None, query=None,
            limit=None, intent=None, radius=None, sw=None, ne=None,
            category_id=None, url=None, provider_id=None, link_id=None):
        """
        """
        params = {
            "ll": ll,
            "llArc": ll_arc,
            "alt": alt,
            "altAcc": altAcc:
            "query": query,
            "limit": limit,
            "intent": intent,
            "radius": radius,
            "sw": sw,
            "ne": ne,
            "categoryId": category_id,
            "url": url,
            "providerId": provider,
            "linkId": link_id
        }
        return _request('/'.join([PATH, "search"]), params=params)

    def suggestcompletion(self, ll, query, ll_arc=None, alt=None, limit=None):
        """
        """
        params = {
            "ll": ll,
            "query": query,
            "llArc": ll_arc,
            "alt": alt,
            "limit": limit
        }
        return _request('/'.join([PATH, "suggestcompletion"]), params=params)

    def trending(self, ll, limit=None, radius=None):
        """
        """
        params = {
            "ll": ll,
            "limit": limit,
            "radius": radius
        }
        return _request('/'.join([PAHT, "trending"]), params=params)


class Aspects(API):

    sort_types = {"recent", "popular"}
    group_list = {"checkin", "venue"}
    listed_group = {"created", "edited", "followed", "friends", "othter"}

    def herenow(self, venue_id, limit=None, offset=None, after_timestamp=None):
        """
        """
        params = {
            "limit": limit,
            "offset": offset,
            "afterTimestamp": after_timestamp
        }
        return _request('/'.join([PATH, venue_id, "horenow"]), params=params)

    def tips(self, venue_id, sort_type=None, limit=None, offset=None):
        """
        """
        if sort_type:
            if sort_type not in sort_types:
                raise ValueError("sort type value must be recent/popular")
        params = {
            "limit": limit,
            "offset": offset,
            "sort": sort_type
        }
        return _request('/'.join([PATH, "tips", venue_id], params=params)

    def photos(self, venue_id, group, limit=None, offset=None):
        """
        """
        if group not in group_list:
            raise ValueError("group value must be checkin/venue")
        prams = {
            "group": group,
            "limit": limit,
            "offset": offset
        }
        return _request('/'.join([PATH, "photos", venue_id]), params=params)

    def links(self):
        """
        """
        return _request('/'.join([PATH, venue_id, "links"]))

    def listed(self, group=group):
        """
        """
        if group:
            if group not in listed_group:
                raise ValueError("group value must be " +
                    '/'.join(listed_group))
        params = {
            "group": group
        }
        return _request('/'.join([PATH, venue_id, "listed"], params=params)

    def similar(self):
        """
        """
        return _request('/'.join([PATH, venue_id, "similar"]))

    def events(self):
        """
        """
        return _request('/'.join([PATH, venue_id, "events"])


class Actions(API):

    problem_list = {"mislocated", "closed", "duplicate", "inappropriate",
        "doesnt_exist", "event_over"}

    def marktodo(self, venue_id, text=text):
        """
        """
        params = {
            "text": text
        }
        return _request('/'.join([PATH, venue_id, "marktodo"]), method="POST",
            params=params)

    def flag(self, venue_id, problem, dup_venue_id=None):
        """
        """
        if not problem:
            raise ValueError("problem must be " + '/'.join(problem))
        if problem == "duplicate":
            if not dup_venue_id:
                raise ValueError("dup_venue_id must. when problem is duplicate.")
        params = {
            "problem": problem
            "venueId": venue_id
        }
        return _request('/'.join([PATH], venue_id, "flag"]), method="POST",
            params=params)

    def edit(self, venue_id, name=None, address=None, cross_street=None,
        city=None, state=None, zip_code=None, phone=None, ll=None,
        category_id=None, twitter=None, description=None, url=None):
        """
        """
        params = {
            "address": address,
            "crossStreet": cross_street,
            "city": city,
            "state": state,
            "zip": zip_code,
            "phone": phone,
            "ll": ll,
            "categoryId": category_id,
            "twitter": twitter,
            "description": description,
            "url": url
        }
        return _request('/'.join([PATH, venue_id, "edit"]), method="POST",
            params=params)

    def proposeedit(self, venue_id, name=None, address=None, cross_street=None,
            city=None, state=None, zip_code=None, phone=None, ll=None,
            primary_category_id = None):
        """
        """
        params = {
            "name": name,
            "address": address,
            "crossStreet": cross_street,
            "city": city,
            "state": state,
            "zip": zip_code,
            "phone": phone,
            "ll": ll,
            "primaryCategoryId": primary_category_id
        }
        return _request('/'.join([PATH, venue_id, "proposeedit"]), params=params)
