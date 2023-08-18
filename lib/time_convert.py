def to24hourtime(hour, minute, period):
    if (int(hour) in range(1, 13) and int(minute) in range(0, 60) and period == ("am" or "pm")):
        if(period == "am"):
            new_hour = str(hour).zfill(2)
            if(hour == 12):
                new_hour = str(0).zfill(2)
        elif(period == "pm"):
            new_hour = str(12 + hour)
            if(hour == 12):
                new_hour = str(hour).zfill(2)
    time = new_hour + str(minute).zfill(2)
            
    print(time)
    return time
    
to24hourtime(12, 45, "am")
