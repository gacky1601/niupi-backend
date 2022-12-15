from fastapi import HTTPException, status

SellerNotFound = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Seller not found"
)
