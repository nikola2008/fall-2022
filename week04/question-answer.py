
answer = input("what is the color of the sky? " )
if answer == "blue" or answer ==  "Blue":
    score = score + 1
    print ("yes")
else:
    print("I was looking for blue or Blue")
answer = input("How old is the president? ")
if answer == "104":
    print("good")
    score = score + 1 
else:
    print("nope")
answer = input("how many great lakes are there? ")
if answer == "5":
    score = score + 1
    print("Oh your smart")
else:
    print("Wrong theres 5")
print("your score is ", score)

answer =input("what kind of gas does a yamaha 125 take, mixed or unleaded? ")
if answer == "unleaded":
    print("right")
else:
    print("wrong, never fuel a 125 ")