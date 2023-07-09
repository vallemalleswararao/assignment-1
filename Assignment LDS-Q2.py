def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Get array from user
arr = input("Enter the array of elements (space-separated): ").split()
arr = [int(num) for num in arr]

print("Original array:", arr)
reverse_array(arr)
print("Reversed array:", arr)