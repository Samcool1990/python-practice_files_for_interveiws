#Basic structure for FastAPI i
from fastapi import Fastapi
from pydantic import Basemodel
from typing import Optional, List
# from sqlaclhemy import CreateEngine

app = Fastapi()

class request_body(Basemodel):
    id: int
    name: str
    desc: str 

#database.py
# database_str = {'host', 'port', 'user', 'pass'}
# CreateEngine(database_str,)
# session(CreateEngine)

def get_db(session):
    try:
        session.db.connect()
    except:
        return {'message': 'failed'}
    finally:
        session.db.close()

@app.get('/index', Depends = get_db)
def func1(params: request_body):
    #business logic
    db  = get_db()
    db.execute()
    return {'status':200, 'message':'Success'}


#Decorator
def decorator(func):
    def wrapper(x,y):
        #add logic
        # print()
        print(f"{func.__name__} is running with arguments {x} and {y}")
        return func(x,y)
    return wrapper
    
@decorator
def add(x,y):
    return x + y
    
print(add(5,3))



#Custom exception using decorator
#Multithread & Multiprocessing when to use in reall life?
