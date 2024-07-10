import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings.sort()
meetings.sort(key=lambda x:x[1])

timetable = [meetings[0]]
for i in range(1, len(meetings)):
    now = meetings[i]
    if timetable[-1][1] <= now[0]:
        timetable.append(meetings[i])

print(len(timetable))