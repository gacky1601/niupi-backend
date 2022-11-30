from fastapi import HTTPException, status

StoreNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="There is no store owned by this user"
)


SellerNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Seller not found"
)


InvalidCellphoneNumber = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail=[
        {
            "loc": [
                "body",
                "cellphone_number"
            ],
            "msg": "value is not a valid cellphone number",
            "type": "value_error.cellphone_number"
        }
    ]
)

InvalidTelephoneNumber = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail=[{
        "loc": [
            "body",
            "telephone_number"
        ],
        "msg": "value is not a valid telephone number",
        "type": "value_error.telephone_number"
    }]
)
