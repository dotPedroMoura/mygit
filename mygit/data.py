import hashlib
from pathlib import Path

GIT_DIRECTORY = '.mygit'
IGNORE_DIRECTORY = '.mygitignore'

def init():
    (Path(GIT_DIRECTORY) / 'objects').mkdir(parents=True, exist_ok=False)
    Path(IGNORE_DIRECTORY).touch()
    Path(IGNORE_DIRECTORY).write_text("*.mygitignore/")
    print(f'Initialized empty mygit repository in {Path(GIT_DIRECTORY).absolute()}')

def hash_object(data, obj_type ='blob'):
    obj = obj_type.encode() + b'\x00' + data
    obj_id = hashlib.sha1(obj).hexdigest()

    (Path('.') / GIT_DIRECTORY / 'objects' / obj_id).write_bytes(obj)

    return obj_id

def get_object(obj_id, expected_type ='blob'):
    obj = (Path('.') / GIT_DIRECTORY / 'objects' / obj_id).read_bytes()

    obj_type, _, content = obj.partition(b'\x00')
    obj_type = obj_type.decode()

    if obj_type != expected_type and expected_type is not None:
        raise ValueError(f'Expected {expected_type} but got {obj_type}')
    return content
