# from functools import wraps
# import time
# # from loguru import logger

# def main_decorator(DEBUG = "Custom Logging"):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             start = time.time()
#             result = func(*args,**kwargs)
#             end = time.time()
#             total_time = end - start
#             # logger.info(f"Total {total_time} time taken to run {__func__.__name__}")
#             print(f"Total {total_time} time taken to run {func.__name__}")
#             return result
#         return wrapper
#     return decorator


# @main_decorator("Custom Logging")
# def add(a,b):
#     return a + b
    
# print(add(5,3))



# a = (1,2,3,4)
# a = (1,2,3,4,5)



# try:
#     a = 10 % 0
# # except ZeroDivisioError as e:
# #     print(f"{ e.error}"")
    
# # else:
# #     print("Else block is running")
    
# finally:
#     print("Finally Block is running")

# class 

# class CustomException(Exception):
#     def __init__(self, amount, message, transaction_id):
#         self.amount = amount
#         self.transaction_id = transaction_id
#         self.message = message
#         print(f"{self.transaction_id} with {self.amount} has failed with {self.message}")
#         super().__init__(self.message)
        
#     def __str__(self):
#         print(self.message )
        

# amount = 100
# message = "Failed"
# transaction_id = "001"


# if amount != 100:
#     raise CustomException(amount,message , transaction_id)



# To write a Python program that searches for elements containing "metal" in the array
# without changing the datatype, you can achieve this by iterating through the set elements and checking
# if any element contains the word "metal".
 
 
# Initial array of sets
arr = [{"metal", "rock"}, {"metallica", "masti"}, {"master", "masti"}, {"blaster", "rock"}]
search = 'metal'
result = []
for i in arr:
    
    
    if search in i:
        result.append(i)
print(result)
    




