'''
You are given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. A single person can perform only one activity at a time, meaning no two activities can overlap. Your task is to determine the maximum number of activities that a person can complete in a day.

Examples:

Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: A person can perform at most four activities. The maximum set of activities that can be executed is {0, 1, 3, 4}
Input: start[] = [10, 12, 20], finish[] = [20, 25, 30]
Output: 1
Explanation: A person can perform at most one activity.
Input: start[] = [1, 3, 2, 5], finish[] = [2, 4, 3, 6]
Output: 3
Explanation: A person can perform activities 0, 1 and 3.
Constraints:
1 ≤ start.size() = finish.size() ≤ 2*105
1 ≤ start[i] ≤ finish[i] ≤ 109
'''

# Approach: Greedy Algorithm
# The greedy algorithm works by selecting the activity with the earliest finish time. We can sort the activities based on their finish times and then iterate through them to select the activities that do not overlap with the previously selected activities.
class Solution:
    def activitySelection(self, start, finish):
        n = len(start)
        if n <= 1:
            return n

        # Create a list of tuples with the start and finish times of the activities
        activities = [(start[i], finish[i]) for i in range(n)]

        # Sort the activities based on their finish times
        activities.sort(key=lambda x: x[1])

        # Initialize the count of activities and the finish time of the last selected activity
        count = 1
        last_finish = activities[0][1]

        # Iterate through the sorted activities to select the non-overlapping activities
        for i in range(1, n):
            if activities[i][0] > last_finish:
                count += 1
                last_finish = activities[i][1]

        return count