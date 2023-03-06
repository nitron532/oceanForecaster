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

#if(line.substring(8,10)!= todaysday): stop loop, return list  | has to ignore first two lines, problem is live data file uses different time zone than PST

#NTBC1 and 46053 are the closest buoys to ventura point, ntbc1 is closer to shore

def searchHour(dayList):
    print()
    strQuery = str(input("Which hour of the forecast (military time) are you searching for? Ex. 9   "))
    strQuery = int(strQuery)
    strQuery +=8
  
    if(strQuery>=24):
        strQuery-=24
    if(strQuery<10):
        strQuery = str(strQuery)
        strQuery = "0"+strQuery
    strQuery = str(strQuery)
    print(strQuery)
    
    for i in range(len(dayList)):
        hour = dayList[i]
        #print(hour)
        if(hour[11:13] == strQuery):
            windSpeed = str(float(hour[22:25]) * 3.281)
           # print(windSpeed)
            gustSpeed = str(float(hour[27:30]) * 3.281)
            #print(gustSpeed)
            waveHeight = str(float(hour[33:36]) * 3.281)
            #print(waveHeight)
            imperial = hour[0:21] + " Wind Speed: " + windSpeed + "ft/s " + "Gust Speed: " +  gustSpeed + "ft/s " + "Wave Height: " + waveHeight + "ft " + hour[36:]
            #print(imperial)
            return imperial

#for an approximate result, multiply the length value by 3.281
#GMT is 8 hours ahead of PST
##YY  MM DD hh mm WDIR WSPD GST  WVHT   DPD   APD MWD   PRES  ATMP  WTMP  DEWP  VIS PTDY  TIDE
##yr  mo dy hr mn degT m/s  m/s     m   sec   sec degT   hPa  degC  degC  degC  nmi  hPa    ft
#2023 03 06 04 50 250  4.0  5.0   1.7    13   7.5 286 1019.2  11.9  12.5    MM   MM   MM    MM
#0123456789

#searchHour founction needs to be able to handle when spaces are different, when measurements say MM, might have to go off like the nth instance of 
#when an index isnt a space to find where the different measurements are and keep count, like windspeed is the 5th listed measurement, 5th time 
#loop finds an index that isnt a space i record those numbers


buoyNumber = str(input("Input buoy number: "))
url = 'https://www.ndbc.noaa.gov/data/realtime2/' + buoyNumber + '.txt'
wGetFile = wget.download(url)
buoyDataFile = readToday(wGetFile)
#for i in range(len(buoyDataFile)):
#    print(buoyDataFile[i])
measurements = searchHour(buoyDataFile)
print(measurements)
#input(what hour search for / what should i do now : search for hour option)


#YY  MM DD hh mm WDIR WSPD GST  WVHT   DPD   APD MWD   PRES  ATMP  WTMP  DEWP  VIS PTDY  TIDE
#yr  mo dy hr mn degT m/s  m/s     m   sec   sec degT   hPa  degC  degC  degC  nmi  hPa    ft




#ask for user input on which buoy they want, insert that into url string, provide key and maybe convert meter measurements to feet
#i had a good session on x/y/z, check conditions on that day to see what's good at that buoy

