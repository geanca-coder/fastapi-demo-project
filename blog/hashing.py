from passlib.context import CryptContext
class Hash():
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")
        
    def hash(self,password):
        return  self.pwd_context.hash(password)

    def verify(self, hashed_password, plain_password):
        return self.pwd_context.verify(plain_password, hashed_password)