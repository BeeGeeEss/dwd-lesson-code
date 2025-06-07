# Lists Exercise

# Shopping Cart
cart = ["apples", "bananas", "bread"]

# 1. Add milk to the end of the cart.
# 2. Bananas are out of stock. Remove them.
# 3. You remembered you need eggs and they're a higher priority
#       than everything other than apples.
#       Insert eggs right after apples.
# 4. You decide to get 2 more apples, so add them.
# 5. Print out how many apples are in the cart.
# 6. Sort the cart alphabetically.
# 7. Get and print a new list with only the first 2 items.
# 8. Get and print a new list with all items EXCEPT the first one.
# 9. Print the final cart and how many items are in it.

print(cart)
cart.append("milk")
print(cart)
cart.remove("bananas")
print(cart)
cart.insert(1, "eggs")
print(cart)
cart.insert(1, "apples")
cart.insert(1, "apples")
print(cart)
print(cart.count("apples"))
(cart.sort())
print(cart)
cart.reverse()
print(cart)

first_two = cart[:2]
print(first_two)

all_except_first = cart[1:]
print(all_except_first)

print(len(cart))