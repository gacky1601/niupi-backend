from fastapi import HTTPException, status

EmailExists = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Email already in use"
)
