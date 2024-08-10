import time

def focus_timer(work_minutes=25, break_minutes=5):
    print(f"开始工作 {work_minutes} 分钟...")
    time.sleep(work_minutes * 60)
    print("工作时间结束！")

    print(f"开始休息 {break_minutes} 分钟...")
    time.sleep(break_minutes * 60)
    print("休息时间结束！")

if __name__ == "__main__":
    focus_timer()
