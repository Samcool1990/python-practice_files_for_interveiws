list1 =[1,1,1,1,2,3,4,5,6,2,2,2]

new_lst = []
for i in list1:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)


d = {}

for i in list1:
    d[i] = d.get(i,0) + 1
print(d)

from fastapi import FastAPI
# from 
# # schema: 
# class schemName(Basemodel):
#     id : int
#     name:  str
##mysql
# database connection
# db = SessionLocal()
# app = Fastapi()

# @app.get('v1/employee/{empid}')
# def get_employee_id(empid: int):
#     try:
#         result = db.query.filter_by(schemName.id ==empid )

#         return {'message': 200, "body": result}       
#     except Ellipsis as e:
#         print(e)
#     finally:
#         db.close()

 


