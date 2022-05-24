# Write a Python program to convert seconds to day, hour, minutes and seconds.

time = int(input("Input seconds to convert to days, hours, minutes and seconds: "))

day = time // (24 * 60 * 60)
time = time % (24 * 60 * 60)
hour = time // (60 * 60)
time = time % (60 * 60)
minute = time // 60
time = time % 60
seconds = time

print("d:hh:mm:ss -> %d:%d:%d:%d" % (day, hour, minute, seconds))