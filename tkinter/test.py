from datetime import date

today = date.today()

# mm/dd/y
d3 = today.strftime("%d%b%Y")
print("d3 =", d3)
