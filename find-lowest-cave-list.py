def generate_power_2_list(nums):
    return list(map(lambda num: num**2, nums))


class Solution:
    def find_lowest(self, nums):
        first_index = 0
        last_index = len(nums) - 1
        while last_index - first_index > 1:
            bound_len = last_index - first_index
            one_third_index = first_index + round(bound_len / 3)
            two_third_index = first_index + round(bound_len * 2 / 3)
            if nums[one_third_index] > nums[two_third_index]:
                first_index = one_third_index
            else:
                last_index = two_third_index
        return last_index


nums = [-3, -2, -2, -1, 0, 1, 2, 3]

nums = generate_power_2_list(nums)

r = Solution().find_lowest(nums)
print(r)
