numbers = []
for i in range(10):
    num = float(input("enter your number: "))
    numbers.append(num)

# میانگین
avarage = sum(numbers) / len(numbers)
print(avarage)

# واریانس
variance = sum((x - avarage)**2 for x in numbers)/len(numbers)
print(variance)

# ماکسیمم و مینیمم
minimum = min(numbers)
maximum = max(numbers)
print(minimum)
print(maximum)
