pizzas = ["peperoni", "cheese", "veggies"]
friend_pizza = pizzas[:]

pizzas.append("chicken")
friend_pizza.append("bbq")

print(f"My favorite pizzas are")


for pizza in pizzas:
    print(f"{pizza.title()}.")


print(f"\nMy friend favorite pizzas are")
for pizza in friend_pizza:
    print(f"{pizza.title()}.")



# print("\nI can eat all these pizzas in one sitting!")