def get_total(price, qty=1, tax= 0.02, discount=0):
    subtotal = price * qty * (1 - discount)
    print(subtotal * (1 + tax))
    
get_total(4.99, 5, 0.015, 0.2)    
get_total(price=4.99, qty=5, tax=0.01, discount=0.6) 
# Com keywords os argumentos podem ser passados em qualquer ordem.
get_total(price=3.55, discount = 0.1, qty=2, tax=0.05)