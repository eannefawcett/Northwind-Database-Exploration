# **Northwind Database Exploration**
# Methodology
This database contains information about the selling and purchasing of food items by a fictional company, Northwind. The approach that I took in exploring the database was to ask questions with the mindset of improving the bottom line. I split my approach into two methods of attack. I first thought about ways to increase customer spending and then methods by which to reduce overhead.

# Increasing Customer Spending
This repository contains two jupyter notebooks that address the exploration into increasing customer spending. They are titled:
- Discount and Quantity
- Reorder and Discount

# Reducing Overhead
This repository contains two juypter notebooks that address the exploration into reducing overhead. They are titled:
- Product Price and OrderDetail Price
- Region Performance

# Database Access
In each juypter notebook, the database is initialized and connected to. The SQL queries are similarly included in each notebook. The database is also included in this repository.

## Discount and Quantity
The primary question being addressed in this notebook is:
**Does discount amount have a statistically significant effect on the quantity of a product in an order? If so, at what level(s) of discount?**
Ultimately, discount does have an affect on the quantity of a product in an order, at every level. The level of discount does not further impact quantity. To increase customer spending, it might be advantageous to move towards offering smaller discounts more frequently.

## Reorder and Discount
The primary question being addressed in this notebook is:
**Does reorder and shipping company affect customer spending on an order? Which shipping company is best for what level of reorder?**
Customer spending is affected by having a reorder on file. It's actually decreased. However, there is a specific reorder level that mirrors customer spending without reorder. So, it might be worth moving customers to a reorder level of 15 to increase spending to the same level as customers without a reorder on file. Additionally, shipping company 1 is the ideal company to be used for orders that have a reorder on them, followed by shipping company 3.

## Product Price and OrderDetail Price
The primary question being addressed in this notebook is:
**Do the changes in product pricing affect spending?**
The changes in product pricing do affect customer spending.

## Region Performance
The primary question being addressed in this notebook is:
**Which region is performing the best? How can we optimize performance?**
There are two regions that performed better than the rest. The regions included the cities: Phoenix, AZ, USA, Scottsdale, AZ, USA, Bellevue, WA, USA, Redmond, WA, USA, Seattle, WA, USA, Wilton, England, UK, and Neward, England, UK. And this enhanced performance actually came from two employees: Nancy Davolio in the US and Michael Suyama in the UK. When compared to the other employees, Nancy and Michael both had a higher frequency of orders that had less items in them. It might be worth offering incentives to employees to increase the number of orders that they take, or increasing client communication.
