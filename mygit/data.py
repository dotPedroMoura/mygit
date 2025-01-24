import hashlib
import os

GIT_DIRECTORY = '.mygit'

def init():
    os.makedirs(GIT_DIRECTORY)
    os.makedirs(os.path.join(GIT_DIRECTORY, 'objects'))
    print(f'Initialized empty mygit repository in {os.path.join(os.getcwd(), GIT_DIRECTORY)}')

def hash_object(data, obj_type ='blob'):
    obj = obj_type.encode() + b'\x00' + data
    obj_id = hashlib.sha1(obj).hexdigest()
    with open(f'{os.path.join(GIT_DIRECTORY, 'objects', obj_id)}', 'wb') as output:
        output.write(obj)

    return obj_id

def get_object(obj_id, expected_type ='blob'):
    with open(f'{os.path.join(GIT_DIRECTORY, "objects", obj_id)}', 'rb') as f:
        obj = f.read()

    obj_type, _, content = obj.partition(b'\x00')
    obj_type = obj_type.decode()

    if obj_type != expected_type and expected_type is not None:
        raise ValueError(f'Expected {expected_type} but got {obj_type}')
    return content