#!/usr/bin/python
import requests
import json
import re
'''
An REST API interface.
It supports the following functions
    1. set up a list of API urls,                       : addAPI_URL
    2. get data in JSON format from the API urls        : getDataAsJSON
'''


class exoREST:

    def __init__(self):
        self.url_list = {}

    def addAPI_URL(self, url_name, url):
        url_format = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"

        if url == '':
            raise Exception('URL is null')
        if bool(re.match(url_format, url)) is False:
            raise Exception('URL format isn\'t matching')
        if url in self.url_list.values():
            raise Warning('URL already exists')
        if url_name == '':
            raise Exception('URL name can not be null')
        elif url_name in self.url_list.keys():
            raise Exception('URL name already exists')
        else:
            self.url_list[url_name] = url

    def getURL_LIST(self):
        return self.url_list

    def getDataFromAPI(self, url_name):
        if url_name not in self.url_list.keys():
            raise Exception('{} is not a valid urlname'.format(url_name))
        url = self.url_list[url_name]
        parsed = {}
        response = requests.get(url)
        # return response
        data = response.text
        # return data
        parsed = json.loads(data)
        return parsed


class exoJSON:
    @staticmethod
    def JSONParser(jsonVar, param=''):
        _tempJson = jsonVar
        if param == '':
            return jsonVar
        if jsonVar == {}:
            raise Warning("Empty JSON")
        else:
            paramList = param.split('/')
            for p in paramList:
                if p not in list(_tempJson.keys()):
                    raise Exception(
                        "invalid json parameter: {}. Available parameters: {}".format(
                            p, _tempJson.keys()))
                _tempJson = _tempJson[p]
        return _tempJson

    @staticmethod
    def JSONStructure(jsonVar, KEY=''):
        '''
         KEY == '' returns entire structure
         KEY == '__ROOT__' returns only root keys
         if KEY == key, returns the sub-keys under a particular key
        '''
        stack = list(jsonVar.keys())
        result = list(jsonVar.keys())
        if KEY == '__ROOT__':
            return result
        elif KEY != '':
            stack = [KEY]
            result = [KEY]
        _json = jsonVar
        while stack:
            top_element = stack.pop()
            _json = _json[top_element]
            try:
                list_of_keys = list(_json.keys())
                # print(list_of_keys)
                for key in list_of_keys:
                    # print(top_element, end = "-->")
                    # print(key)
                    stack.append(key)
                    result.append(top_element + '/' + key)
            except BaseException:
                return result
