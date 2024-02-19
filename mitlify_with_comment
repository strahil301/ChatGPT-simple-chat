
def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    The function `create_access_token` generates an access token with optional expiration time.
    
    :param data: The `data` parameter is a dictionary containing the information that you want to encode
    into the access token. This information can include user details, permissions, or any other data
    that you want to associate with the token
    :type data: Dict[str, Any]
    :param expires_delta: The `expires_delta` parameter is an optional parameter that specifies the
    duration for which the access token will be valid. If provided, the access token will expire after
    the specified duration. If not provided, the access token will expire after 30 minutes by default
    :type expires_delta: Optional[timedelta]
    :return: A JWT (JSON Web Token) is being returned as a string.
    """
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.oauth2_secret_key, algorithm=settings.oauth2_algorithm)
    return encoded_jwt
