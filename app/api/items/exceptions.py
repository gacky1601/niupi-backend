from fastapi import HTTPException, status

ItemNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Item not found"
)


StoreNotFound = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Cannot add a new item to a store that does not exist"
)
