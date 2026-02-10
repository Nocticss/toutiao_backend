
"""
from passlib.context import CryptContext

#创建密码上下文
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


#密码加密
def get_hash_password(password:str):
    return pwd_context.hash(password)
"""
from passlib.context import CryptContext

# 把 bcrypt 换成这个，无长度限制，彻底解决问题
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

