# 1. Get all the users who are currently active
# 2. Get all users name the descending order of their name
# 3. delete all users starting with letter "a"
# 4. find count of active and inactive users

# # Assuming your model is defined as follows:
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)

# # 1. Get all the users who are currently active
# active_users = User.objects.filter(is_active=True)

# # 2. Get all users name in descending order of their name
# users_descending_order = User.objects.order_by('-name')

# # 3. Delete all users starting with letter "a"
# User.objects.filter(name__istartswith='a').delete()

# # 4. Find count of active and inactive users
# active_count = User.objects.filter(is_active=True).count()
# inactive_count = User.objects.filter(is_active=False).count()


# -- 1. Get all the users who are currently active
# SELECT * FROM users WHERE is_active = 1;

# -- 2. Get all users name in descending order of their name
# SELECT * FROM users ORDER BY name DESC;

# -- 3. Delete all users starting with letter "a"
# DELETE FROM users WHERE name LIKE 'a%';

# -- 4. Find count of active and inactive users
# SELECT
#     SUM(CASE WHEN is_active = 1 THEN 1 ELSE 0 END) as active_users,
#     SUM(CASE WHEN is_active = 0 THEN 1 ELSE 0 END) as inactive_users
# FROM users;


# list1= [1,2,[3,[4,[5]]]]
# flatten the list
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


# Use recursion for factorial series
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# decorator
def decorator(func):
    def wrapper(x, y):
        print("Before function execution>>>>>")
        # result =
        print("After function execution>>>")
        return func(x, y)

    return wrapper


@decorator
def add(x, y):
    return x + y


# create a new branch in git
# git checkout -b feature/new-feature

# asyncio
"""asyncio is a library to write concurrent code using the async/await syntax. 
asyncio is used as a foundation for multiple Python asynchronous frameworks that provide 
high-performance network and web-servers, database connection libraries, distributed task queues, etc."""

# MVT architecture
