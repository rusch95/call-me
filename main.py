import time
from make_call import call_with_headline

debug_counter = 0
#Looping until time is greater or equal to Friday, 
while True:
    debug_counter += 1
    date = time.localtime()
    day = date[2]
    hour = date[3]
    minute = date[4]
    min_day = 23
    min_hour = 16
    min_minute = 0
    time_to_call_flag = minute >= min_minute and hour >= min_hour and day >= min_day
    if time_to_call_flag:    
        call_with_headline()
        break
    if debug_counter > 50:
        debug_counter = 0
        print 'Day: ' + str(day)
        print 'Hour: ' + str(hour)
        print 'Min: ' + str(minute)
        print 'Waiting until Day {}, Hour {}, Min {}'.format(min_day, min_hour, min_minute)
        print ''
    time.sleep(.1)

