
# Let's make a PC part calculator, by inputing the existing prices of each component to calculate the cost.

cpu_price = 400
gpu_price = 700
motherboard_price = 200
ram_price = 150
storage_price = 80
power_supply_price = 70
case_price = 60

total_build = (cpu_price + gpu_price + motherboard_price + ram_price + storage_price + power_supply_price + case_price)

print("Hello, it's time to calculate how much your total build costs.")

print(f"The CPU costs {cpu_price} and the GPU costs {gpu_price}.")

print(f"Other important components like the motherboard and RAM costs {motherboard_price} and {ram_price} in total.")

print(f"The storage device, power supply, and case all costs {storage_price}, {power_supply_price}, and {case_price}.")

print(f"For the total price of the entire rig, the total comes up to {total_build} dollars before taxes.")

# This shows how arithmetic functions can calculate variables in Python.

# And now, let's do a different approach with formating and more sophisticated commands.

parts = {
    "CPU": 400,
    "GPU": 700,
    "Motherboard": 150,
    "RAM": 90,
    "Storage": 80,
    "PSU": 70,
    "Case": 60,
}

total_build = sum(parts.values())

print("PC Build Price Breakdown")
print("-" * 30)
for part, price in parts.items():
    print(f"{part:<12} ${price:>7.2f}")
print("-" * 30)
print(f"{'Total':<12} ${total_build:>7.2f}")

# It will output dashes and has its own title to show the list. This is how Python formats code when doing math.