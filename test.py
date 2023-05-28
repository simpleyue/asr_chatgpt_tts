# @Author  : chenhaibing01
# @File    : test.py
# @Software: PyCharm
startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5


res = 0
worktime = list(zip(startTime, endTime))
print(worktime)
for time in worktime:
    if time[0] <= queryTime <= time[1]:
        res += 1
print(res)



