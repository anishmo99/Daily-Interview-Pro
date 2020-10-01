def findRange(nums):
    n = len(nums)
    if n <= 1:
        return 0
    start = 0
    end = n - 1

    # find first index violating ascending order
    while start < n - 1 and nums[start] <= nums[start+1]:
        start += 1

    if start == n - 1:
        # already sorted
        return 0

    # find first index violating descending order in reverse
    while end > 0 and nums[end] >= nums[end-1]:
        end -= 1

    if start == 0 and end == n - 1:
        return n

    # find min and max of our temporary window
    windowMax = max(nums[start:end+1])
    windowMin = min(nums[start:end+1])

    # extend the window
    while start > 0 and nums[start-1] > windowMin:
        start -= 1

    while end < n -1 and nums[end+1] < windowMax:
        end += 1

    return [start, end]

print(findRange([1, 7, 9, 5, 7, 8, 10]))