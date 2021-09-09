def add_time(start, duration, day=False):
  days_of_the_day_index = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "friday":6}
  days_of_the_day_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  duration_t = duration.partition(":")
  duration_h = int(duration_t[0])
  duration_m = int(duration_t[2])

  start_t = start.partition(":")
  start_m_t = start_t[2].partition(" ")
  start_h = int(start_t[0])
  start_m = int(start_m_t[0])
  AM_or_PM = start_m_t[2]
  am_and_pm = {"AM":"PM", "PM":"AM"}

  days = int(duration_h / 24)

  end_m = start_m + duration_m
  if (end_m >= 60):
    start_h += 1
    end_m = end_m %60
  
  am_or_pm_flip = int((start_h + duration_h) / 12)
  end_h = (start_h + duration_h) % 12

  if end_m > 9:
    end_m = end_m  
  else:
    end_m = "0" + str(end_m)

  if end_h == 0:
     end_h = 12
  else:
    end_h

  if (AM_or_PM == "PM" and start_h + (duration_h %12) >= 12):
    days +=1
  
  if am_or_pm_flip % 2 == 1:
    AM_or_PM = am_and_pm[AM_or_PM]
  else: 
    AM_or_PM

 
 
  returnTime = str(end_h) + ":" + str(end_m) + " " + str(AM_or_PM)
  if (day):
    day = day.lower()
    index = int((days_of_the_day_index[day]) + days) %7
    n_day = days_of_the_day_array[index]
    returnTime += ", " + n_day
  
  if (days == 1):
    return returnTime + " " + "(next day)"
  elif (days > 1):
    return returnTime + " (" + str(days) + " days later)"

  return returnTime



  #if am_and_pm == "AM" and enh_h >12:
   # AM_or_PM = "PM"
  #if am_and_pm == "AM" and enh_h >12:
   # AM_or_PM = "AM"
  

  
  


    





