import numpy as np
import pandas as pd

df = pd.read_csv('C:\\Users\\prave\\OneDrive\\Desktop\\Python\\FIX_Messages.txt',names=['Fix','New_Order','Product_Name',
'Buy_Sell','Quantity','Order_Types','Force_Orders','Stock_Types','Client_ID','Price'], sep='|')

print('\n'"Stock types - Average, Sum, Min, Max in Quantity and Price")
print('---------------------------------------------------------------')
#Avg stock types
print(df.groupby("Stock_Types").agg({"Quantity":["mean","sum","min","max"],"Price":["mean","sum","min","max"]}))

print('\n'"Top 5 Large quantity Orders")
print('---------------------------------------------------------------')
#top 5 quantities
print(df.nlargest(5, "Quantity"))

print('\n'"Top 5 least quantity Orders")
print('---------------------------------------------------------------')
#top 5 least quantity orders
print(df.nsmallest(5, "Quantity"))

print('\n'"Most popular order types")
print('---------------------------------------------------------------')
#Most popular order types
print(df.groupby("Order_Types").size().sort_values(ascending=False))

print('\n'"Number of unique Client IDs")
print('---------------------------------------------------------------')
#no of unique clients
print(df.Client_ID.nunique())

print('\n'"Client ID and its Sum")
print('---------------------------------------------------------------')
#clients and sum of amounts
print(df.groupby('Client_ID')['Price'].sum().sort_values(ascending=False))

print('\n'"List of products per clients")
print('---------------------------------------------------------------')

#List of products per client_ID
print(df.groupby('Client_ID').apply(lambda x: ','.join(x.Product_Name)))

print('\n'"Order Types and its average Quantity")
print('---------------------------------------------------------------')

#Order_Types and its average Quantity
print(df.groupby('Order_Types')["Quantity"].mean().sort_values(ascending=False))