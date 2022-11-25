def linear_search(arr, key, size):
	if (size == 0):
		return -1
	elif (arr[size - 1] == key):
		return size - 1
	else:
		return linear_search(arr, key, size - 1)

if __name__ == "__main__":
	arr = [5, 15, 6, 9, 4,20,11]
	key = 4
	size = len(arr)
	ans = linear_search(arr, key, size) # Calling the Function
	if ans != -1:
		print("The element", key, "is found at",
			ans, "index of the given array.")
	else:
		print("The element", key, "is not found.")
