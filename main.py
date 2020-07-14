import jwt


def create_token(data, secret):
    token = jwt.encode(data, secret, algorithm='HS256')
    return token


def verify_signature(token):
    try:
        signature = jwt.decode(token, "acelera", algorithms='HS256')
        return signature
    except:
        return({"error": 2})
