# -*- coding: utf-8 -*-

import urllib
import urllib2
import httplib2
import json


class NotYetImplException(Exception):
    pass

class API(object):

    API_BASE_URL = "https://api.foursquare.com/v2/"

    def __init__(self, oauth_token):
        self._oauth_token = oauth_token

    def _create_params(self,params):
        for k,v in params.items():
            if v is None:
                del params[k]
        params["oauth_token"] = self._oauth_token
        return params

    def _url_open(self, url, method, params):
        params = self._create_params(params)
        res = ""
        if method == "GET":
            fullurl = url + "?" + urllib.urlencode(params)
            print fullurl
            res = urllib2.urlopen(fullurl).read()
        elif method == "POST":
            res = urllib.urlopen(url,params).read()
        return res

    def _request(self, url, method="GET", params={}):
        return json.loads(self._url_open(self.API_BASE_URL + url, method, params))

    def _test(self):
        if "sort_type" in params.keys():
            params["sort"] = params["sort_type"]
            del params["sort_type"]
        if "zip_code" in params.keys():
            params["zip"] = params["zip_code"]
            del params["zip_code"]

