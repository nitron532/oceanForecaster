import wget
from datetime import date
todayDate = str(date.today())
def readToday(fileName: str):
    count = 0
    details = []
    with open(f'{fileName}',"r") as file:
        for line in file.readlines():
            count+=1
            if(count<=2):
                continue
            if(count == 26):
                break
            details.append(line)
    return details

#if(line.substring(8,10)!= todaysday): stop loop, return list  | has to ignore first two lines

#NTBC1 and 46053 are the closest buoys to ventura point, ntbc1 is closer to shore

buoyNumber = str(input("Input buoy number: "))
url = 'https://www.ndbc.noaa.gov/data/realtime2/' + buoyNumber + '.txt'
wGetFile = wget.download(url)
buoyDataFile = readToday(wGetFile)
for i in range(len(buoyDataFile)):
    print(buoyDataFile[i])







#ask for user input on which buoy they want, insert that into url string, provide key and maybe convert meter measurements to feet
#i had a good session on x/y/z, check conditions on that day to see what's good at that buoy

