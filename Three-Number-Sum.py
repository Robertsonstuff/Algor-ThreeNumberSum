# how to get sum three numbers in the selected array to add up to the target sum.
# O(n^2) time | O(n) space


def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    # so far we have sorted our array and created an empty array called 'triplets'
    for i in range(len(array) - 2):
        #print(i)
        left =  i + 1
        right = len(array) -1
        # this loop will iterate through the array, setting markers left and right. 'left' will start at the start and iterate through the length of the array up by 1 increment each time.
        # the right marker will stay at the last index as it has not been told to do otherwise.
        print(array)
        while left < right:
            currentSum = array[i] + array[left] + array[right]
# meaning: keep looping if the following is true (-8 + -6 + 12) = -2. Is left less than right? Yes it is, keep going to the if statement. [-8, -6, 1, 2, 3, 5, 6, 12] 
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
# if -2 == 0 append the numbers that reached the answer to the triplets list. Move the index of the left marker to the right and the right marker to the left. 
            elif currentSum < targetSum:
                left += 1
# otherwise, if the -2 < 0, index the left marker to the right to get a larger answer. 
            elif currentSum > targetSum:
                right -= 1
# otherwise, if the -2 > 0, index the right marker to the left to get a smaller answer.
# Once the array has gone through both of the loops - both moving the markers back and forth in the while loop AND the currentSum has moved through the array in the for loop. The completed array with print with all of the triplets that reached the targetSum 
    return triplets

blah = threeNumberSum([12,3,1,2,-6,5,-8,6], 0)
print(blah)