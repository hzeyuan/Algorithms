# 寻找局部最大的序列
def findMaxSubArray(nums,l,mid,r):
    # print(l,mid,r)
    left_suffix_max_sum = right_prefix_max_sum = 0
    sum = 0
    for i in range(mid, l-1, -1):
        sum += nums[i]
        left_suffix_max_sum = max(left_suffix_max_sum, sum)
    sum = 0
    for i in range(mid + 1, r+1):
        sum += nums[i]
        right_prefix_max_sum = max(right_prefix_max_sum, sum)
    # print(l, mid, r)
    cross_max_sum = left_suffix_max_sum + right_prefix_max_sum
    return max(cross_max_sum, left_suffix_max_sum, right_prefix_max_sum)

def maxSubArray(nums,l,r):
    if l >= r:
        return nums[l]
    mid = (l + r) // 2
    maxSubArray(nums, l, mid)
    maxSubArray(nums, mid + 1, r)
    return findMaxSubArray(nums,l,mid,r)

print(maxSubArray([4,-3,5,-2,-1,2,6,-2],0,7))
print(maxSubArray([1,2,3,4,5],0,4))

