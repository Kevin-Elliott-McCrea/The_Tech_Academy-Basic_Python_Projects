from datetime import datetime
import pytz

newYork = pytz.timezone('America/New_York')
London = pytz.timezone('Europe/Dublin')
Portland = pytz.timezone('America/Los_Angeles')

ny_time = datetime.now(newYork)
print(ny_time.strftime('%H%M'))

lon_time = datetime.now(London)
print(lon_time.strftime('%H%M'))

port_time = datetime.now(Portland)
print(port_time.strftime('%H%M'))


ny_str = ny_time.strftime('%H%M')
lon_str = lon_time.strftime('%H%M')
port_str = port_time.strftime('%H%M')


                 
if (int(ny_str) < 900 or int(ny_str) > 1700):
    print("The New York branch is closed")
else: print("The New York branch is open")

if (int(lon_str) < 900 or int(lon_str) > 1700):
    print("The London branch is closed")
else: print("The London branch is open")

if (int(port_str) < 900 or int(port_str) > 1700):
    print("The Portland branch is closed")
else: print("The Portland branch is open")

