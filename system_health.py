from shutil import disk_usage
from psutil import cpu_percent
import sys


class SystemHealth:
    def check_disk_usage():
        # empty from your system memory
        path = input(
            'Please write the path you want, for example (/) root dir, if you want to keep it as default, just press enter : ')
        try:
            if path == '':
                disk = disk_usage('/')
            elif path != None:
                disk = disk_usage(path)
            free = round(disk.free/disk.total*100)
            if free <= 30:
                return (f'This amount is empty from your system memory : {free}%\nYour memory is not healthy ):\nPlease consider reducing consumption ...')
            elif free >= 30:
                return (f'This amount is empty from your system memory : {free}%\nYour memory is healthy :)')
        except:
            print(f'The entered path is invalid, please enter the correct path, for example (/) root dir \ntry agin :)')
            sys.exit()

    def check_cpu_usage():
        # cpu intake
        time = input(
            'Please write the time you want, for example (5) seconds, if you want to keep it as default, just press enter : ')
        try:
            if time == '':
                cpu = cpu_percent(5)
            elif time != None:
                cpu = cpu_percent(int(time))
            if cpu >= 70:
                return (f'Your cpu intake: {cpu}%\nYour cpu is not healthy ):\nPlease consider reducing consumption ...')
            elif cpu <= 70:
                return (f'Your cpu intake: {cpu}%\nYour cpu is healthy :)')
        except:
            print('The time entered is invalid, please enter the correct time, for example (5) seconds \nTry again :)')
            sys.exit


check_disk_usage = SystemHealth.check_disk_usage()
check_cpu_usage = SystemHealth.check_cpu_usage()

print(check_disk_usage)
print(check_cpu_usage)