#! /usr/bin/env python
# coding=utf-8
# Syslog example - Chapter 3 - syslogsample.py
# 此处是python 2 版本。脚本有些地方看不懂，所以不会修改成python3。

# 在开始记录信息之前，必须调用openlog()来初始化syslog接口。
# openlog(ident[, logopt[, facility]])
# ident 通常是类似postfix/qmgr[2445], 即程序名[PID]
# syslog([priority,] message)

# 脚本运行成功后，查看/var/log/messages
import syslog, sys, StringIO, traceback, os

def logexception(includetraceback = 0):
    exctype, exception, exctraceback = sys.exc_info()
    excclass = str(exception.__class__)
    message = str(exception)

    if not includetraceback:
        syslog.syslog(syslog.LOG_ERR,"%s: %s" % (excclass, message))
    else :
        excfd = StringIO.StringIO()
        traceback.print_exception(exctype, exception, exctraceback, None, excfd)
        for line in excfd.getvalue().split("\n"):
            syslog.syslog(syslog.LOG_ERR,line)

def initsyslog():
    syslog.openlog("%s[%d]" %(os.path.basename(sys.argv[0]), os.getpid()),0,syslog.LOG_DAEMON)
    syslog.syslog("Started.")


initsyslog()

try:
    raise RuntimeError, "Exception 1"
except:
    logexception(0)

try:
    raise RuntimeError,"Exception 2"
except:
    logexception(1)

syslog.syslog("I'm terminating.")
