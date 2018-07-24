"""
[Easy] Talking Clock
Description

No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're
never late again. A talking clock takes a 24-hour time and translates it into words.

Input Description

An hour (0-23) followed by a colon followed by the minute (0-59).

Output Description

The time in words, using 12-hour format followed by am or pm.

Sample Input data

00:00
01:30
12:05
14:01
20:29
21:00
Sample Output data

It's twelve am
It's one thirty am
It's twelve oh five pm
It's two oh one pm
It's eight twenty nine pm
It's nine pm
Extension challenges (optional)

Use the audio clips found here to give your clock a voice.

programmed by: Matthew Lopez
"""

# take input of the time
time = input("Please enter time: ")
# check to see if it is valid (0-23):(0-59)

# output the time in words
tens = ["oh", "teen", "twenty", "thirty", "fourty", "fifty"]
hours = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

split_time = time.split(":")
og_split_hour = int(split_time[0])
split_hour = og_split_hour
# for the minutes
split_minute = split_time[1]
min_tens = int(split_minute[-2])
min_ones = int(split_minute[-1])
time_string = ""

# making the time not military
if og_split_hour > 12:
    split_hour = split_hour - 12

# minute tens place
if int(split_minute) in range(13, 19):
    time_string = "The time is " + hours[split_hour] + " " + hours[min_ones] + " " + tens[min_tens]
elif int(split_minute) in range(11, 12):
    time_string = "The time is " + hours[split_hour] + " " + hours[int(split_minute)]
else:
    time_string = "The time is " + hours[split_hour] + " " + tens[min_tens] + " " + hours[min_ones]

# checking the am or pm
if og_split_hour > 12:
    time_string += " pm"
else:
    time_string += " am"
print(time_string)