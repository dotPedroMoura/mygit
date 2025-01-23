import hashlib
import os

GIT_DIRECTORY = '.mygit'

def init():
    os.makedirs(GIT_DIRECTORY)
    os.makedirs(os.path.join(GIT_DIRECTORY, 'objects'))

def hash_object(data):
    object_id = hashlib.sha1(data).hexdigest()
    with open(f'{os.path.join(GIT_DIRECTORY, 'objects', object_id)}', 'wb') as output:
        output.write(data)

    return object_id