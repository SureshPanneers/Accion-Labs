def common_elements(arr1, arr2):
    """Find common elements between two sorted arrays without duplicates."""
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1  # Move forward in arr1
        elif arr1[i] > arr2[j]:
            j += 1  # Move forward in arr2
        else:
            # Avoid duplicates in the result
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1  # Move both pointers forward
            
    return result

# Example Usage
arr1 = [1, 2, 4, 5, 6, 8, 10]
arr2 = [2, 4, 6, 8, 10, 12, 14]

print("Common Elements:", common_elements(arr1, arr2))
