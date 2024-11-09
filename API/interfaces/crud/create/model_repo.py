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
    def insert(json: dict):
        """Commit the data from json payload into the database
        
        :param json: dict variable is the poayload received to insert into database
        
        .. versionchanged:: 0.1
        """
        table_name = json.get("table")
        insert_data = json.get("data", {})

        # Get the model based on the table name in the payload
        model = model_mapping.get(table_name)
        if not model:
            return jsonify({"error": "Invalid table name"}), 400

        # Create a new instance of the model with the provided data
        try:
            new_record = model(**insert_data)
            db.session.add(new_record)
            db.session.commit()
            return jsonify({"message": "Record inserted successfully", "id": new_record.id}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 409
        