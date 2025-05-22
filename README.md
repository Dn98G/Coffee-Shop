## Coffee Shop Project
The object-oriented programming in this Python assignment represents a coffee shop. Three key sections are included:: `Customer`, `Coffee`, and `Order`.

## Relationships

- A Customer can make one order. (one-to-one)
- A Coffee can have many Orders. (one-to-many)
- An Order connects one Customer and one Coffee (many-to-many).

## Files

- `customer.py` – Class of customers with order modalities and identity checks
- `coffee.py` – Tracking order and standard pricing for coffee class
- `order.py` – Linking buyers and coffees through order classes
- `debug.py` – To actively examine the code

## Features

- Generate coffee and clients
- Make an order with a specified quantity
- Get all the order from a customer for a coffee
- Determine who paid the most for a certain coffee