import pandas as pd

customer_data = pd.read_json('dim_customer.json')
product_invoice_data = pd.read_csv('fct_invoice.csv')
# print(product_invoice_data)

# --------- 1. NO. OF UNIQUE CUSTOMERS ---------

unique_customer_ids = (pd.unique(customer_data['id']) != "")
# print(unique_customer_ids.sum())
freq_customers = customer_data['id']
# print(freq_customers)


# --------- 2. PRODUCT CATEGORIES ---------
product_category_list = pd.unique(product_invoice_data['category'])
num_product_categories = (product_category_list != "").sum()

# print(product_category_list, num_product_categories)

# --------- 3. POPULAR PAYMENT METHOD ---------
payment_method_list = product_invoice_data['payment_method'].value_counts()
# print(payment_method_list)


# --------- 4. 3 POPULAR CATEGORIES ---------

categ_quant_count = product_invoice_data[['quantity', 'category']].value_counts().reset_index(name='count')
categ_quant_count['total_sales'] = categ_quant_count['quantity'] * categ_quant_count['count']
output_df = categ_quant_count[['category', 'total_sales']]
print(output_df.groupby('category').sum())
