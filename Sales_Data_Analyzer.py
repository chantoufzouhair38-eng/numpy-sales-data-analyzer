
import numpy as np

products = np.array([
    "Laptop",
    "Phone",
    "Tablet",
    "Headphones",
    "Keyboard"
])

# Rows = products
# Columns = January, February, March, April
sales = np.array([
    [120, 150, 130, 170],
    [200, 180, 220, 250],
    [90, 100, 110, 95],
    [300, 280, 320, 350],
    [150, 160, 140, 180]
])

prices = np.array([800, 500, 300, 50, 40])
print("="*50)
print("          SALES DATA ANALYZER              ")
print("="*50)
print("TOTAL UNITS SOLD:")
total_unit=np.sum(sales,axis=1)
for i in range(len(products)):
    print(f"{products[i]}:{total_unit[i]} units")

total_revenue=total_unit*prices
print("\nTOTAL REVENUE PER PRODUCT:")
for i in range(len(products)):
    print(f"{products[i]}:{total_revenue[i]}")

print("\nBEST-SELLING PRODUCT:")   
best_selling=np.argmax(total_revenue)
print(f"Product:{products[best_selling]}")
print(f"Totale unit sold:{total_unit[best_selling]}")
print("MONTHLY SALES")
totale_unit_per_month=np.sum(sales,axis=0)
months=np.array(["January","February","March","Aprile"])
for i in range(len(months)):
    print(f"{months[i]}:{totale_unit_per_month[i]}")
print("\nPRODUCTS WITH MORE THAN 600 UNITS SOLD")
more_600=products[total_unit>=600]
for i in range(len(more_600)):
    print(f"{more_600[i]}")  

print("\nAVERAGE MONTHLY SALES") 
avrege_monts=np.mean(sales,axis=1)
for i in  range(len(products)):
    print(f"{products[i]}:{avrege_monts[i]} units")     

print("\nSALES RANKING")
ranking=np.argsort(total_unit)[::-1]
for position, i in enumerate(ranking, start=1):
    print(f"{position}. {products[i]} - {total_unit[i]} units")

print("\nMONTH WITH THE HIGHEST TOTAL SALES:")
best_month_index = np.argmax(totale_unit_per_month)

print(f"Month: {months[best_month_index]}")
print(f"Total units sold: {totale_unit_per_month[best_month_index]} units")

print("\n" + "=" * 50)
print("          ANALYSIS COMPLETED")
print("=" * 50)

