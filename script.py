cpu = input("CPU: ")
gpu = input("GPU: ")
ram = int(input("RAM (GB): "))
storage = int(input("Storage (GB): "))

score = 0

if "Ryzen 3" in cpu:
    print("AMD Ryzen 3 CPU.")
    print("Entry CPU.")
    score += 1
elif "Ryzen 5" in cpu:
    print("AMD Ryzen 5 CPU.")
    print("Mid CPU.")
    score += 2
elif "Ryzen 7" in cpu:
    print("AMD Ryzen 7 CPU.")
    print("High CPU.")
    score += 3
elif "Ryzen 9" in cpu:
    print("AMD Ryzen 9 CPU.")
    print("Enthusiast CPU.")
    score += 4
elif "i3" in cpu:
    print("Intel i3 CPU.")
    print("Entry CPU.")
    score += 1
elif "i5" in cpu:
    print("Intel i5 CPU.")
    print("Mid CPU.")
    score += 2
elif "i7" in cpu:
    print("Intel i7 CPU.")
    print("High CPU.")
    score += 3
elif "i9" in cpu:
    print("Intel i9 CPU.")
    print("Enthusiast CPU.")
    score += 4

if "RX" in gpu:
    print("Radeon RX GPU.")
    score += 2
elif "RTX" in gpu:
    print("Nvidia RTX GPU.")
    score += 3
elif "GTX" in gpu:
    print("Nvidia GTX GPU.")
    score += 1
else:
    print("Invalid GPU.")

if storage < 1:
    print("Invalid storage amount.")
if ram < 1:
    print("Invalid RAM amount.")
if 1 <= ram < 16:
    print("RAM could be upgraded. ")
    score += 1
elif ram >= 16 and ram < 32:
    print("RAM is enough. ")
    score += 2
elif ram >= 32:
    print("RAM is great. ")
    score += 3


if 1 <= storage < 500:
    print("Storage could be upgraded. ")
    score += 1
elif 1000 > storage > 499:
    print("Storage is decent. ")
    score += 2
elif storage > 999:
    print("Storage is great. ")
    score += 3

print("===== PC BUILD =====")
print("CPU:", cpu)
print("GPU:", gpu)
print("RAM:", ram, "GB")
print("Storage:", storage, "GB")
print("Score:", score, "/ 13")
if 0 < score < 5:
    print("Weak PC.")
elif 4 < score < 8:
    print("Decent PC.")
elif 7 < score < 11:
    print("Good PC.")
elif 10 < score < 13:
    print("Very Good PC.")
elif score == 13:
    print("Beast PC.")
print("====================")
