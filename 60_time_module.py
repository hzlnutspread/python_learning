import time

# to find computer's epoch
print(time.ctime(0))
# ctime method converts a time expressed in seconds since epoch to a readable string
print(time.ctime(1000000))

print(time.time())
# returns current second since epoch

print(time.ctime(time.time()))
# combines the previous two methods


time_object = time.localtime()
# time_object = time.gmtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)  # string format time
print(local_time)


time_string = "20 April, 2020"
time_formatted = time.strptime(time_string, "%d %B, %Y")
print(time_formatted)


time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_str = time.asctime(time_tuple)
print(time_str)


time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_str = time.mktime(time_tuple)
print(time_str)