from utilit import create_users_list, create_base_date, get_user_by_id, create_orders_list, get_order_by_id, \
    create_offers_list, get_offer_by_id, create_users, create_user, update_data, delete_data, create_order, create_offer
from table import *
import json
from flask import request

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return json.dumps(create_users_list())
    elif request.method == 'POST':
        if isinstance(request.json, list):
            create_user(request.json)
        elif isinstance(request.json, dict):
            create_user([request.json])
        return json.dumps(request.json)


@app.route("/users/<int:gid>", methods=['GET', 'PUT', 'DELETE'])
def load_users_by_id(gid):
    if request.method == 'GET':
        return json.dumps(get_user_by_id(gid))
    elif request.method == 'PUT':
        update_data(gid, User, request.json)
        return f"User # {gid} update"
    elif request.method == 'DELETE':
        delete_data(User, gid)
        return f"User # {gid} delete"


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return json.dumps(create_orders_list())
    elif request.method == 'POST':
        if isinstance(request.json, list):
            create_order(request.json)
        elif isinstance(request.json, dict):
            create_order([request.json])
        return json.dumps(request.json)


@app.route("/orders/<int:gid>", methods=['GET', 'PUT', 'DELETE'])
def load_orders_by_id(gid):
    if request.method == 'GET':
        return json.dumps(get_order_by_id(gid))
    elif request.method == 'PUT':
        update_data(gid, Order, request.json)
        return f"Order # {gid} update"
    elif request.method == 'DELETE':
        delete_data(Order, gid)
        return f"Order # {gid} delete"


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return json.dumps(create_offers_list())
    elif request.method == 'POST':
        if isinstance(request.json, list):
            create_offer(request.json)
        elif isinstance(request.json, dict):
            create_offer([request.json])
        return json.dumps(request.json)


@app.route("/offers/<int:gid>", methods=['GET', 'PUT', 'DELETE'])
def load_offer_by_id(gid):
    if request.method == 'GET':
        return json.dumps(get_offer_by_id(gid))
    elif request.method == 'PUT':
        update_data(gid, Offer, request.json)
        return f"Offer # {gid} update"
    elif request.method == 'DELETE':
        delete_data(Offer, gid)
        return f"Offer # {gid} delete"


if __name__ == "__main__":
    create_base_date()
    app.run(host="0.0.0.0", port=8080, debug=True)
