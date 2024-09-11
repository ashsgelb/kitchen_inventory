import sqlite3

# database.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your models
class DrinkInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    coke = db.Column(db.Integer, nullable=False)
    diet_coke = db.Column(db.Integer, nullable=False)
    sprite = db.Column(db.Integer, nullable=False)
    coke_zero = db.Column(db.Integer, nullable=False)
    lacroix_lemoncello = db.Column(db.Integer, nullable=False)
    lacroix_lime = db.Column(db.Integer, nullable=False)
    lacroix_pamplemousse = db.Column(db.Integer, nullable=False)
    lacroix_pasteque = db.Column(db.Integer, nullable=False)
    horizon_milk = db.Column(db.Integer, nullable=False)
    tangerine = db.Column(db.Integer, nullable=False)
    lacroix_berry = db.Column(db.Integer, nullable=False)
    lemon = db.Column(db.Integer, nullable=False)
    lacroix_blackberry_cucumber = db.Column(db.Integer, nullable=False)
    lacroix_cherry_lime = db.Column(db.Integer, nullable=False)
    lacroix_pineapple_strawberry = db.Column(db.Integer, nullable=False)
    lacroix_ki_biscus = db.Column(db.Integer, nullable=False)

class KeurigInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    keurig = db.Column(db.Integer, nullable=False)

class NespressoInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    nespresso = db.Column(db.Integer, nullable=False)

class SnackInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    snack = db.Column(db.String(100), nullable=False)

class OfficeSupplyInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    office_supply = db.Column(db.String(100), nullable=False)
