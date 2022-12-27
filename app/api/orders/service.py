from pydantic import UUID4, conlist
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Session

from .models import Orders, OrderItem


def get_order_by_order_id(database: Session, order_id: str):
    items_json_object = (
        """
            jsonb_build_object(
                'name', item.name,
                'price', item.price,
                'photo_id', (photos.photo_id)[1],
                'quantity', order_item.quantity
            )AS items
        """
    )

    statement = (
        f"""
            WITH items AS (
                SELECT array_agg(items) as items FROM (
                    SELECT DISTINCT {items_json_object}
                    FROM orders
                    LEFT JOIN order_item
                    ON orders.id = order_item.order_id
                    LEFT JOIN item
                    ON order_item.item_id = item.id
                    LEFT JOIN (
                        SELECT item_id, array_agg(id) as photo_id
                        FROM item_photo
                        GROUP BY item_id
                    ) as photos
                    ON order_item.item_id=photos.item_id
                    GROUP BY item.name, item.price, order_item.quantity, photos.photo_id
                ) as t
            )

            SELECT orders.store_id, store.name as store_name, users.username as recipient,
                   users.cellphone_number as recipient_telephone_number, users.address,
                   SUM(item.price) * SUM(order_item.quantity) as sub_total, items.items,
                   orders.shipping_fee, items.items,
                   (SUM(item.price) * SUM(order_item.quantity) + shipping_fee) as total_amount
            FROM orders
            LEFT JOIN store
            ON orders.store_id = store.id
            LEFT JOIN users
            ON orders.user_id = users.id
            LEFT JOIN order_item
            ON orders.id = order_item.order_id
            LEFT JOIN item
            ON order_item.item_id = item.id
            LEFT JOIN item_photo
            ON order_item.item_id=item_photo.item_id
            JOIN items
            ON TRUE
            WHERE orders.id = '{order_id}'
            GROUP BY orders.store_id, store.name, item.name,
            item.price, recipient, recipient_telephone_number,
            orders.shipping_fee, order_item.quantity, users.address, items.items
        """
    )

    return database.execute(statement).first()
