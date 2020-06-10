# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        sumArr = []
        countArr = []
        scanNode(root, 0, sumArr, countArr)
        print(sumArr)
        print(countArr)
        for i in range(0, len(sumArr)):
            sumArr[i] = float(sumArr[i])/countArr[i]
        print(sumArr)
        return sumArr

def scanNode(root, level, sumArr, countArr):
    if root is None:
        return
    if len(sumArr)>level:
        sumArr[level] = sumArr[level]+root.val
        countArr[level]=countArr[level]+1
    else:
        sumArr.append(root.val)
        countArr.append(1)
    
    scanNode(root.left, level+1, sumArr, countArr)
    scanNode(root.right, level+1, sumArr, countArr)


if __name__ == '__main__':
    root = TreeNode(3)
    l0_left = TreeNode(9)
    l0_right = TreeNode(20)
    l1_right_left = TreeNode(15)
    l1_right_right = TreeNode(7)
    l0_right.left=l1_right_left
    l0_right.right=l1_right_right
    root.left = l0_left
    root.right = l0_right
    # 
    s = Solution()
    s.averageOfLevels(root)