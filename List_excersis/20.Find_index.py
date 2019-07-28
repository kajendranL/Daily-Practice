print('''Write a Python program access the index of a list.''')

print()

def find_index(nums):

    for num_index, num_val in enumerate(nums):
        print("The number",num_val, "is at index of", num_index)


nums1 = [5, 15, 35, 8, 98]
print(find_index(nums1))
