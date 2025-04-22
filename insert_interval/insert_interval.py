
def finding(intervals): 

    if not intervals: 
        return 0

    if len(intervals) == 1: 
        return 0

    intervals.sort(key = lambda x: x[0])
    print(intervals)

    merged = [intervals[0]]
    ways = 0
    for current in intervals[1:]:
        prev = merged[-1] 
        if current[0] < prev[1]:
            ways += 1
    return ways

finding([[1,100],[11,22],[1,11],[2,12]])