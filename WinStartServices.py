import win32serviceutil
import psutil
import time
import smtplib

#add windows services (if have dependensess service) for chacking and started
services = ["metricbeat", "heartbeat", "Bacula-fd"]
SERVICE_STATUS_RUNNING = "running"

# pouse run in second after start service
time_sleep_run_service = 3

# credentioonal for mail services

mailAddressFrom = "vdidenko@vdidenko.com"
mailAddressFromPassword = "********"
mailAddressTo = {"vdidenko@vdidenko.com"}
smtpServer = smtplib.SMTP('outlook.office365.com', 587)
smtpServer.starttls()
smtpServer.login(mailAddressFrom, "********")

#chacking services and started
def startServices(listService):
    item_for_loop = 0
    while item_for_loop < len(services):
        item_for_iner_loop = 0
        while item_for_iner_loop < len(services):
            try:
                status = psutil.win_service_get(listService[item_for_iner_loop])
                print(status.as_dict().get('status'))  # this is array display status runinig
                if status.as_dict().get('status') != "running":
                    win32serviceutil.StartService(listService[item_for_iner_loop])
                    print("sleep 3 sec")
                    time.sleep(time_sleep_run_service)
                    if item_for_loop == len(services)-1:
                        if status.as_dict().get('status') != "running":
                            sendMailbrocken(status.__str__())
                            print("mail send")
            except:
                 Exception()

            item_for_iner_loop += 1
        item_for_loop+=1

def sendMailbrocken(serviceNotWork):
    mailBodyMassage = "\r\n".join((
        "From: %s" % mailAddressFrom,
        "To: %s" % mailAddressTo,
        "Subject: %s" % "service no started",
        "",
        "Service Not started " + serviceNotWork
    ))
    smtpServer.sendmail(mailAddressFrom, mailAddressTo, mailBodyMassage)
    smtpServer.quit()

#Start checking
startServices(services)