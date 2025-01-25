def is_valid(arr, n, k, max_pages):
    students_required = 1
    current_sum = 0

    for i in range(n):
        if arr[i] > max_pages:
            return False

        if current_sum + arr[i] > max_pages:
            students_required += 1
            current_sum = arr[i]

            if students_required > k:
                return False
        else:
            current_sum += arr[i]

    return True

def find_minimum_pages(arr, n, k):
    if n < k:
        return -1

    start = max(arr)
    end = sum(arr)
    result = float('inf')

    while start <= end:
        mid = (start + end) // 2

        if is_valid(arr, n, k, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result

# Example usage
arr1 = [12, 34, 67, 90]
k1 = 2
print(find_minimum_pages(arr1, len(arr1), k1))  # Output: 113

arr2 = [15, 17, 20]
k2 = 5
print(find_minimum_pages(arr2, len(arr2), k2))  # Output: -1

arr3 = [22, 23, 67]
k3 = 1
print(find_minimum_pages(arr3, len(arr3), k3))  # Output: 112