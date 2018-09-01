

burgers = ["beef", "chicken", "beans"]
toppings = ["cheese", "eggs", "beans" "spam"]

meals = []
for meals in [(burger, topping) for burger in burgers]:
    print(topping)
    print(meals)
print("="*20)
