# AGILE & RESAPI

# 4. What are Idempotent methods? How is it relevant in RESTful web services domain?
# The meaning of idempotent is that even after calling a single request multiple times, 
# the outcome of the request should be the same. While designing REST APIs, we need to keep in 
# mind to develop idempotent APIs. This is because the consumers can write client-side code which can 
# result in duplicate requests intentionally or not. Hence, fault-tolerant APIs need to be designed so 
# that they do not result in erroneous responses.

# Idempotent methods ensure that the responses to a request if called once or ten times or more 
# than that remain the same. This is equivalent to adding any number with 0.
# REST provides idempotent methods automatically. GET, PUT, DELETE, HEAD, OPTIONS, and TRACE are 
# the idempotent HTTP methods. POST is not idempotent.
# POST is not idempotent because POST APIs are usually used for creating a new resource on the server. 
# While calling POST methods N times, there will be N new resources. This does not result in the same 
# outcome at a time.
# Methods like GET, OPTIONS, TRACE, and HEAD are idempotent because they do not change the state of 
# resources on the server. They are meant for resource retrieval whenever called. They do not result 
# in write operations on the server thereby making it idempotent.
# PUT methods are generally used for updating the state of resources. If you call PUT methods N times, 
# the first request updates the resource and the subsequent requests will be overwriting the same resource again and again without changing anything. Hence, PUT methods are idempotent.
# DELETE methods are said to be idempotent because when calling them for N times, the first request 
# results in successful deletion (Status Code 200), and the next subsequent requests result in nothing - 
# Status Code 204. The response is different, but there is no change of resources on the server-side.
# However, if you are attempting to delete the resource present, at last, every time you hit the API, 
# such as the request DELETE /user/last which deletes the last user record, then calling the request N 
# times would delete N resources on the server. This does not make DELETE idempotent. In such cases, 
# as part of good practices, it is advisable to use POST requests.


# how to you consider user stories for a particular sprint
# You can use feedback and data to refine your user stories before, during, and after your sprint planning 
# and delivery, by using techniques such as surveys, interviews, prototypes, demos, reviews, retrospectives,
# and metrics

