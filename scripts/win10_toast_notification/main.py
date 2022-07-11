from win10toast import ToastNotifier
from datetime import datetime
toaster = ToastNotifier()

toaster.show_toast("Сделай зарядку",
                   icon_path=None,
                   duration=5,
                   threaded=True)

with open('runtimes.txt', 'a+') as file:
    file.write(str(datetime.now()))
