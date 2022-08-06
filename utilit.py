import json

from table import *


def open_json(file):
    with open(f"{file}", 'r', encoding="utf-8") as file_json:
        return json.load(file_json)


def create_users():
    for user in open_json('users.json'):
        new_user = User(
            id=user.get('id'),
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            age=user.get('age'),
            email=user.get('email'),
            role=user.get('role'),
            phone=user.get('phone')
        )
        db.session.add(new_user)
    db.session.commit()


def create_orders():
    for order in open_json('orders.json'):
        new_order = Order(
            id=order.get('id'),
            name=order.get('name'),
            description=order.get('description'),
            start_date=order.get('start_date'),
            end_date=order.get('end_date'),
            address=order.get('address'),
            price=order.get('price'),
            customer_id=order.get('customer_id'),
            executor_id=order.get('executor_id')
        )
        db.session.add(new_order)
    db.session.commit()


def create_offers():
    for offer in open_json('offers.json'):
        new_offer = Offer(
            id=offer.get('id'),
            order_id=offer.get('order_id'),
            executor_id=offer.get('executor_id')
        )
        db.session.add(new_offer)
    db.session.commit()


def create_base_date():
    db.drop_all()
    db.create_all()
    create_users()
    create_orders()
    create_offers()


def create_users_list():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.make_dist())
    return result


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user.make_dist()


def create_orders_list():
    orders = Order.query.all()
    result = []
    for order in orders:
        result.append(order.make_dist())
    return result


def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    return order.make_dist()


def create_offers_list():
    offers = Offer.query.all()
    result = []
    for offer in offers:
        result.append(offer.make_dist())
    return result


def get_offer_by_id(offer_id):
    offer = Offer.query.get(offer_id)
    return offer.make_dist()


def create_user(input_data):
    for user in input_data:
        db.session.add(
            User(
                id=user.get("id"),
                first_name=user.get("first_name"),
                last_name=user.get("last_name"),
                age=user.get("age"),
                email=user.get("email"),
                role=user.get("role"),
                phone=user.get("phone")
                )
            )
    db.session.commit()


def update_data(data_id, db_data, update_data):
    row = db_data.query.get(data_id)
    row.id = update_data.get("id")
    row.first_name = update_data.get("first_name")
    row.last_name = update_data.get("last_name")
    row.age = update_data.get("age")
    row.email = update_data.get("email")
    row.role = update_data.get("role")
    row.phone = update_data.get("phone")

    row.name = update_data.get("name")
    row.description = update_data.get("description")
    row.start_date = update_data.get("start_date")
    row.end_date = update_data.get("end_date")
    row.address = update_data.get("address")
    row.price = update_data.get("price")
    row.customer_id = update_data.get("customer_id")
    row.executor_id = update_data.get("executor_id")

    db.session.commit()


def delete_data(db_data, data_id):
    data = db_data.query.get(data_id)
    db.session.delete(data)
    db.session.commit()


def create_order(input_data):
    for order in input_data:
        db.session.add(
            Order(
                id=order.get('id'),
                name=order.get('name'),
                description=order.get('description'),
                start_date=order.get('start_date'),
                end_date=order.get('end_date'),
                address=order.get('address'),
                price=order.get('price'),
                customer_id=order.get('customer_id'),
                executor_id=order.get('executor_id')
                )
            )
    db.session.commit()


def create_offer(input_data):
    for offer in input_data:
        db.session.add(
            Offer(
                id=offer.get('id'),
                order_id=offer.get('order_id'),
                executor_id=offer.get('executor_id')
                )
            )
    db.session.commit()

