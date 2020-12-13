from io import BytesIO
from secrets import token_bytes
from PIL import Image
from typing import Tuple


def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")


def encrypt(img: Image, fmt: str) -> Tuple[int, int]:
    b: BytesIO = BytesIO()
    img.save(b, fmt)
    b.seek(0)
    original_bytes: bytes = b.read()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> Image:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return Image.open(BytesIO(temp))


if __name__ == "__main__":
    rabbit_img: Image = Image.open("rabbit.jpg", "r")
    key1, key2 = encrypt(rabbit_img, "jpeg")
    result: Image = decrypt(key1, key2)
    result.save("rabbit-decrypted.jpg")