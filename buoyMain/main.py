import wget
import os
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
            stringLine = ""
            for character in line: #
                if character == " ":
                    stringLine +="&"
                else:
                    stringLine += character
            details.append(stringLine)
    return details

#if(line.substring(8,10)!= todaysday): stop loop, return list  | has to ignore first two lines, problem is live data file uses different time zone than PST
"""

"""
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
        readableHour = ""
        if(hour[11:13] == strQuery):
            count = -1
            for i in range(len(hour)):
                startIndex = 0
                endIndex = 0
                if hour[i] == "&" and hour[i+1] != "&":
                    startIndex = i+1
                    endIndex = i+1
                    while hour[i+1] != "&" and i != (len(hour)-2):
                        endIndex +=1
                        i+=1
                    count+=1
                    match count:
                        case 0:
                            readableHour += "Month: "
                        case 1:
                            readableHour += "\n Day (GMT): "
                        case 2:
                            readableHour += "\n Hour (GMT): "
                        case 3:
                            readableHour+= "\n Minute: "
                        case 4:
                            readableHour+= "\n Wind Direction (degrees): "
                        case 5:
                            readableHour+= "\n Wind Speed (meters/sec): "
                        case 6: 
                            readableHour+= "\n Peak Gust Speed (meters/sec): "
                        case 7:
                            readableHour+= "\n Significant Wave Height (meters): "
                        case 8:
                            readableHour+= "\n Dominant Wave Period (sec): "
                        case 9:
                            readableHour+= "\n Average Wave Period (sec): "
                        case 10:
                            readableHour+= "\n Dominant Period Wave Direction (degrees): "
                        case 11:
                            readableHour += "\n Sea Level Pressure (hPa): "
                        case 12:
                            readableHour += "\n Air Temperature (celsius): "
                        case 13:
                            readableHour += "\n Sea Surface Temperature (celsius): "
                        case 14:
                            readableHour += "\n Dewpoint Temperature (celisus): "
                        case 15:
                            readableHour += "\n Station Visibility (nautical miles): "
                        case 16:
                            readableHour += "\n Pressure Tendency (hPa): "
                        case 17:
                            readableHour += "\n Tide (feet): "
                    readableHour += hour[startIndex:endIndex]
            return readableHour


#for descriptions of data categories, visit https://www.ndbc.noaa.gov/faq/measdes.shtml
#ask user if they want to access specific hour or most recent data


#for an approximate result, multiply the length value by 3.281
#GMT is 8 hours ahead of PST
##YY  MM DD hh mm WDIR WSPD GST  WVHT   DPD   APD MWD   PRES  ATMP  WTMP  DEWP  VIS PTDY  TIDE
##yr  mo dy hr mn degT m/s  m/s     m   sec   sec degT   hPa  degC  degC  degC  nmi  hPa    ft
#2023 03 06 04 50 250  4.0  5.0   1.7    13   7.5 286 1019.2  11.9  12.5    MM   MM   MM    MM
#0123456789


buoyNumber = str(input("Input buoy number, station names must be all CAPS: "))
url = 'https://www.ndbc.noaa.gov/data/realtime2/' + buoyNumber + '.txt'
wGetFile = wget.download(url)
buoyDataFile = readToday(wGetFile)
toDelete = str(wGetFile)
measurements = searchHour(buoyDataFile)
print(measurements) #showing "none" sometimes live data doesnt have searched for hour, imperial is returned as blank, should have check for "none"
os.remove(toDelete)
#input(what hour search for / what should i do now : search for hour option)


#YY  MM DD hh mm WDIR WSPD GST  WVHT   DPD   APD MWD   PRES  ATMP  WTMP  DEWP  VIS PTDY  TIDE
#yr  mo dy hr mn degT m/s  m/s     m   sec   sec degT   hPa  degC  degC  degC  nmi  hPa    ft




#ask for user input on which buoy they want, insert that into url string, provide key and maybe convert meter measurements to feet
#i had a good session on x/y/z, check conditions on that day to see what's good at that buoy

