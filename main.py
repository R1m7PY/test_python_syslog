import syslog
import time


def Job():
    # syslog.openlog(ident="PythonTest", logoption=syslog.LOG_INFO, facility=syslog.LOG_AUTH)
    syslog.syslog(syslog.LOG_INFO, "I started working")
    for i in range(5):
        time.sleep(2)
        syslog.syslog(syslog.LOG_INFO, "I'm working")
    syslog.syslog(syslog.LOG_INFO, "I'm done working")


if __name__ == '__main__':
    Job()
