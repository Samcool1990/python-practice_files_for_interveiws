
donutStoreDataSet = [
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0002",
		"type": "donut",
		"name": "Raised",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0003",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}
]


#Type First

# Define a custom comparison function based on topping count
def compare_by_topping_count(donut):
    return len(donut["topping"])

# Sort the array based on topping count in descending order
sorted_donuts = sorted(donutStoreDataSet, key=compare_by_topping_count, reverse=True)

# Print the sorted array
for donut in sorted_donuts:
    print(donut)

#Type second
def compare_by_topping_count(donut):
    return len(donut["topping"])


for i in range(len(donutStoreDataSet)):
    for j in range(i+1, len(donutStoreDataSet)):
        if compare_by_topping_count(donutStoreDataSet[i]) > compare_by_topping_count(donutStoreDataSet[j]):
            donutStoreDataSet[i] ,donutStoreDataSet[j] =donutStoreDataSet[j], donutStoreDataSet[i] 
print(donutStoreDataSet)

# What is dependency injection

'''
Dependency injection is a design pattern used in software development to achieve inversion of control and 
promote decoupling between different components or modules of a system. It's a technique that helps manage 
the dependencies between various parts of an application.

In the context of your work as a Backend Engineer in the IT industry, understanding dependency injection
can be crucial for writing maintainable and testable code.

Here's a simplified explanation:

Dependencies:
In software development, a "dependency" refers to an object or service that another part of the code 
relies on in order to function.

Injection:
"Injection" refers to the process of providing these dependencies to a component, rather than the 
component creating or managing them itself.

There are a few key benefits to using dependency injection:

Testability:
By injecting dependencies, you can easily replace real dependencies with mock or stub objects during 
testing. This allows you to isolate and test individual components in isolation.

Flexibility:
It allows for more flexible and modular code. You can swap out dependencies without making significant 
changes to the components using them.

Decoupling:
Components are not tightly coupled to specific implementations of their dependencies. This makes your 
code more maintainable and easier to refactor.

Inversion of Control (IoC):
With dependency injection, the control of how dependencies are created and provided is inverted. Instead 
of a component creating its dependencies, they are provided from the outside.

For example, in a web application, a database connection object could be a dependency for a service that 
interacts with the database. With dependency injection, this connection object is provided to the service, rather than the service creating it directly.

Different programming languages and frameworks have their own ways of implementing dependency injection, 
so the specific syntax and techniques can vary. If you're working with a specific language or framework, 
it's a good idea to look up the documentation or resources related to dependency injection for that 
particular technology.'''






    