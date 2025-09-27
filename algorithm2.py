def group_schedule(schedules, daily_times, duration):
    busyTimes = []

    # build busy list
    for i in range(len(schedules)):
        dailyStart = daily_times[i][0].split(":")
        dailyEnd = daily_times[i][1].split(":")
        startDay = int(dailyStart[0]) * 60 + int(dailyStart[1])
        endDay = int(dailyEnd[0]) * 60 + int(dailyEnd[1])

        busyTimes.append([0, startDay])
        busyTimes.append([endDay, 1440])

        for interval in schedules[i]:
            start = interval[0].split(":")
            end = interval[1].split(":")
            s = int(start[0]) * 60 + int(start[1])
            e = int(end[0]) * 60 + int(end[1])
            busyTimes.append([s, e])

    # sort by start
    busyTimes.sort(key=lambda x: x[0])

    # merge overlaps (inefficient way)
    merged = busyTimes
    changed = True
    while changed:
        changed = False
        for i in range(len(merged)-1):
            if merged[i+1][0] <= merged[i][1]:
                merged[i][1] = max(merged[i][1], merged[i+1][1])
                del merged[i+1]
                changed = True
                break  # restart loop

    # find gaps
    answer = []
    for i in range(len(merged)-1):
        start = merged[i][1]
        end = merged[i+1][0]
        if end - start >= duration:
            h1, m1 = divmod(start, 60)
            h2, m2 = divmod(end, 60)
            slot = [f"{h1:02d}:{m1:02d}", f"{h2:02d}:{m2:02d}"]
            answer.append(slot)

    return answer


# Example
person1_Schedule = [["7:00","8:30"],["12:00","13:00"],["16:00","18:00"]]
person1_DailyAct = ["9:00","19:00"]

person2_Schedule = [["9:00","10:30"],["12:20","14:00"],["14:30","15:00"],["16:00","17:00"]]
person2_DailyAct = ["9:00","18:30"]

schedules = [person1_Schedule, person2_Schedule]
daily_times = [person1_DailyAct, person2_DailyAct]

print(group_schedule(schedules, daily_times, 30))
