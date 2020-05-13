from exo import exoREST
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
    