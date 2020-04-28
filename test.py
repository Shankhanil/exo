import unittest
from src.exoAPI import exoREST


class TestAPI(unittest.TestCase):
    def test_addAPI_URL(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : addAPI_URL(self, url_name, url)
        
    # Test for URL_list
        # url_list must be a an empty dict initially
        self.assertEqual(api.url_list, {}, 'Initial url list must be empty')
        
     # Test for URL name
        # Try to add 'abc' url. It should successfully add
        self.assertEqual(api.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees'), None, 'Function should return nothing on success.\
        Exception on failure')
        
        #Null URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertTrue('null URL name' in context.exception)
        
        #duplicate URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('abc', 'google.com')
        self.assertTrue('Duplicate URL name' in context.exception)        
        
    # Test for URL
        api2 = exoREST()
        api2.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees')
        
        # check for URL formatting is correct
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('def', 'example/com')
        
        # Raise exception if URL is null
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('abc', '')
        self.assertTrue('Null URL' in context.exception)
        
        # Raise warning if same URL has been added already
        with self.assertRaises(Warning) as context:
            api2.addAPI_URL('def', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertTrue('duplicate URL' in context.warning)
        
    def test_getURL_LIST(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : getURL_LIST(self)
        
        self.assertEqual(api.getURL_LIST(), {}, 'returns a null url_list on initial call')
        api.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertEqual(api.getURL_LIST(), {'abc': 'http://dummy.restapiexample.com/api/v1/employees'},'returns proper dictionay on call')
    
    def test_getDataAsJSON(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : getDataAsJSON(self, url_name, method = 'get', outputformat = 'json')
        api.addAPI_URL('abc', 'http://dummy.restapiexample.com/api/v1/employees/12')
        api.addAPI_URL('abc2', 'http://dummy.restapiexample.com/api/v1/employees/0')
        
        # test with a normal url_name, get a sucess 
        self.assertEqual( api.getDataAsJSON(url_name = 'abc'), True, 'Should run properly and return True')
        
        # test with a normal url_name, get a failure
        self.assertEqual( api.getDataAsJSON(url_name = 'abc2'), False, 'Should run properly and return False')
        
        # test with a non existing url_name
        with self.assertRaises(Exception) as context:
            api.getDataAsJSON(url_name = 'def')
        self.assertTrue('URL not existing' in context.exception)
        
        # test with null url
        with self.assertRaises(Exception) as context:
            api.getDataAsJSON(url_name = '')
        self.assertTrue('null url' in context.exception)
        
    def test_JSONStructure(self):
        pass

    def test_JSONParser(self):
        api = exoREST
        
        # FUNCTION SIGNATURE : JSONParser(self, jsonVar, hierarchy)
        jsonVar = {"status":"success", "data":{"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}}
        
        # simple test
        self.assertEqual(self.JSONParser(jsonVar, 'status'), "success" , "should return \'success\'" )
        
        # simple failing test: wrong hierarchy:
        with self.assertRaises(Exception) as context:
            api.JSONParser(jsonVar, 'stat')
        self.assertTrue('no key called stat in jsonVar' in context.exception)
        
        # null hierarchy -- ?????
        # -------------------Under consideration------------------------
        # with self.assertRaises(Exception) as context:
            # api.JSONParser(jsonVar, '')
        # self.assertTrue('null hierarchy not allowed' in context.exception)
        # -------------------Under consideration------------------------
        
        _jsonVar = {}
        
        #empty jsonvar
        
        with self.assertRaises(Warning) as context:
            api.JSONParser(_jsonVar, 'status')
        self.assertTrue('empty json var' in context.warning)
        
class TestSocialBot(unittest.TestCase):                
    def test_socialBot(self):
        pass
class TestMotivateU(unittest.TestCase):
    def test_MotivateU(self):
        pass
class TestMotivateU_GUI(unittest.TestCase):
    def test_gui(self):
        pass
        
if __name__ == '__main__':
    unittest.main()