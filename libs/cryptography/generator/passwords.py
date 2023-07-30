import os
from libs.cryptography.random import Random

ascii_lowercase = list("abcdefghijklmnopqrstuvwxyz")
ascii_uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = list("0123456789")
punctuation = list(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
emoji = ["🙏","😀","😁","😂","😃","😄","😅","😆",
         "😇","😈","😉","😊","😋","😌","😍","😎",
         "😏","😐","😑","😒","😓","😔","😕","😖",
         "😗","😘","😙","😚","😛","😜","😝","😞",
         "😟","😠","😡","😢","😣","😤","😥","😦",
         "😧","😨","😩","😪","😫","😬","😭","😮",
         "😯","😰","😱","😲","😳","😴","😵","😶",
         "😷","😸","😹","😺","😻","😼","😽","😾",
         "😿","🙀","🙁","🙂","🙃","🙄","🙅","🙆",
         "🙇","🙈","🙉","🙊","🙋","🙌","🙍","🙎",] # 🚀📚

def password(length=10, use_specials=False, use_upper=False, use_digits=False, use_emojis=False, use_quantum=False):
    random = Random()
    if use_quantum: random.quantum()

    s_ascii_lowercase = ''.join(random.choice(ascii_lowercase) for _ in range(length))
    s_ascii_uppercase = ''.join(random.choice(ascii_uppercase) for _ in range(length))
    s_digits = ''.join(random.choice(digits) for _ in range(length))
    s_punctuation = ''.join(random.choice(punctuation) for _ in range(length))
    s_emoji = ''.join(random.choice(emoji) for _ in range(length))

    allowed_chars = s_ascii_lowercase

    if use_digits:
        allowed_chars += s_digits
    if use_upper:
        allowed_chars += s_ascii_uppercase
    if use_specials:
        allowed_chars += s_punctuation
    if use_emojis:
        allowed_chars += s_emoji
    
    password_list = list(allowed_chars)
    random.shuffle(password_list)
    return ''.join(random.choice(password_list) for _ in range(length))

def passphrase(length, separator, dict, use_quantum):
    random = Random()
    if use_quantum: random.quantum()

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bip-0039", dict + ".txt")
    
    if dict not in {"chinese_simplified", "chinese_traditional", "czech", "english","french", "italian", "japanese", "korean","portuguese", "spanish"}:
        path = dict

    with open(path, "r", encoding="utf8") as f:
        data = f.read().split("\n")
        return separator.join(random.choice(data) for _ in range(length))