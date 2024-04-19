# returns all customers from customer table
customers = Customer.objects.all()
customer1 = Customer.objects.first()

product = Product.objects.first()

# to get the element of a specific feature
orderz = Order.objects.get(customer='kamlesh')

# to filter the elements from a feature
orderp = Order.objects.filter(product__name='Ball')

# to sort the products according to the feature
productG = Product.objects.add().order_by('id')

# to reverse the ordering
productG = Product.objects.add().order_by('-id')

# to call the child info from parent
# provides all the orders by the particular customer
orders1 = customer1.order_set.all()

# to call parent from child
# this way we call the which customer ordered the first purchase
order1 = Order.objects.first()
print(order1.customer.name)

# Returns the tota count for a number of time a "Ball" was orderd for by the first customer.

ballOrders = firstCustomer.order_set.filter(product__name='Ball').count()

# Returns total count for each order
allOrders = {}

for order in firstCustomer.order_set.all():
  if order.product.name in allOrders:
    allOrders[order.product.name] += 1
  else:
    allOrders[order.product.name] = 1