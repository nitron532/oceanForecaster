import wget
url = 'https://www.ndbc.noaa.gov/data/realtime2/46053.txt'
filename = wget.download(url)
print(filename)
#ask for user input on which buoy they want, insert that into url string, provide key and maybe convert meter measurements to feet