#Desktop notification

import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!",
            message = "Take a Break! It has been an hour you using pc.",
            timeout = 10
        )
        time.sleep(3)