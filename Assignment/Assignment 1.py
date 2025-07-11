# =====================================
# DYNAMIC PRICING MANAGER 
# =====================================

# -------------------------------
# SECTION 1: INPUT PRODUCT DETAILS
# -------------------------------

product_id = input("Enter Product ID (just a number): ")
print("You entered:", product_id)
product_id = int(product_id)
product_name = input("Enter Product Name: ")
base_price = float(input("Enter Base Price (₹): "))
discount_percentage = float(input("Enter Discount Percentage: "))

# -------------------------------
# SECTION 2: INPUT MARKET INFORMATION
# -------------------------------

competitor_price = float(input("Enter Competitor's Price (₹): "))
pricing_tier = input("Enter Pricing Tier (e.g., Budget, Standard, Premium): ")
tags = input("Enter Product Tags (comma-separated): ").split(',')

# -------------------------------
# SECTION 3: CALCULATIONS
# -------------------------------

# Calculate discount amount
discount_amount = (discount_percentage / 100) * base_price

# Calculate final sale price
sale_price = base_price - discount_amount

# Calculate difference from competitor price
price_difference = sale_price - competitor_price

# -------------------------------
# SECTION 4: FORMATTED OUTPUT
# -------------------------------

print("\n===================================")
print("         DYNAMIC PRICING REPORT         ")
print("===================================")

# 1. Comma Separation (sep=',')
print("\n1. Using Comma Separation (sep=','):")
print("Product ID, Name, Base Price:", product_id, product_name, base_price, sep=",")

# 2. Percentage Formatting (%)
print("\n2. Using Percentage Formatting:")
print("Discount Applied: %.2f%%" % discount_percentage)

# 3. f-strings
print("\n3. Using f-strings:")
print(f"Base Price         : ₹{base_price}")
print(f"Discount Amount    : ₹{discount_amount}")
print(f"Sale Price         : ₹{sale_price}")
print(f"Competitor Price   : ₹{competitor_price}")
print(f"Price Difference   : ₹{price_difference}")
print(f"Pricing Tier       : {pricing_tier}")
print(f"Product Tag 1      : {tags[0]}")
print(f"Product Tag 2      : {tags[1]}")
print(f"Product Tag 3      : {tags[2]}")

# 4. .format() method
print("\n4. Using .format() method:")
print("Product Summary: {} | Final Price: ₹{:.2f} | Tier: {}".format(
    product_name, sale_price, pricing_tier))

# -------------------------------
# END OF PROGRAM
# -------------------------------
