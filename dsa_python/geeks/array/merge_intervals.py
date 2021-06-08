class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge_intervals(intervals, newInterval):
    updated_interval = []
    if len(intervals) == 0:
        return [newInterval]

    if newInterval.start > intervals[-1].end:
        return intervals.append(newInterval)
    
    if newInterval.end < intervals[0].start:
        return intervals.insert(0, newInterval)

    if intervals[0].start >= newInterval.start and intervals[-1].end <= newInterval.end:
        return newInterval

    flag = True
    for interval in intervals:
        if interval.start <= newInterval.start and interval.end >= newInterval.start:
            newInterval = Interval(min(interval.start, newInterval.start), max(interval.end, newInterval.end))
        elif interval.end >= newInterval.end and interval.start <= newInterval.end:
            newInterval = Interval(min(interval.start, newInterval.start), max(interval.end, newInterval.end))
        elif newInterval.end < interval.start:
            if flag:
                updated_interval.append(newInterval)
                flag = False
            updated_interval.append(interval)
        elif newInterval.start > interval.end:
            updated_interval.append(interval)

    if flag:
        updated_interval.append(newInterval)
    if len(updated_interval) > 0:
        return updated_interval
    else:
        return [newInterval]


a = [Interval(1, 3), Interval(6, 9)]
mer = Interval(2, 5)
intervals = list()
aa = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
mer2 = Interval(4, 9)
for a in aa:
    intervals.append(Interval(a[0], a[1]))

pp = merge_intervals(intervals, mer2)
for p in pp:
    print(p.start, p.end)
