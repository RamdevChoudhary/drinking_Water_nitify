import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!",
            message = "The National Academies of Science, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for wenen.",
            app_icon = "C:/Users/Admin/OneDrive/Pictures/Desktop/Python/Images/glass.ico",
            timeout=10
        )
        time.sleep(60*60)

#  if you need to run you app in backgroud with python use ths command in terminal
#  pythonw .\filename.py
