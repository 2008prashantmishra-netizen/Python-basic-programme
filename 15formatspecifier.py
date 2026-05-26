# format specifiers = {values:flags} format a vallue based 
#                    on what flags are intrested
'''
# ==============================
# PYTHON FORMAT SPECIFIERS NOTES
# ==============================

# Syntax
# f"{value:specifier}"


# ------------------------------
# .2f  -> Float with 2 decimals
# ------------------------------
price = 99.456
print(f"{price:.2f}")     # 99.46


# ------------------------------
# d -> Integer
# ------------------------------
num = 25
print(f"{num:d}")         # 25


# ------------------------------
# e -> Scientific notation
# ------------------------------
num = 1234
print(f"{num:e}")         # 1.234000e+03


# ------------------------------
# % -> Percentage
# ------------------------------
score = 0.85
print(f"{score:%}")       # 85.000000%

print(f"{score:.0%}")     # 85%


# ------------------------------
# , -> Comma separator
# ------------------------------
money = 1000000
print(f"{money:,}")       # 1,000,000


# ------------------------------
# > -> Right align
# ------------------------------
name = "Python"
print(f"{name:>10}")      # "    Python"


# ------------------------------
# < -> Left align
# ------------------------------
print(f"{name:<10}")      # "Python    "


# ------------------------------
# ^ -> Center align
# ------------------------------
print(f"{name:^10}")      # "  Python  "


# ------------------------------
# 0> -> Fill with zeros
# ------------------------------
num = 42
print(f"{num:0>5}")       # 00042


# ------------------------------
# + -> Show positive/negative sign
# ------------------------------
num = 10
print(f"{num:+}")         # +10


# ------------------------------
# Combination Example
# ------------------------------
price = 1234.5678
print(f"{price:,.2f}")    # 1,234.57'''

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

# for spaces
'''print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")'''

