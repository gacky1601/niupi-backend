from fastapi import HTTPException, status

StoreNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="There is no store owned by this user"
)
