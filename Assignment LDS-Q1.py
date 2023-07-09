def find_pairs(arr, target_sum):
    pairs = []
    num_dict = {}

    for num in arr:
        complement = target_sum - num
        if complement in num_dict:
            pairs.append((num, complement))
        num_dict[num] = True

    return pairs

# Get array from user
arr = input("Enter the array of integers (space-separated): ").split()
arr = [int(num) for num in arr]

# Get target sum from user
target_sum = int(input("Enter the target sum: "))

result = find_pairs(arr, target_sum)
print(f"Pairs in the array with sum {target_sum}:")
for pair in result:
    print(pair)