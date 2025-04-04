class SortedArrayIntersection:
    """Class to find common elements between two sorted arrays."""
    
    def __init__(self, arr1, arr2):
        """Initialize with two sorted arrays."""
        self.arr1 = arr1
        self.arr2 = arr2

    def find_common_elements(self):
        """Returns an array containing numbers common to both arrays without duplicates."""
        i, j = 0, 0
        result = []
        
        while i < len(self.arr1) and j < len(self.arr2):
            if self.arr1[i] < self.arr2[j]:
                i += 1  # Move forward in arr1
            elif self.arr1[i] > self.arr2[j]:
                j += 1  # Move forward in arr2
            else:
                # Avoid duplicates in the result
                if not result or result[-1] != self.arr1[i]:
                    result.append(self.arr1[i])
                i += 1
                j += 1  # Move both pointers forward
        
        return result

# Example Usage
arr1 = [1, 2, 4, 5, 6, 8, 10]
arr2 = [2, 4, 6, 8, 10, 12, 14]

intersection_finder = SortedArrayIntersection(arr1, arr2)
print("Common Elements:", intersection_finder.find_common_elements())

