# PREREQUISITS
## Install Node
    - https://nodejs.org/en/learn/getting-started/how-to-install-nodejs
    - https://www.geeksforgeeks.org/installation-of-node-js-on-windows/

# RUN THE "REMOTE" SERVICES

Run these in separate terminals
```
node invoices.js
```
```
node customers.js
```

# CONNECT TO THE "REMOTE" SERVICES

Customer service can be reached at GET http://localhost:9090

Invoice service can be reached at GET http://localhost:9092

# WHAT THE "REMOTE" SERVICES RETURN

The Customer service returns data about customers. For Example:

```
{
    "customers": [
        {
            "ID": 0,
            "name": "Alice",
            "surname": "Klark"
        },
        ...
    ]
}
```

where ID is the unique identifier and name and surname are the name and the surname of our customer.

The Invoice service returns data about invoices. For exampls:

```
{
    "invoices": [
        {
            "ID": 0,
            "customerId": 0,
            "amount": 12
        },
        ...
    ]
}
```

where ID is the unique identifier, customer ID is the customer ID, which is loosely coupled with the Customer data, and the amount is the amount that our customer has been charged.

If we assume that Alice Klark has one invoice only then her total amount spent would be 12.

# THE CHALLENGE

Write an application that calculates which customer spent the most money in our store and displays his/her name, surname, and total amount spent.

# EXTRA POINTS

What is the best test strategy for an application like this? The team with the best test strategy will be awarded 5 extra points!

Tip: No, "I will let QA decide" is not an option

# EVEN MORE EXTRA POINTS

The team with highest test coverage will be awarded 5 extra points!

# HOW TO RUN

```
python solution.py
```

# HOW TO RUN TESTS

```
pytest
```
