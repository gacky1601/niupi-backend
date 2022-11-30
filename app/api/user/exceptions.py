from fastapi import HTTPException, status

UserNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found"
)

DeleteNonExistingUser = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Cannot delete an account that does not exist"
)

UpdateNonExistingUser = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Non-existent users cannot be updated"
)

InvalidCellphoneNumber = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
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
