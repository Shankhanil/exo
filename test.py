import unittest
from src.exo import exoREST, exoJSON

class Test_exoREST(unittest.TestCase):
    def test_addAPI_URL(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : addAPI_URL(self, url_name, url)
        
    # Test for URL_list
        # url_list must be a an empty dict initially
        self.assertEqual(api.url_list, {}, 'Initial url list must be empty')
        
     # Test for URL name
        # Try to add 'validAPI_URL' url. It should successfully add
        self.assertEqual(api.addAPI_URL('validAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees'), None, 'Function should return nothing on success')
        
        #Null URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('', 'http://dummy.restapiexample.com/api/v1/employees')
        
        #duplicate URL name should throw exception
        with self.assertRaises(Exception) as context:
            api.addAPI_URL('validAPI_URL', 'google.com')
        
    # Test for URL
        api2 = exoREST()
        api2.addAPI_URL('validAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees')
        
        # Raise exception if URL is null
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('validAPI_URL', '')
            
        # check for URL formatting is correct
        with self.assertRaises(Exception) as context:
            api2.addAPI_URL('invalidAPI_URL', 'example/com')
        
        # Raise warning if same URL has been added already
        with self.assertRaises(Warning) as context:
            api2.addAPI_URL('duplicateAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees')
        # self.assertTrue('duplicate URL' in context.warning)
        
    def test_getURL_LIST(self):
        api = exoREST()
        
        # FUNCTION SIGNATURE : getURL_LIST(self)
        
        self.assertEqual(api.getURL_LIST(), {}, 'returns a null url_list on initial call')
        api.addAPI_URL('validAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees')
        self.assertEqual(api.getURL_LIST(), {'validAPI_URL': 'http://dummy.restapiexample.com/api/v1/employees'},'returns proper dictionay on call')
    
    def test_getDataFromAPI(self):
        api = exoREST()
        # FUNCTION SIGNATURE : getDataFromAPI(self, url_name, method = 'get', outputformat = 'json')
        api.addAPI_URL('validAPI_URL', 'http://maps.googleapis.com/maps/api/geocode/json')
        api.addAPI_URL ('invalid_URL', 'http://maps.googleapis.com/')
        json_abc1 = {"error_message" : "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter.","results" : [],"status" : "INVALID_REQUEST"}
        
        # test with a normal url_name, get a sucess 
        self.assertEqual( api.getDataFromAPI(url_name = 'validAPI_URL'), json_abc1, 'Should run properly and return json_abc1')
        
        # test with a non existing url_name
        with self.assertRaises(Exception) as context:
            api.getDataFromAPI(url_name = 'unknownAPI_URL')
        
        # test with null url
        with self.assertRaises(Exception) as context:
            api.getDataFromAPI(url_name = '')
            
        # test will invalid api url
        with self.assertRaises(Exception) as context:
            api.getDataFromAPI(url_name = 'invalid_URL')

class Test_exoJSON(unittest.TestCase):
    
    def test_JSONStructure(self):
        jsonVar = {"status":"success", "data":{"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}}

        structure_1 = ['status', 'data', 'data/id', 'data/employee_name','data/employee_salary','data/employee_age','data/profile_image']
        # Get entire json tree structure.
        self.assertEqual( exoJSON.JSONStructure(jsonVar), structure_1, "should return the JSON tree structure" )
        
        self.assertEqual( exoJSON.JSONStructure(jsonVar, 'status'), ['status'], "should return the JSON tree structure" )
        self.assertEqual( exoJSON.JSONStructure(jsonVar, 'data'), ['data', 'data/id', 'data/employee_name','data/employee_salary','data/employee_age','data/profile_image'], "should return the JSON tree structure" )
        self.assertEqual( exoJSON.JSONStructure(jsonVar, '__ROOT__'), ['status','data'], "should return the JSON tree structure" )
        
    def test_JSONParser(self):
        
        # FUNCTION SIGNATURE : JSONParser(self, jsonVar, hierarchy)
        jsonVar = {"status":"success", "data":{"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}}
        _jsonVar = {}
        # simple test with single level hierarchy
        self.assertEqual( exoJSON.JSONParser(jsonVar,"status") , "success" , "should return \'success\'" )
        
        # simple test with multi level hierarchy
        
        self.assertEqual( exoJSON.JSONParser(jsonVar, "data/id") , "1" , "should return \'1\'" )
        
        # simple test with multi level hierarchy
        nestedJSON = {"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}
        self.assertEqual( exoJSON.JSONParser(jsonVar, "data") , nestedJSON , "should return jsonVar[data]" )
        
        # simple failing test: wrong hierarchy:
        with self.assertRaises(Exception) as context:
            exoJSON.JSONParser(jsonVar, 'stat')
        
        # null hierarchy -- RETURN entire JSON
        self.assertEqual( exoJSON.JSONParser(jsonVar, "") , jsonVar , "should return entire jsonVar" )
        
        _jsonVar = {}
        
        #empty jsonvar
        with self.assertRaises(Warning) as context:
            exoJSON.JSONParser(_jsonVar, 'status')
        
if __name__ == '__main__':
    unittest.main()