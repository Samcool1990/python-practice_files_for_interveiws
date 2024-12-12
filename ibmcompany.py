list1 = [1, 1, 1, 1, 2, 3, 4, 5, 6, 2, 2, 2]

new_lst = []
for i in list1:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)

# new_lst3 = []
# new_lst2 = [new_lst3.append(i) for i in list1 if i not in new_lst3]
# print(">>>>>>", new_lst3)
d = {}

for i in list1:
    d[i] = d.get(i, 0) + 1
print(d)
# Initialize min_count with a large number
min_count = None

# Finding the minimum count
for key in d:
    if min_count is None or d[key] < min_count:
        min_count = d[key]


# from fastapi import FastAPI
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
