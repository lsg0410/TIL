import platform
print(platform.architecture())
import win32com.client
import pythoncom
import os, sys
import json
import pandas as pd
import numpy as np
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class XASessionEvents:
    state = False
    def OnLogin(self, code, msg):
        print("OnLogin : ", code, msg)
        XASessionEvents.state = True
    def OnLogout(self):
        print("-----------")
        pass
    def OnDisconnect(self):
        print("========")
        pass

def Login(id, pwd, cert, url = "demo.ebestsec.co.kr", port = 200001, svrtype=0):
    session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
    result = session.ConnectServer(url, port)
    if not result:
        nErrCdoe = session.GetLastError()
        strErrMsg = Session.GetErrorMessage(nErrCode)
        return (False, nErrCode, strErrMsg, None, session)
    session.Login(id, pwd, cert, svrtype, 0)

    while XASessionEvents.state == False:
        pythoncom.PumpWaitingMessages()
    account_ls = []
    account_num = session.GetAccountListCount()

    for i in range(account_num):
        account_ls.append(session.GetAccountList(i))
    return (True, 0, "OK", account_ls, session)

if __name__ == "__main__":
    cert_df = pd.read_csv("cert.csv")
    id = cert_df["id"].values[0]
    pwd = cert_df["pwd"].values[0]
    cert = cert_df["cert"].values[0]
    url  = cert_df["url"].values[0]
    result, code, msg, account_ls, session = Login(id = id, pwd = pwd, cert = cert, url = url, port = 200001, svrtype=0)
    if result == False:
        sys.exit(0)
    for account in account_ls:
        print(account)
