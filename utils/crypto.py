import zlib
import hashlib

from __jcr__.secret import SECRET


def generate_hash(algorithm, string, salt=SECRET['DEFAULTS']['SALT'], by_crypt=False):
    """Will generate hash for any of the function"""

    sb = f'{string} {salt}'.encode('utf-8')

    if algorithm in ('adler32', 'crc32'):
        return getattr(zlib, algorithm)(sb).hexdigest()

    return getattr(hashlib, algorithm)(sb).hexdigest()
