import os

from datetime import datetime

# os.rename(os.listdir()[0],'adi.jpg')
print(os.listdir('pics')[0])
# os.rename("pics/"+os.listdir('pics')[0], "pics/vaishnavi.jpg")


a = [i.split('-')[0] for i in os.listdir()]
print(a)
for i in sorted(os.listdir('pics'), key=lambda x: os.stat('pics/'+x).st_ctime):
    print(i)
# c = os.stat('suman.jpg').st_ctime
# print(datetime.fromtimestamp(c))