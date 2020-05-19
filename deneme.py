import urllib3 ,time
#from win10toast import ToastNotifier
from plyer import notification




say=0
siteler=[]
siteler1=[]

while True:
    http = urllib3.PoolManager()
    #bildiri = ToastNotifier()
    ac = open("siteler.txt")

    for i in ac :

        siteler.append(i)
        siteler1.append(i)

        say += 1

        sil=i.replace("\n","")

        try:
            http.request('GET', '{}'.format(sil), retries=False)

            #bildiri.show_toast(sil,"Aktif")
            notification.notify(  # ikinci bildirim kütüphanesi
                title=sil,
                message=' Aktif',
                app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
                timeout=10,  # seconds
            )

            siteler = []

        except urllib3.exceptions.NewConnectionError:

            #bildiri.show_toast(sil, "DeAktif")
            notification.notify(  # ikinci bildirim kütüphanesi
                title=sil,
                message=' Deaktif',
                app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
                timeout=3,  # seconds
            )

            siteler = []

    if say == len(siteler1):
        say=0
        time.sleep(300)


    ac.close()