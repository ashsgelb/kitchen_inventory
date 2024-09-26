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
    half_caff = db.Column(db.Integer, nullable=False)
    breakfast_blend = db.Column(db.Integer, nullable=False)
    breakfast_blend_decaf = db.Column(db.Integer, nullable=False)
    colombia_select = db.Column(db.Integer, nullable=False)
    nantucket_blend = db.Column(db.Integer, nullable=False)
    bigelow_lemon_echinacea = db.Column(db.Integer, nullable=False)
    swiss_miss_milk_chocolate = db.Column(db.Integer, nullable=False)
    vanilla_latte = db.Column(db.Integer, nullable=False)
    chai_latte = db.Column(db.Integer, nullable=False)
    cafe_bustelo_dark_roast = db.Column(db.Integer, nullable=False)
    mandarin_orange_spice = db.Column(db.Integer, nullable=False)
    tim_hortons_original = db.Column(db.Integer, nullable=False)
    light_roast = db.Column(db.Integer, nullable=False)
    house_decaf = db.Column(db.Integer, nullable=False)
    dunkin_original_blend = db.Column(db.Integer, nullable=False)
    

class NespressoInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    de_scuro = db.Column(db.Integer, nullable=False)
    il_caffe = db.Column(db.Integer, nullable=False)
    voltesso = db.Column(db.Integer, nullable=False)
    fortado = db.Column(db.Integer, nullable=False)
    toccanto = db.Column(db.Integer, nullable=False)
    festive_black = db.Column(db.Integer, nullable=False)
    seasonal_delight_spices = db.Column(db.Integer, nullable=False)
    frosted_caramel_nut = db.Column(db.Integer, nullable=False)
    stormio = db.Column(db.Integer, nullable=False)
    half_caffeinato = db.Column(db.Integer, nullable=False)
    melozio = db.Column(db.Integer, nullable=False)
    mexico_mexique = db.Column(db.Integer, nullable=False)
    melozio_decaffeinato_coffee = db.Column(db.Integer, nullable=False)

class SnackInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    baked_chips = db.Column(db.Integer, nullable=False)
    kirkland_snacking_nuts = db.Column(db.Integer, nullable=False)
    kirkland_trail_mix = db.Column(db.Integer, nullable=False)
    popcorn = db.Column(db.Integer, nullable=False)
    kirkland_nut_bars = db.Column(db.Integer, nullable=False)
    fruit_strips_variety_pack = db.Column(db.Integer, nullable=False)
    cheez_it_snapped = db.Column(db.Integer, nullable=False)
    skinny_pop = db.Column(db.Integer, nullable=False)
    nature_valley_protein_bars = db.Column(db.Integer, nullable=False)
    sun_chips = db.Column(db.Integer, nullable=False)
    cheez_it = db.Column(db.Integer, nullable=False)
    pretzels = db.Column(db.Integer, nullable=False)

class OfficeSupplyInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)
    office_supply = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)