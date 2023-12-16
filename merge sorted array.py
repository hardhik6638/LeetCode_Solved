def countSubarrays(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        max_element = nums[i]
        freq = 0

        for j in range(i, n):
            max_element = max(max_element, nums[j])

            if max_element == nums[j]:
                freq += 1

            if freq >= k:
                count += 1

    return count

# Example usage:
nums = [2, 1, 4, 3]
k = 2
result = countSubarrays(nums, k)
print("Number of subarrays where max element appears at least", k, "times:", result)
