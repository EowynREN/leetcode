class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        #hashmap/hashtable
        self.nums = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        #record distinct num and count the duplicates

        if number in self.nums:
            self.nums[number] = 2
        else:
            self.nums[number] = 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        for num1 in self.nums.keys():
            array = self.nums
            #num2 = value - num1

            #num1 + num2 = value
            #if num1 == num2, then nums must at least contain two num1(or num2), otherwise there is no such sum
            #if num1 != num2, num2 must exits in the nums, otherwise there is no such sum that consisted by num1 and num2
            for num1 in array:
                if value - num1 in array and (value - num1 != num1 or array[value - num1] == 2):
                    return True
        return False