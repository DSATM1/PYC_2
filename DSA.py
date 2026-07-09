"""# --- DSA Logic Building Practice ---

def find_second_largest(arr):
    """
    # 1. Find the Second Largest Element
    # Theory: Single pass approach to dynamically track largest and second largest.
    # Time Complexity: O(N) | Space Complexity: O(1)
"""
    if len(arr) < 2:
        return None
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

def move_zeros(arr):
    """
    # 2. Move Zeros to End
    # Theory: Two-pointer technique to swap non-zeros to the front in-place.
    # Time Complexity: O(N) | Space Complexity: O(1)
"""
    non_zero_idx = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_idx], arr[i] = arr[i], arr[non_zero_idx]
            non_zero_idx += 1
    return arr

def two_sum(arr, target):
    """
    # 3. Two Sum
    # Theory: Uses a dictionary (Hash Map) to store seen elements and their indices for instant lookups.
    # Time Complexity: O(N) - Loop runs once, and dictionary checks are O(1) average.
    # Space Complexity: O(N) - Worst case scenario stores every element in the dictionary.
"""
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return None

def binary_search(arr, target):
    """
    # 4. Binary Search
    # Theory: Efficiently finds the index of a target in a SORTED array by halving the search space.
    # Time Complexity: O(log N) | Space Complexity: O(1)
    # How the logic works:
    # 1. Pointers: Establish 'left' (start) and 'right' (end) pointers.
    # 2. Looping Condition: Continue as long as left <= right.
    # 3. Finding Midpoint: Calculate mid = (left + right) // 2.
    # 4. Checking Matches:
    #    - If arr[mid] == target, return mid.
    #    - If arr[mid] < target, target is in the right half (left = mid + 1).
    #    - If arr[mid] > target, target is in the left half (right = mid - 1).
    # 5. Not Found: Return -1 if the loop finishes without finding the target.
"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    # """
    # 5. Recursive Binary Search
    # Theory: Achieves O(log N) time by calling itself with updated boundaries.
    # Time Complexity: O(log N) | Space Complexity: O(log N) - due to call stack memory.
"""
    if left > right:
        return -1
        
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

if __name__ == "__main__":
    print("--- Testing DSA Functions ---")
    
    # Test 1: Find Second Largest
    print("1. Find Second Largest:")
    print(f"   Standard: {find_second_largest([10, 5, 20, 8, 12])}")
    print(f"   All same: {find_second_largest([7, 7, 7])}") # Edge case: Identical elements
    print(f"   Too short: {find_second_largest([5])}") # Edge case: < 2 elements
    print(f"   Negatives: {find_second_largest([-10, -5, -20])}") # Edge case: Negative numbers
    
    # Test 2: Move Zeros
    print("\n2. Move Zeros:")
    print(f"   Standard: {move_zeros([0, 1, 0, 3, 12])}")
    print(f"   All zeros: {move_zeros([0, 0, 0])}") # Edge case: Only zeros
    print(f"   No zeros: {move_zeros([1, 2, 3])}") # Edge case: No zeros
    print(f"   Empty: {move_zeros([])}") # Edge case: Empty list
    
    # Test 3: Two Sum
    print("\n3. Two Sum:")
    print(f"   Standard: {two_sum([2, 7, 11, 15], 9)}")
    print(f"   No match: {two_sum([1, 2, 3], 10)}") # Edge case: No valid pair
    print(f"   Negatives: {two_sum([-3, 4, 3, 90], 0)}") # Edge case: Sums to zero with negatives
    print(f"   Empty: {two_sum([], 5)}") # Edge case: Empty list
    
    # Test 4: Binary Search
    print("\n4. Binary Search:")
    print(f"   Standard: {binary_search([1, 3, 5, 7, 9, 11], 7)}")
    print(f"   Not found: {binary_search([1, 3, 5, 7, 9, 11], 4)}") # Edge case: Target missing
    print(f"   Empty: {binary_search([], 5)}") # Edge case: Empty list

    # Test 5: Recursive Binary Search
    print("\n5. Recursive Binary Search:")
    arr5 = [1, 3, 5, 7, 9, 11]
    print(f"   Standard: {binary_search_recursive(arr5, 7, 0, len(arr5) - 1)}")
    print(f"   Not found: {binary_search_recursive(arr5, 4, 0, len(arr5) - 1)}") # Edge case: Target missing
    print(f"   Empty: {binary_search_recursive([], 5, 0, -1)}") # Edge case: Empty list
"""
