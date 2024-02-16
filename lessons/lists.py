"""Practice with lists!"""

#Initlialize an empty list
grocery_list: list[str] = list() # list constructor

print(grocery_list)

# Add item ot a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# Create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("pop")
print(grocery_list2)

def display(a: list[str]) -> None:
    list_idx: int = 0
    list_length: int = len(a) - 1
    while list_idx <= list_length:
        print(a[list_idx])
        list_idx += 1

display(["bananas", "milk"])

def create(a: str,b: str) -> list[str]:
    created_list: list[str] = [a, b]
    return created_list

print(create("j", "g"))