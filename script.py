hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price= 0
#Loop through the prices list and add each price to the variable total_price.
for price in prices:
  total_price = total_price + price
  #After your loop, create a variable called average_price that is the total_price divided by the number of prices.You can get the number of prices by using the len() function.
average_price = total_price / len(prices)
#Print the value of average_price so the output looks like:
print("Average Haircut Price : " + str(average_price))
#Use a list comprehension to make a list called new_prices, which has each element in prices minus 5
new_prices = [price -5 for price in  prices]
#Print new_prices.
print(new_prices)
#Create a variable called total_revenue and set it to 0
total_revenue = 0
#Use a for loop to create a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
  total_revenue = prices[i] + last_week[i]
print("Total Revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print(cuts_under_30)
