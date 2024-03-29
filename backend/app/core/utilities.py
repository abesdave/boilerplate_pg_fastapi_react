from app.models import User, Token


async def encode_jwt(user: User) -> Token:
    return Token(type="Bearer", token=f"fakehashedtoken_{user.id}_{user.username}")


async def decode_jwt() -> User:
    pass
