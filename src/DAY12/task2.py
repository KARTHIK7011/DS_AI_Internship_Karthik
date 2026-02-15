import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
trend_sales = [200, 250, 300, 280, 320, 350]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(months, trend_sales, marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()


plt.show()



