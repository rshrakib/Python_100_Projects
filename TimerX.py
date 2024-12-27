import time



def countdown(user_time):
    while user_time >= 0:
        mins, sec = divmod(user_time,60)

        timer = f'{mins:02d}:{sec:02d}'
        print(timer, end='\r', flush=True)
        time.sleep(1)
        user_time-=1
    print('Countdown off')

if __name__ =='__main__':
    user_time = int(input("Enter your time in sec: "))
    countdown(user_time)