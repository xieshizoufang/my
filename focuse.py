import time

def timer(duration):
    print("尝试保持专注，持续 %d 分钟...\n" % duration)
    time.sleep(duration * 60)
    print("专注时间到！")

if __name__ == "__main__":
    duration = int(input("请输入专注时长（分钟）："))
    timer(duration)
