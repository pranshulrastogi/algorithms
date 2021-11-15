"""
Problem link: https://leetcode.com/problems/daily-temperatures/
Difficulty: Medium
"""


def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    l = len(temperatures)
    ans = [0 for i in range(l)]
    st = []
    for i, ele in enumerate(temperatures):
        if not st:
            st.append((i, ele))

        else:
            if st[-1][1] >= ele:
                st.append((i, ele))

            else:
                while st and st[-1][1] < ele:
                    # its a warmer day
                    ans[st[-1][0]] = i - st[-1][0]
                    st.pop()
                st.append((i, ele))
    return ans
