from datetime import datetime
def convert_unix(datetime_str):
    # datetime_str = '2022-07-01 00:00:00'

    # Convert to a datetime object
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

    # Convert to Unix time (seconds since epoch)
    unix_time = int(datetime_obj.timestamp())

    return unix_time
# 1656613800

# print(convert_unix('2022-07-01 00:00:00'))