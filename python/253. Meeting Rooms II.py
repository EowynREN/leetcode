def minMeetingRooms(self, intervals):
    # Write your code here
    room = []
    # 加入开始时间和结束时间，1是房间+1，-1是房间-1
    for i in intervals:
        room.append((i.start, 1))
        room.append((i.end, -1))
    tmp = 0
    ans = 0
    # 排序, 确保所有item是按时间排序的，这样计算的结果才准确
    room = sorted(room)
    # 扫描一遍
    for idx, cost in room:
        tmp += cost
        ans = max(ans, tmp)
    return ans