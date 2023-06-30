import pandas as pd

customer_data = pd.read_json('dim_customer.json')
product_invoice_data = pd.read_csv('fct_invoice.csv')

# --------- 1. NO. OF UNIQUE CUSTOMERS ---------

unique_customer_ids = (pd.unique(customer_data['id']) != "")
# print(unique_customer_ids.sum())


# --------- 2. PRODUCT CATEGORIES ---------
product_category_list = pd.unique(product_invoice_data['category'])
num_product_categories = (product_category_list != "").sum()

# print(product_category_list, num_product_categories)

# --------- 3. POPULAR PAYMENT METHOD ---------
payment_method_list = product_invoice_data['payment_method'].count()

print(payment_method_list)