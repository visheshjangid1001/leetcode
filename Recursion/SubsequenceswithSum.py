def backtrack(nums, target, index, total, subset, result):
    # Base case
    if total == target:
        result.append(subset.copy())
        return
    if total > target or index >= len(nums):
        return

    # Include current element
    subset.append(nums[index])
    backtrack(nums, target, index + 1, total + nums[index], subset, result)

    # Backtrack (remove last element)
    subset.pop()

    # Exclude current element
    backtrack(nums, target, index + 1, total, subset, result)


def find_subsets(nums, target):
    result = []
    backtrack(nums, target, 0, 0, [], result)
    return result


# Example usage
nums = [2, 3, 5]
target = 5
print(find_subsets(nums, target))