def add_time(start, duration, day=''):
  #needs refactoring to clean up variable and make more readable
  days_index ={
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
  }

  days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
  
  start = start.split()
  s_start = start[0]
  l_start = s_start.split(":")
  start_hour = int(l_start[0])
  start_min = int(l_start[1])

  l_duration = duration.split(":")
  duration_hour = int(l_duration[0])
  duration_min = int(l_duration[1])

  end_min = start_min + duration_min

  if end_min >= 60:
    start_hour += 1
    end_min = end_min%60

  end_hour = (start_hour + duration_hour)%12
  if end_hour == 0:
    end_hour += 12
  
  #calculate whether AM or PM
  time_suffix = ''
  suffix_calc = int((start_hour+duration_hour)/12)

  if start[1] == 'PM':
    suffix_calc += 1

  if suffix_calc%2 == 0:
    time_suffix += 'AM'
  elif suffix_calc%2 == 1:
    time_suffix += 'PM'
  #end AM/PM Calc

  #start optional param day. calc index
  day_index = 0
  if day != '':
    day_index += days_index[day.lower()]


  #begin day Passage calc
  day_calc = start_hour+duration_hour
  if start[1] == 'PM':
    day_calc += 12

  amount_days = int(day_calc/24)
  #end days calculation
  
  time_str = ''
  
  #String buiding
  #Initial string
  if end_min < 10:
    time_str += f"{end_hour}:0{end_min} {time_suffix}"
  elif end_min >= 10:
    time_str += f"{end_hour}:{end_min} {time_suffix}"
  #conditional middle string portion, optional day variable pass through
  #finishes end day calc in string
  if day != '':
    local_day = days[((day_index+amount_days)%7)]
    time_str += f", {local_day}"
  #final string portion
  if amount_days > 0:
    if amount_days == 1:
      time_str += " (next day)"
    else:
      time_str += f" ({amount_days} days later)"

  return time_str