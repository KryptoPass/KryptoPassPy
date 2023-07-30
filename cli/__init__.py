from gettext import gettext as _
import argparse
import sys

from libs.config import Config


from libs.cryptography.hash import ALGORITHMS_AVAILABLE
from utility.logger import setLevel

parser = argparse.ArgumentParser(_("parser.prog"), description=_("parser.description"), epilog=_("parser.epilog"))
parser.add_argument("--verbose", "-v", default=1, action="count", help=_("parser.argument_verbose_help"))

subparser = parser.add_subparsers(dest="action")

# Subparser to manage tools
tools = subparser.add_parser("tools")
tools_subparser = tools.add_subparsers(dest="tools", required=True)

# Subparser for password, passphrase, and encryption key generation
generate_parser = tools_subparser.add_parser(name="generate", help=_("generate_parser.generate_help"))
generate_subparser = generate_parser.add_subparsers(dest="generate", required=True)

# Password Generator
generator_password = generate_subparser.add_parser(name="password", help=_("parser.generate_subparser.password_help"))
generator_password.add_argument("--length", "-l", action="store", help=_("parser.generate_subparser.password.argument_length_help"), default=10, type=int)
generator_password.add_argument("--specials", "-s", action="store_true", help=_("parser.generate_subparser.password.argument_specials_help"))
generator_password.add_argument("--upper", "-u", action="store_true", help=_("parser.generate_subparser.password.argument_upper_help"))
generator_password.add_argument("--digits", "-d", action="store_true", help=_("parser.generate_subparser.password.argument_digits_help"))
generator_password.add_argument("--emojis", "-e", action="store_true", help=_("parser.generate_subparser.password.argument_emojis_help"))
generator_password.add_argument("--quantum", "-q", action="store_true", help=_("parser.generate_subparser.password.argument_quantum_help"))

# Passphrase Generator
generator_passphrase = generate_subparser.add_parser(name="passphrase", help="Generate a random passphrase")
generator_passphrase.add_argument("--length", "-l", action="store", help="set the number of words for the passphrase", default=12, type=int)
generator_passphrase.add_argument("--separator", "-s", action="store", help="sets the separator character to use", default="")
generator_passphrase.add_argument("--dict", "-d", action="store", metavar="DICT/PATH",  default="english", help="chinese_simplified, chinese_traditional, czech, english, french, italian, japanese, korean, portuguese, spanish")
generator_passphrase.add_argument("--quantum", "-q", action="store_true", help="uses a seed of quantum random numbers to generate the passphrase (requires internet connection)")

# Keys Generator
generator_key = generate_subparser.add_parser(name="key", help="Generate a random key")
generator_key.add_argument("--length", "-l", action="store", help="length of the key to be generated", default=32, type=int)
generator_key.add_argument("--quantum", "-q", action="store_true", help="uses a seed of quantum random numbers to generate the key (requires internet connection)")
generator_key.add_argument("--output", "-o", action="store", help="the format to be exported hex, raw, base64", choices=["hex", "base64", "raw"], default="base64")
generator_key.add_argument("--file", "-f", action="store", help="path to save the file | note this option will replace everything in content")

# Subparser for calculating hashes of text and files
hash_parser = tools_subparser.add_parser(name="hash", help="Calculate the hash of text and files with different algorithms")

# Hash Group
hash_group = hash_parser.add_mutually_exclusive_group(required=True)
hash_group.add_argument("--text", "-t", action="store_true", help="Calculate hash of text")
hash_group.add_argument("--file", "-f", action="store_true", help="Calculate hash of file")

# Hash Arguments
hash_parser.add_argument("--length", "-l", action="store", help="Length for shake_128 and shake_256 algorithms", type=int)
hash_parser.add_argument("--algorithm", "-a", action="store", choices=ALGORITHMS_AVAILABLE, default="sha256", help="Hash algorithm to use")
hash_parser.add_argument("--output", "-o", action="store", default="default", help="Output file path")
hash_parser.add_argument("--compare", "-c", action="store", help="Compare the resulting hash with the entered one (only works when hashing a file)")
hash_parser.add_argument("value", action="store", help="File path or text", metavar="PATH/FILES", nargs="+")

# Subparser for encoding text in base64 and hexadecimal
encode_parser = tools_subparser.add_parser(name="encode", help="Encode text in base64 and hexadecimal")
encode_group = encode_parser.add_mutually_exclusive_group(required=True)
encode_group.add_argument("--base64", "-b", action="store_true", help="Encode text in base64")
encode_group.add_argument("--hex", "-x", action="store_true", help="Encode text in hexadecimal")
encode_parser.add_argument("value", action="store", help="Text to encode")

# Subparser for decoding text from base64 and hexadecimal
decode_parser = tools_subparser.add_parser(name="decode", help="Decode text from base64 and hexadecimal")

login = subparser.add_parser("login")
login.add_argument("--database", "-d", action="store", help="database file path")
login.add_argument("--password", "-p", action="store", help="allows to pass the password as an argument, if not specified it is requested in interactive mode")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

arguments = parser.parse_args()

if arguments.verbose and arguments.verbose <= 0 or arguments.verbose > 4:
    raise parser.error(f"Verbose count must be between 1 and 4")
else:
    setLevel(arguments.verbose)

if "tools" in arguments:
    from .tools import parse_tools
    parse_tools()
elif arguments.action == "login":
    from .login import parse_login
    parse_login()
else:
    parser.print_help()
    sys.exit(0)
