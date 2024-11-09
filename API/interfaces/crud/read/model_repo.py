from API.models.orm import ProductModel, ClientModel, AccountInfoModel
from API.mapping.modelMapping import model_mapping
from API import db

from flask import jsonify
"""
    CURRENT_DIRECTORY - CURRENT_FILENAME script to (...insert the use for this script)
    ----------------------------------------------------------------------------
    >Created: 2024-11-09
    >Last_modified: 2024-11-09
    >Author: __name__
"""

class ModelRepository:
    @staticmethod
    def func(json: dict):
        """Query the data from database using json payload
        
        :param json: dict variable is the request received trough /api/query
        
        .. versionchanged:: 0.1
        """
        table_name = json.get("table")
        filters = json.get("filters", {})
        
        model = model_mapping.get(table_name)
        if not model:
            return jsonify({"error": "Invalid table name"}), 400

        query = model.query.filter_by(**filters).all()
        
        if not query:
            return jsonify({"error": "No row found for filters"}), 400
        
        results = []
        for item in query:
            item_data = {key: getattr(item, key) for key in item.__dict__.keys() if not key.startswith('_')}
            results.append(item_data)
        
        return jsonify(results)
    