from fastapi import HTTPException, status

ItemNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Item not found"
)
