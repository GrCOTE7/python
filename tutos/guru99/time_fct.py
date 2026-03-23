import time

print(time.timezone)
print(time.tzname)

print('-'*72)

start_time_Guru99 = time.time()
print("Time elapsed after some level wait...")
print("The start time is", start_time_Guru99)
print("The start time in human form", time.ctime(start_time_Guru99))
time.sleep(1)
end_time_Guru99 = time.time()
print("The end time is", end_time_Guru99)
print("The start time in human form", time.ctime(end_time_Guru99))
time.sleep(1)

print("Time elapsed in this example code: ", end_time_Guru99 - start_time_Guru99)

print(time.ctime())

result = time.gmtime(time.time())
print("The structure format of time is as follows")
print(result)
print("Year in structured format is represented as", result.tm_year)
print("Hour in structured format is represented as", result.tm_hour)
