def group_schedule(schedules, daily_times, duration):
    busyTimes = [] #storing busy intervals in minutes

    #building busy list
    for i in range(len(schedules)): #loop through each persons schedule 
        dailyStart = daily_times[i][0].split(":") #take out the :
        dailyEnd = daily_times[i][1].split(":") #take out the :
        startDay = int(dailyStart[0]) * 60 + int(dailyStart[1]) #convert start time to minutes
        endDay = int(dailyEnd[0]) * 60 + int(dailyEnd[1]) #convert end time to minutes 

        busyTimes.append([0, startDay]) #add start day to empty busy times list 
        busyTimes.append([endDay, 1440]) #add end day to empty busy times list 

        for interval in schedules[i]: #loop through schedules into minutes 
            start = interval[0].split(":") #take out the :
            end = interval[1].split(":") #take out the :
            s = int(start[0]) * 60 + int(start[1]) #convert start time to minutes 
            e = int(end[0]) * 60 + int(end[1]) #convert end time to minutes 
            busyTimes.append([s, e]) #add start time and end time (minutes) to list 

    # sort by start
    busyTimes.sort(key=lambda x: x[0])

    #merge the overlapping times 
    merged = busyTimes #initalize merged 
    changed = True #boolean initailze
    while changed: #while change 
        changed = False #so at least one run
        for i in range(len(merged)-1): #iterate through merge 
            if merged[i+1][0] <= merged[i][1]: #if our intervals overlap
                merged[i][1] = max(merged[i][1], merged[i+1][1]) #then we merge them 
                del merged[i+1] #delete the merged interval 
                changed = True #restart loop
                break  # restart loop

    # find gaps
    answer = [] #blank list 
    for i in range(len(merged)-1):#loop through all of merged 
        start = merged[i][1] #end of current busy interval 
        end = merged[i+1][0] #start of next busy interval 
        if end - start >= duration:#if gap is long enough 
            h1, m1 = divmod(start, 60) #conver tto minutes
            h2, m2 = divmod(end, 60) #convert end to minutes 
            slot = [f"{h1:02d}:{m1:02d}", f"{h2:02d}:{m2:02d}"] #formattiong
            answer.append(slot) #adding slot to the answer 

    return answer #return 


#person1 schedule and daily act 
person1_Schedule = [["7:00","8:30"],["12:00","13:00"],["16:00","18:00"]]
person1_DailyAct = ["9:00","19:00"]

#person2 schedule and daily act 
person2_Schedule = [["9:00","10:30"],["12:20","14:00"],["14:30","15:00"],["16:00","17:00"]]
person2_DailyAct = ["9:00","18:30"]

#combine
schedules = [person1_Schedule, person2_Schedule]
daily_times = [person1_DailyAct, person2_DailyAct]

print(group_schedule(schedules, daily_times, 30))
