from API import db

from datetime import datetime

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.TEXT, nullable=True)
    price = db.Column(db.Float, nullable=False)
    sku = db.Column(db.TEXT, nullable=True)
    stockQtty = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.Integer, nullable=True)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    createdBy = db.Column(db.String(10), nullable=False)
    modifiedOn = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modifiedBy = db.Column(db.String(10), nullable=False)

class ClientModel(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    cellphone = db.Column(db.String(15), unique=True, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    createdBy = db.Column(db.String(10), nullable=False)
    modifiedOn = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modifiedBy = db.Column(db.String(10), nullable=False)

class AccountInfoModel(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    clientID = db.Column(db.Integer, nullable=False)
    LastLoginDate = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Status = db.Column(db.String(10), default="active", nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modifiedOn = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)