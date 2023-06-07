def moving_average(nums: list, size: int) -> list:
    window_sum = sum(nums[:size])
    result = [window_sum / size]
    for i in range(len(nums) - size):
        window_sum -= nums[i]
        window_sum += nums[i + size]
        result.append(window_sum / size)
    return result


nums = [1, 2, 3, 4, 5]
print(moving_average(nums, 1))
