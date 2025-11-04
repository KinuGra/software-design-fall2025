arr = [1, 3, 5, 11, 12, 13, 17, 22, 25, 28]

left = 0
right = len(arr) - 1
mid = (left + right) // 2
count = 0

target = int(input("Enter the number to search for. >> "))
result = None

while left < right:
    print(f"count: {count}, left: {left}, right: {right}, mid: {mid}")

    if target == arr[mid]:
        result = mid
        break

    if target > mid:
        left = mid + 1
    else:
        right = mid - 1
    mid = (left + right) // 2
    count += 1

if result is None:
    print("Not Found")
else:
    print(result)
