import math

def add_time(start, duration, weekday = ''):
    start_time, m_info = start.split()

    start_hour, start_minutes = split_hours_and_minutes(start_time)
    duration_hour, duration_minutes = split_hours_and_minutes(duration)

    minutes_total, extra_hours = calc_minutes(start_minutes, duration_minutes) 

    hours_total, extra_days, hours_total_int = calc_hours(start_hour, duration_hour, extra_hours)

    m_info, extra_days = calc_m_info(m_info, hours_total_int, extra_days)

    new_time = ((hours_total + ':' + minutes_total) + ' ' + m_info)

    if weekday != '':
        new_time = add_weekday_to_new_time(new_time, weekday, extra_days)
    
    new_time = add_text_if_different_day(new_time, extra_days)


    return new_time


def split_hours_and_minutes(time):
    return time.split(':')

def is_odd(int):
    if int % 2 == 0:
        return False
    else:
        return True 
    
def check_if_one_char_long_and_add_zero(input):
    string = str(input)
    if len(string) == 1:
        string = f'0{string}'
    return string

def convert_surplus_minutes_to_hours(minutes_total_int):
    if minutes_total_int >= 60:
        extra_hours = math.floor(minutes_total_int/60)
        minutes_total_int = minutes_total_int % 60
    else:
        extra_hours = 0
    return minutes_total_int, extra_hours

def calc_minutes(start_minutes, duration_minutes):
    minutes_total_int = int(start_minutes) + int(duration_minutes)
    minutes_total_int, extra_hours = convert_surplus_minutes_to_hours(minutes_total_int)
    minutes_total = check_if_one_char_long_and_add_zero(minutes_total_int)
    return minutes_total, extra_hours

def calc_hours(start_hour, duration_hour, extra_hours):
    hours_total_int = int(start_hour) + int(duration_hour) + int(extra_hours)
    hours_total, extra_days = convert_surplus_hours_to_days(hours_total_int)
    return hours_total, extra_days, hours_total_int

def convert_surplus_hours_to_days(hours_total_int):
    if hours_total_int > 12:
        hours_total = str(hours_total_int % 12)
        extra_days = math.floor(hours_total_int/24)
        if hours_total == '0':
            hours_total = '12'
    else:
        hours_total = str(hours_total_int)
        extra_days = 0
    return hours_total, extra_days

def calc_m_info(m_info, hours_total, extra_days):
    hours_total_int = math.floor(int(hours_total) / 12)
    print(hours_total_int)
    if ((hours_total_int % 2) == 1):
        if m_info == 'AM':
            m_info = 'PM'
        else:
            m_info = 'AM'
            extra_days = extra_days + 1
    return m_info, extra_days

def add_weekday_to_new_time(new_time, weekday, extra_days):
    weekdays = {'monday': 0,'tuesday': 1,'wednesday': 2,'thursday': 3,'friday': 4,'saturday': 5,'sunday': 6}
    weekdays_numbers = {0: 'Monday',1: 'Tuesday',2: 'Wednesday',3: 'Thursday',4: 'Friday',5: 'Saturday',6: 'Sunday'}
    day_int = int(weekdays[weekday.lower()])
    day_int = (day_int + extra_days) % 7
    weekday = weekdays_numbers[day_int]
    new_time = f'{new_time}, {weekday}'
    return new_time

def add_text_if_different_day(new_time, extra_days):
    if extra_days == 1:
        new_time = f'{new_time} (next day)' 
    if extra_days > 1:
        new_time = f'{new_time} ({extra_days} days later)' 
    return new_time