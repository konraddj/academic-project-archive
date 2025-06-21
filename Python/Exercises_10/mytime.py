from datetime import datetime

# current date and time
now = datetime.now()

# convert to string
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S") # %Y-%m-%d %H:%M:%S == YYYY-MM-DD hh:mm:ss
print('DateTime String:', date_time_str)

# Output current time