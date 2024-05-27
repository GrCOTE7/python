
  # euro_price_str = ''.join(filter(str.isdigit, price.split()[2]))

# print(price.split()[2])

price='Prix : 20â‚¬'
# print(list(filter(str.isdigit, price)))
print(''.join(ch for ch in price if ch.isdigit()))

