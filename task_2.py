def binary_search(arr, target):
	left, right = 0, len(arr) - 1
	iterations = 0
	upper_bound = None
	
	while left <= right:
		iterations += 1
		mid = left + (right - left) // 2
		
		if arr[mid] == target:
			return (iterations, arr[mid])
		
		if arr[mid] < target:
			left = mid + 1
		else:
			upper_bound = arr[mid]
			right = mid - 1
	
	if upper_bound is None:
		upper_bound = max(arr)
		
	return (iterations, upper_bound)


if __name__ == "__main__":
	# Приклад використання
	arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
	print(binary_search(arr, 3.5))  # Виведе: (кількість ітерацій, верхню межу)
	print(binary_search(arr, 4))  # Виведе: (кількість ітерацій, верхню межу)
	print(binary_search(arr, 6.0))  # Виведе: (кількість ітерацій, макс елемент)