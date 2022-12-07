from fastapi import HTTPException, status

StoreNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="There is no store owned by this user"
)


InitializeNonExistingStore = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Cannot initialize an store that does not exist"
)
