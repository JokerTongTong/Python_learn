import time
import datetime


'''
struct_time：time库定义的时间类型，包含一个 9元元组，其中 tm_isdist 表示是否为闰年
time.struct_time(tm_year=2018, tm_mon=10, tm_mday=12, 
                tm_hour=13, tm_min=51, tm_sec=29, 
                tm_wday=4, tm_yday=285, tm_isdst=0)               
time.gmtime([secs])：接受一个时间戳，返回 UTC标准的 struct_time 。没有传入时间戳则以当前时间的时间戳为参数。
time.localtime([secs]) ：与 time.gmtime([secs])相似，不过返回的是以当前时区为标准的 struct_time 。
time.mktime(t)：接受一个 struct_time类型的变量，返回变量对应的时间戳。
time.sleep(secs)：阻塞程序 secs秒。
time.strftime(format[, t])：接受一个 struct_time类型的变量，返回 format指定格式的时间。没有传入 struct_time参数，则默认以当前时间作为参数。
time.strptime(string[,format])：接受一个时间字符串，根据给定的 format将其转换为 struct_time类型并返回。如果 format与给定的字符串不匹配，会报 ValueError错误。
time.time()：返回当前时间的时间戳。

'''



def strftime(timestamp, format_string='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format_string, time.localtime(timestamp))


def strptime(string, format_string='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(string, format_string))

print(strftime(time.time()))

print(strptime('2019-07-03 15:08:24'))

tm1 = time.time()
print('tm:{}'.format(tm1))

tm2 = time.mktime(time.localtime())
print('tm:{}'.format(tm2))


#1.将字符串时间转换为时间戳
a = "2019-04-27 17:49:00"
# 转化为数组
timeArray = time.strptime(a,"%Y-%m-%d %H:%M:%S")
print(timeArray)

# 转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

# 2.字符串格式更改
'''
如 a = "2019-04-27 17:49:00",想改为 a = "2019/04/27 17:49:00"
方法 
    先转换为时间数组，然后转换为其他格式
'''

otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S",timeArray)
print(otherStyleTime)


# 3.时间戳转换为指定格式日期：
'''
方法一：
    利用localtime()转换为时间数组，然后格式化为需要的格式
'''
timeStamp = 1524822540
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
print(otherStyleTime)

'''
方法二：
'''
timeStamp = 1524822540
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)


# 4.获取当前时间并转换为指定日期格式
# 方法一：
# 获取当前时间戳
now = int(time.time()) # 这是时间戳
# 转换为其他日期格式.如：“%Y-%m-%d %H:%M:%S”
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S",timeArray) # 2019-07-03 17:22:04
print(otherStyleTime)

# 方法二：
now = datetime.datetime.now() # 这是时间数组格式
# 转换为指定的格式：
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

# 5.获得三天前的时间
# 方法：
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now()-datetime.timedelta(days=3))
                                              # timedelta()参数有days,hours,seconds,microseconds
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

# 6.给定时间戳，计算该时间的几天前时间
timeStamp = 1524822540
# 先转换为datetime
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray-datetime.datetime(day=3)

