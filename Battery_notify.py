from plyer import notification
import psutil
from time import sleep

while True:
    battery = psutil.sensors_battery()
    life = battery.percent

    notification.notify(
        title = "Battery Percentage",
        message = f" Current Battery {life} %",
        timeout = 10
    )

    if life < 30:
        notification.notify(
            title = "Battery Low",
            message = "Please connect the adapter.",
            timeout = 10
        )
    sleep(10)

