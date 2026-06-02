# Take numbers from the user
# 1. User cannot enter a value less than 10, more than 100
# 2. You calculate the total & average of the numbers entered 
# 3. stop when the sum is greater than 200 or average is more than 75
#    tell them in how many steps they achieved this.

total = 0
avg = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    if num >= 100 or num <= 10:
        print("The  number cannot be > 100 & < 10")
        continue

    total += num
    count += 1
    avg = total / count

    if total > 200 or avg > 75:
        break

    print(f"Sum: {total}\t Avg: {avg}\t Count: {count}")

print(f"You acheived a Sum: {total} and Average: {avg} in {count} steps")