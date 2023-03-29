import syslog
import time


def Job():
    syslog.openlog(ident="python_test", logoption=syslog.LOG_INFO, facility=syslog.LOG_AUTH)
    syslog.syslog("I started working")
    for i in range(5):
        time.sleep(2)
        syslog.syslog("I'm working")
    syslog.syslog("I'm done working")


if __name__ == '__main__':
    Job()
