import win32serviceutil
import psutil
import time
import smtplib


#add windows services (if have dependensess service) for chacking and started
services = ["metricbeat", "heartbeat"]
SERVICE_STATUS_RUNNING = "running"


# credentioonal for mail services

mailAddressFrom = "test@test.com"
mailAddressFromPassword = "***"
mailAddressToSuccess = {"1@test.com"}
mailAddressToBrocken = {"1@test.com", "1@test.com"}
smtpServer = smtplib.SMTP('outlook.office365.com', 587)
smtpServer.starttls()
smtpServer.login(mailAddressFrom, "***")
successMessageText = "text massage"


#chacking services and started
def startServices(listService):
    a = 0
    while a < len(services):
        i = 0
        while i < len(services):
            try:
                status = psutil.win_service_get(listService[i])
                print(status.as_dict().get('status'))  # this is array display status runinig
                if status.as_dict().get('status') != "running":
                    win32serviceutil.StartService(listService[i])
                    print("sleep 3 sec")
                    time.sleep(3)
            except:
                 Exception()

            i += 1
        a+=1
    #lambda SERVICE_STATUS_RUNNING,


def sendMailbrocken(sendMailBrocken):
    mailBodyMassage = "\r\n".join((
        "From: %s" % mailAddressFrom,
        "To: %s" % mailAddressToBrocken,
        "Subject: %s" % "backup is brocken",
        "",
        "backup is brocken" + sendMailBrocken.__str__()
    ))
    smtpServer.sendmail(mailAddressFrom, mailAddressToBrocken, mailBodyMassage)
    smtpServer.quit()


#Start checking
startServices(services)