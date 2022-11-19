# Problem 1
for x in range(1,5):
 print(x)
# need colon 

# Problem 2
names = ("dogs", "cats")
numbers = []
for name in names:
    countTEXT = input(f"How many {name}?")
    count = float(countTEXT)
    numbers.append(count)
    
print(f"Minimum: {min(numbers)}")
print(f"Maximum {max(numbers)}")

#In the for loop names should have been name 

#Problem 3
t1 = ["the", "quick", "brown", "fox""jumped", "over", "the", "lazy", "dog"]
print(t1)
for i in t1:
    print(i)

#Remove the circle bracet and put a square, put brackets around "t1", put brackets around "i"