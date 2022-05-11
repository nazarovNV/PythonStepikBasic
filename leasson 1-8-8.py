X = int(input("")) # Необходимое количество минут дял сна
H = int (input(""))
M = int (input(""))
time_to_sleep_hours = X // 60 # 7
time_to_sleep_minutes = X % 60 # 42
set_an_alarm_hour = (time_to_sleep_hours + H) + (time_to_sleep_minutes + M) // 60
set_an_alarm_minutes = (time_to_sleep_minutes + M) % 60
print(set_an_alarm_hour)
print(set_an_alarm_minutes)
