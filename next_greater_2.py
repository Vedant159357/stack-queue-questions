class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [-1] * n

        st = []

        for i in range(2 * n - 1, -1, -1):
            ind = i % n

            currEle = nums[ind]

            while st and st[-1] <= currEle:
                st.pop()

            if i < n:
                if st:
                    ans[ind] = st[-1]

            st.append(currEle)

        return ans
