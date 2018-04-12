#-*- coding: utf-8 -*-

import os
import io
import json
from shutil import rmtree
from base64 import b64encode

def json_parser(data, mode):
    if mode == 'r':
        return json.loads(data)
    elif mode == 'w':
        return json.dumps(data)
    else:
        return
    
def readFile_b64encoded(path):
    fio, data = None, None
    try:
        if os.path.isfile(path):
            fio = io.FileIO(path, 'rb')
            data = fio.read()
            return b64encode(data).decode('utf-8')
    except IOError :
        raise IOError()
    finally:
        if fio: fio.close()

def join(*args):
    rtn = '' 
    for arg in args:
        rtn = os.path.join(rtn, arg)
    return rtn

def fileIO(path, mode):
    return io.FileIO(path, mode)

def mkdirs(path):
    dirname = os.path.dirname(path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
        os.chmod(dirname, 0777)

def delete(path):
    if os.path.exists(path):
        rmtree(path)