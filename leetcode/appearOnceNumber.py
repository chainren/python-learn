"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明： 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
    输入: [2,2,1]
    输出: 1

示例 2:
    输入: [4,1,2,1,2]
    输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 使用hash算法
def appear_once_number(nums):
    map = dict()
    for i in nums:
        if map.get(i) is not None:
            map[i] = map[i]+1
        else:
            map[i] = 1
    
    for k,v in map.items():
        if v==1:
            return k    
    return -1 


# 使用异或算法。
# 0^0=0, 0^1=1, 1^0=1, 1^1=0
def appear_once_number1(nums):
    res = 0
    for i in nums:
        res^=i
    return res


nums = [3, 2, 2, 4, 3]
once_number = appear_once_number(nums)
print(once_number)

once_number = appear_once_number1(nums)
print(once_number)