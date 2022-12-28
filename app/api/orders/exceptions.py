from fastapi import HTTPException, status

OrderNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Order not found"
)

OrderIdInvalidFormat = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail=[
        {
            "loc": ["path", "order_id"],
            "msg": "value is not a valid format",
            "type": "type_error.uuid"
        }
    ]
)
