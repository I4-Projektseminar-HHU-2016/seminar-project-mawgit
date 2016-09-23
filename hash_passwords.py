# -*- coding: utf-8 -*-

# Literaturverzeichnis (APA-Stil): 
# Sapin, Simon (2011): „Hashing passwords the Right Way − Exyr.org“. Exyr.org. Abgerufen am 26.08.2016 von http://exyr.org/2011/hashing-passwords/. (Zeile 8-27, 36-56, 58-70, 72-74, 77-89, 97-98)

# Dazu habe ich ein paar Veränderungen am Code vorgenommen. 

"""

    Securely hash and check passwords using PBKDF2.

    Use random salts to protect againt rainbow tables, many iterations against
    brute-force, and constant-time comparaison againt timing attacks.

    Keep parameters to the algorithm together with the hash so that we can
    change the parameters and keep older hashes working.

    See more details at http://exyr.org/2011/hashing-passwords/

    Author: Simon Sapin
    License: BSD

"""

import hashlib
from os import urandom
from base64 import b64encode, b64decode
import base64
#from itertools import izip   #for Python2.7
try:
    from itertools import izip
except ImportError:
    #If using Python3.x, change izip to zip and save it in variable izip
    izip = zip

# pbkdf2 is from https://github.com/mitsuhiko/python-pbkdf2
from pbkdf2 import pbkdf2_bin

# Required for generate_password
import string
import random


# Parameters to PBKDF2. Only affect new passwords.
SALT_LENGTH = 12
KEY_LENGTH = 24
HASH_FUNCTION = 'sha256'  # Must be in hashlib.
# Linear to the hashing time. Adjust to be high but take a reasonable
# amount of time on your server. Measure with:
# python -m timeit -s 'import passwords as p' 'p.make_hash("something")'
COST_FACTOR = 10000


def make_hash(password):
    """ Generate a random salt and return a new hash for the password. """
    if isinstance(password, unicode):  #for Python2.7
    #if isinstance(password, str):  #for Python3.x
        password = password.encode('utf-8')
    salt = b64encode(urandom(SALT_LENGTH))
    return 'PBKDF2${}${}${}${}'.format(
        HASH_FUNCTION,
        COST_FACTOR,
        salt,
        b64encode(pbkdf2_bin(password, salt, COST_FACTOR, KEY_LENGTH,
                             getattr(hashlib, HASH_FUNCTION))))


def check_hash(password, hash_):
    """ Check a password against an existing hash. """
    if isinstance(password, unicode):  #for Python2.7
    #if isinstance(password, str):  #for Python3.x
        password = password.encode('utf-8')
    algorithm, hash_function, cost_factor, salt, hash_a = hash_.split('$')
    assert algorithm == 'PBKDF2'
    #hash_a = b64decode(hash_a, altchars=None, validate=False)
    #hash_a = base64.b64decode(hash_a)
    hash_a = b64decode(hash_a)
    hash_b = pbkdf2_bin(password, salt, int(cost_factor), len(hash_a),
                        getattr(hashlib, hash_function))
    assert len(hash_a) == len(hash_b)  # we requested this from pbkdf2_bin()
    # Same as "return hash_a == hash_b" but takes a constant time.
    # See http://carlos.bueno.org/2011/10/timing.html
    diff = 0
    for char_a, char_b in izip(hash_a, hash_b):
        diff |= ord(char_a) ^ ord(char_b)
    return diff == 0

def generate_password(length = 8):
    """ This function (for Python2.7 only) is from a seminar of Tobias Siebenlist """
    #I made it Python3.x compatible.
    try:
        xrange 
    except NameError: 
        # If Python3.x then change xrange to range
        xrange = range

    chars = string.letters + string.digits
    return ''.join(random.choice(chars) for _ in xrange(length))

