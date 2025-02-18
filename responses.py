from fastapi import HTTPException, Response

LOGIN_REQUIRED = HTTPException(status_code=401, detail="Login required")
USER_NOT_FOUND = HTTPException(status_code=404, detail="User not found")
USER_NOT_FOUND_IN_DB = HTTPException(status_code=402, detail="User not found in db")
INVALID_SESSION = HTTPException(status_code=401, detail="Invalid session")
