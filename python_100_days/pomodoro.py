import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1

def pomodoro_timer():
    work_time = 25
    short_break = 5
    long_break = 15
    cycles = 4

    for i in range(1, cycles + 1):
        print(f"\n🍅 Cycle {i}: Focus for {work_time} minutes!")
        countdown(work_time)
        print("✅ Focus time over!")

        if i < cycles:
            print(f"🧘‍♂️ Take a short break for {short_break} minutes.")
            countdown(short_break)
        else:
            print(f"🎉 Long break time! {long_break} minutes of peace.")
            countdown(long_break)

        input("Press Enter to start next cycle...")

pomodoro_timer()
