from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Cheruiyot")
c2 = Customer("Lennie")
coffee1 = Coffee("Americano")
coffee2 = Coffee("Cappuccino")

c1.create_order(coffee1, 5.0)
c1.create_order(coffee2, 6.0)
c2.create_order(coffee1, 7.0)

print(coffee1.customers())  
print(coffee1.average_price())
print(Customer.most_aficionado(coffee1).name)