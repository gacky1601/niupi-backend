from fastapi import HTTPException, status

StoreNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="There is no store owned by this user"
)


SellerNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Cannot initialize an store that does not exist"
)
