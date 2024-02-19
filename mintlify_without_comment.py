
def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.oauth2_secret_key, algorithm=settings.oauth2_algorithm)
    return encoded_jwt
