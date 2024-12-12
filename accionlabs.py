
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
Dependency Injection(DI) is a software engineering technique for defining the dependencies among objects. 
Basically, the process of supplying a resource that a given piece of code requires. The required resource is 
called dependency.There are various classes and objects defined when writing code. Most of the time, these 
classes depend on other classes in order to fulfill their intended purpose. These classes, or better-used word 
Components, knows the resources it needs and how to get them. DI handles defining these dependent resources 
and provides ways to instantiate or create them externally. Dependency Container is used to implement this 
behavior and holds the map of dependencies for the components. If object A depends on object B, object A must
not create import object B directly. Instead of this, object A must provide a way for injecting object B. The
 responsibility of object creation and dependency injection are delegated to external code.'''



    