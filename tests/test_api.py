from exo import api as exoapi
import pytest


class Test_API:
    def test_addAPI_URL(self):
        api = exoapi.exoREST()

        # Test for URL_list
        assert api.url_list == {}, 'url_list must be a an empty dict initially'

        # Test for URL name
        assert api.addAPI_URL('validAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees') is None, 'It should successfully add'

        # Null URL name should throw exception
        with pytest.raises(Exception) :
            api.addAPI_URL('', 'http://dummy.restapiexample.com/api/v1/employees')

        # duplicate URL name should throw exception
        with pytest.raises(Exception):
            api.addAPI_URL('validAPI_URL', 'google.com')

        # Test for URL
        api2 = exoapi.exoREST()

        api2.addAPI_URL('validAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees')

        # Raise exception if URL is null
        with pytest.raises(Exception):
            api2.addAPI_URL('validAPI_URL', '')

        # check for URL formatting is correct
        with pytest.raises(Exception):
            api2.addAPI_URL('invalidAPI_URL', 'example/com')

        # Raise warning if same URL has been added already
        with pytest.raises(Warning):
            api2.addAPI_URL('duplicateAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees')

    def test_getURL_LIST(self):
        api = exoapi.exoREST()

        # FUNCTION SIGNATURE : getURL_LIST(self)

        assert api.getURL_LIST() == {}, 'returns a null url_list on initial call'

        api.addAPI_URL('validAPI_URL', 'http://dummy.restapiexample.com/api/v1/employees')

        assert api.getURL_LIST() == {'validAPI_URL': 'http://dummy.restapiexample.com/api/v1/employees'}, 'returns proper dictionay on call'

    def test_getDataFromAPI(self):
        api = exoapi.exoREST()
        # FUNCTION SIGNATURE : getDataFromAPI(self, url_name, method = 'get', outputformat = 'json')

        api.addAPI_URL('validAPI_URL', 'http://maps.googleapis.com/maps/api/geocode/json')
        api.addAPI_URL('invalid_URL', 'http://maps.googleapis.com/')

        json_abc1 = {"error_message": "Invalid request. Missing the 'address', 'components', 'latlng' or 'place_id' parameter.", "results": [], "status": "INVALID_REQUEST"}

        # test with a normal url_name, get a sucess
        assert api.getDataFromAPI(url_name='validAPI_URL') == json_abc1, 'Should run properly and return json_abc1'

        # test with a non existing url_name
        with pytest.raises(Exception) :
            api.getDataFromAPI(url_name='unknownAPI_URL')

        # test with null url
        with pytest.raises(Exception) :
            api.getDataFromAPI(url_name='')

        # test will invalid api url
        with pytest.raises(Exception) :
            api.getDataFromAPI(url_name='invalid_URL')
