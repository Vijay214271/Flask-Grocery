from itsdangerous import URLSafeTimedSerializer
from key import secret_key,salt,salt2
def token1(data1,salt):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data1,salt=salt)