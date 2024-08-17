import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("时间到！")

def pomodoro_timer(work_duration=25, break_duration=5):
    while True:
        print("开始工作 25 分钟...")
        countdown(work_duration)
        print("开始休息 5 分钟...")
        countdown(break_duration)

if __name__ == "__main__":
    pomodoro_timer()
