from exo import json as _json
import pytest

class Test_json:
    def test_JSONStructure(self):
        jsonVar = {"status":"success", "data":{"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}}

        structure_1 = ['status', 'data', 'data/id', 'data/employee_name','data/employee_salary','data/employee_age','data/profile_image']
        structure_data = ['data','data/id', 'data/employee_name','data/employee_salary','data/employee_age','data/profile_image']
        structure_ROOT = ['status', 'data']
        
        actual_structure_1 = _json.exoJSON().JSONStructure(jsonVar)
        actual_structure_data = _json.exoJSON().JSONStructure(jsonVar, 'data')
        actual_structure_ROOT = _json.exoJSON().JSONStructure(jsonVar, '__ROOT__')

        assert len(actual_structure_1) == len(structure_1)
        for element in structure_1:
            assert element in actual_structure_1
        
        assert  _json.exoJSON().JSONStructure(jsonVar, 'status') == ['status'], "should return the JSON tree structure"
        
        assert len(actual_structure_data) == len(structure_data)
        for element in structure_data:
            assert element in actual_structure_data
        
        assert len(actual_structure_ROOT) == len(structure_ROOT)
        for element in structure_ROOT:
            assert element in actual_structure_ROOT
        
        
        # if invalid keys, raise an error
        with pytest.raises(Exception) :
            _json.exoJSON().JSONStructure(jsonVar, 'some_invalid_key')
        
    def test_JSONParser(self):
        
        # FUNCTION SIGNATURE : JSONParser(self, jsonVar, hierarchy)
        jsonVar = {"status":"success", "data":{"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}}
        _jsonVar = {}
        # simple test with single level hierarchy
        assert  _json.exoJSON().JSONParser(jsonVar,"status") == "success" , "should return \'success\'"
        
        # simple test with multi level hierarchy
        
        assert  _json.exoJSON().JSONParser(jsonVar, "data/id") ==  "1" , "should return \'1\'" 
        
        # simple test with multi level hierarchy
        nestedJSON = {"id":"1","employee_name":"Tiger Nixon","employee_salary":"320800",\
        "employee_age":"61","profile_image":""}
        assert  _json.exoJSON().JSONParser(jsonVar, "data") == nestedJSON , "should return jsonVar[data]"
        
        # simple failing test: wrong hierarchy:
        with pytest.raises(Exception) :
            _json.exoJSON().JSONParser(jsonVar, 'stat')
        
        # null hierarchy -- RETURN entire JSON
        assert  _json.exoJSON().JSONParser(jsonVar, "") == jsonVar , "should return entire jsonVar"
        
        _jsonVar = {}
        
        #empty jsonvar
        with pytest.raises(Warning) :
            _json.exoJSON().JSONParser(_jsonVar, 'status')
