from uuid import UUID

from sqlalchemy.orm import Session

from .models import Cart


def get_cart_by_id(db: Session, user_id: UUID):
    items_json_object = (
        """
        jsonb_build_object(
            'name', item.name,
            'price', item.price,
            'photo_id', (array_agg(item_photo.id))[1],
            'updated_at', cart.updated_at,
            'quantity', cart.quantity
        )AS items
        """
    )

    statement = (
        f"""
            SELECT DISTINCT store.id, store.name, items.items
            FROM cart
            LEFT JOIN item
            ON cart.item_id = item.id
            LEFT JOIN store
            ON store.id = item.store_id
            LEFT JOIN (
                SELECT array_agg(items) as items FROM (
                    SELECT {items_json_object}
                    FROM cart
                    LEFT JOIN item
                    ON cart.item_id = item.id
                    LEFT JOIN item_photo
                    ON cart.item_id=item_photo.item_id
                    GROUP BY item.name, item.price, cart.updated_at, cart.quantity
                    ORDER BY cart.updated_at
                ) AS t
            ) AS items
            ON TRUE
            WHERE cart.user_id = '{user_id}'
            GROUP BY store.id,store.name, items.items
        """
    )

    return db.execute(statement).all()
