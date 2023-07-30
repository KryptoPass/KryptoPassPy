import secrets
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from cryptography.hazmat.primitives.asymmetric.dsa import generate_private_key
from cryptography.hazmat.primitives.asymmetric.ec import generate_private_key
from cryptography.hazmat.primitives.kdf import x963kdf, scrypt, concatkdf, hkdf, kbkdf, pbkdf2
from argon2 import PasswordHasher

from libs.cryptography.random import Random

def asymmetric():
    pass

def symmetric():
    pass