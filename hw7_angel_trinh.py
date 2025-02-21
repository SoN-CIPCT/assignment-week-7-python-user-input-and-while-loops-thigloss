pizza_orders=["combo","pineapple bacon", "margherita","hawaiian","prosciutto"]
finished_pizza=[]

while pizza_orders:
    current_pizza=pizza_orders.pop()
    print(f"Your {current_pizza.title()} pizza pie is finished!")
    finished_pizza.append(current_pizza)
for pizza in finished_pizza:
    print(f"The pizza {pizza.title()} was made.")