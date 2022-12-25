def find_2_closest(nums, target):
    def get_delta(first_index, last_index):
        return abs(target - (nums[first_index] + nums[last_index]))

    first_index, last_index = 0, len(nums) - 1
    delta = float("inf")
    while first_index < last_index:
        current_delta = get_delta(first_index, last_index)
        if current_delta < delta:
            delta = current_delta
            first, last = nums[first_index], nums[last_index]

        first_delta = get_delta(first_index + 1, last_index)
        last_delta = get_delta(first_index, last_index - 1)
        if first_delta > last_delta:
            last_index -= 1
        else:
            first_index += 1

    return first, last


assert find_2_closest([10, 22, 28, 29, 30, 40], 54) == (22, 30)
assert find_2_closest([1, 3, 4, 7, 10], 15) == (4, 10)
