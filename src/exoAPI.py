#!/usr/bin/python
import urllib.request
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
        if bool(re.match(url_format, url)) == False:
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
            raise Exception(f'{url_name} is not a valid urlname')
        url = self.url_list[url_name]
        parsed = {}
        response = requests.get(url)
        # return response
        data = response.text
        # return data
        parsed = json.loads(data)
        return parsed
            
    def JSONParser(self, jsonVar, param):
        if jsonVar == {}:
            raise Warning("Empty JSON")
        else:
            if param not in list(jsonVar.keys() ):
                raise Exception("invalid json parameter")
        
        return jsonVar[param]
    
    def JSONStructure(self, jsonVar, KEY = ''):
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
            except:
                return result
    # --------------------------------------------
    # Under developement
    # def JSONTraverser(indict, pre=None):
        # pre = pre[:] if pre else []
        # if isinstance(indict, dict):
            # for key, value in indict.items():
                # if isinstance(value, dict):
                    # for d in dict_generator(value, pre + [key]):
                        # yield d
                # elif isinstance(value, list) or isinstance(value, tuple):
                    # for v in value:
                        # for d in dict_generator(v, pre + [key]):
                            # yield d
                # else:
                    # yield pre + [key, value]
        # else:
            # yield pre + [indict]
        
    # def getDataFromJSON(self, JSONdict, parameters):
        # '''
            # parameters: JSON data parameters, which will be
                        # used to access JSON data 
                # type: LIST
                # format:
                    # param1/param2,
                        # where param1 is upper hierarchy
                              # param2 is lower hierarchy
                              
                # CAUTION: ONLY hierarchy upto level 2 is supported
        # '''
        # data = []
        # for p in parameters:
            # _p0 = (p.split('/'))[0]
            # try:
                # _p1 = (p.split('/'))[1]
                # data.append(JSONdict[_p0][_p1])
            # except:
                # data.append(JSONdict[_p0])
        # return data
    # --------------------------------------------