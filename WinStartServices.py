import win32serviceutil # pip instll pypiwin32
import psutil # pip install psutil
import time


#add windows services and also dependensess service  for chacking and started
services = ["VeeamBackupSvc", "VeeamBrokerSvc", "heartbeat"]

mailAddressTo = {}
mailAddressSend = {}



#chacking services and started
def startServices(listService):
    i = 0
    while i < len(services):
        time.sleep(10)
        try:
            win32serviceutil.StartService(listService[i])
            status = psutil.win_service_get(listService[i])
            print(status.as_dict().get('status'))  # this is array display status runinig
        except:
            Exception(print("print service started"))
            i += 1


#Start checking
startServices(services)