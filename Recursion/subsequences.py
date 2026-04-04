def subsets(nums):
    result = []
    solve(nums, 0, [], result)  # solve is called here
    return result


def solve(nums, index, subset, result):
    if index >= len(nums):
        result.append(subset.copy())
        return

    subset.append(nums[index])
    solve(nums, index + 1, subset, result)

    subset.pop()
    solve(nums, index + 1, subset, result)


# Calling function AFTER both are defined
print(subsets([1, 2, 3]))
        