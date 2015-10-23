import time
from make_call import call_with_headline

#Keeps track of time, in order to call at the activation time.

debug_counter = 0
#Looping until Current Time is greater than or equal to Activation Time
while True:
    debug_counter += 1
    date = time.localtime()

    #Current Time Eastern
    day = date[2]
    hour = date[3]
    minute = date[4]

    #Activation Time Eastern
    min_day = 23
    min_hour = 16
    min_minute = 0
    
    #Checking if Current Time > Activation Time
    time_to_call_flag = minute >= min_minute and hour >= min_hour and day >= min_day
    if day > min_day:
        time_to_call_flag = True
    if day >= min_day and hour > min_hour:
        time_to_call_flag = True

    #Activates the calling function when Current > Time
    if time_to_call_flag:    
        call_with_headline()
        break

    #Prints out the both time values for debug purposes
    if debug_counter > 50:
        debug_counter = 0
        print 'Day: ' + str(day)
        print 'Hour: ' + str(hour)
        print 'Min: ' + str(minute)
        print 'Waiting until Day {}, Hour {}, Min {}'.format(min_day, min_hour, min_minute)
        print ''
    time.sleep(.1)

