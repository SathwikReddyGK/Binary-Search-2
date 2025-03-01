# Solution
# // Time Complexity : O(log(n))
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : None


# // Your code here along with comments explaining your approach
# Approach is to keep searching the higher number, used binary search to find mid, check if mid is greater than its neighbours
# if not then move towards the neighbour who is greater than mid. Perform this recursively to find the solution     

def findPeakElement(nums) -> int:
        low = 0
        high = len(nums) - 1

        while low<=high:
            mid = (low+high)//2

            if ( (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1])):
                return mid
            elif mid>0 and nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                low = mid+1

        return -1

if __name__ == "__main__":
     nums = [1,2,3,1]
     print(findPeakElement(nums))