import heapq

class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        records = {}

        for student in results:
            # id = student.id
            # score = student.score

            id = student[0]
            score = student[1]

            if id in records:
                heapq.heappush(records[id], score * -1)
            else:
                records[id] = [score * -1]

        res = {}
        for id, scores in records.iteritems():
            sum = 0
            for i in range(5):
                score = heapq.heappop(records[id])
                sum += score
            res[id] = sum * -1 / 5.0
        return res

s = Solution()
print s.highFive([[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]])