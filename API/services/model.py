from API.interfaces.crud.create.model_repo import ModelRepository as Create
from API.interfaces.crud.read.model_repo import ModelRepository as Read
from API.interfaces.crud.update.model_repo import ModelRepository as Update
from API.interfaces.crud.delete.model_repo import ModelRepository as Delete

"""
    CURRENT_DIRECTORY - CURRENT_FILENAME script to (...insert the use for this script)
    ----------------------------------------------------------------------------
    >Created: 2024-11-09
    >Last_modified: 2024-11-09
    >Author: __name__
"""

class Model:
    # ================================= CREATE =================================
    @staticmethod
    def insert(json: dict):
        return Create.insert(json)
    
    # ================================== READ ==================================
    @staticmethod
    def request(json: dict):
        return Read.func(json)
    
    # ================================= UPDATE =================================
    @staticmethod
    def func3(parameter: str | None):
        pass
    
    # ================================= DELETE =================================
    @staticmethod
    def func4(parameter: str | None):
        pass
    