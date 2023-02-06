pizzas = ["marguerita", "mutzarella", "gorgonzolla"]
friends_pizza = pizzas[:]

pizzas.append('ravioli')
friends_pizza.append('Alho e oleo')

for pizza in pizzas:
    print(pizza.title())
print('\n')
for sabores in friends_pizza:
    print(sabores.title())
