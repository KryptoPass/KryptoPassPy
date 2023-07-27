from __future__ import annotations
import hashlib
import os

ALGORITHMS_AVAILABLE = hashlib.algorithms_available

def _getFileHash(path: str, algorithm: hashlib._Hash, length):
    size = os.stat(path).st_size
    blockSize = 1_000_000
    
    if size < 1_000_000:
        blockSize = size
    
    rest = 0
    iterations = 0

    if size != 0:
        rest = size % blockSize
        iterations = int((size - rest) / blockSize)
    
    with open(path, "br") as file:
        for x in range(iterations):
            file.seek(int(x * blockSize), 0)
            algorithm.update(file.read(blockSize))
    
        if rest != 0:
            file.seek(size - rest)
            algorithm.update(file.read())
    
    if length:
        return algorithm.hexdigest(length)
    else:
        return algorithm.hexdigest()

def _getTextHash(data: str, algorithm: hashlib._Hash, length):
    algorithm.update(data.encode())

    if length:
        return algorithm.hexdigest(length)
    else:
        return algorithm.hexdigest()

def hash(value, algorithm_name, file=False, length=None):
    algorithm = hashlib.new(algorithm_name)
    
    if file:
        return _getFileHash(value, algorithm, length)
    else:
        return _getTextHash(value, algorithm, length)