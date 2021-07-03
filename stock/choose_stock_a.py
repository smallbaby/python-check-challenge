import baostock as bs
import pandas as pd
import datetime
import numpy as np
import time

lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:' + lg.error_code)
print('login respond  error_msg:' + lg.error_msg)

datalist = []


# 获取REO的变异系数
def getCV(arr):
    cv = 0
    try:
        cv = np.std(arr, ddof=1) / np.mean(arr)
    except:
        pass
    return cv


# 净利润增长率
def getYOYNI(code, year=2021, quarter=1):
    rs = bs.query_growth_data(code, year, quarter)
    re = 0
    try:
        re = rs.get_row_data()[5]
        re = round(float(re), 2)
    except:
        pass
    return re


def compare_time(time1, time2, days=365):
    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(time2, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days >= days


def getROE(code="SH.600000", year=2015):
    rs_dupont = bs.query_dupont_data(code=code, year=year, quarter=4)
    re = 0
    try:
        re = rs_dupont.get_row_data()[3]
        re = round(float(re) * 100, 2)
    except:
        pass
    return re


def getName(code):
    rs = bs.query_stock_basic(code)
    return rs.get_row_data()[1]


# 获取上市时间
def getIPO(code):
    re = 0
    try:
        re = bs.query_stock_basic(code)
        re = re.get_row_data()[2]
    except:
        pass
    return re


# 获取所属分类
def getIndustry(code):
    rs = bs.query_stock_industry(code)
    return rs.get_row_data()


def getClosePrice(code):
    rs = bs.query_history_k_data_plus(code, "close")
    re = rs.get_row_data()[0]
    re = round(float(re), 2)
    return re


def Combine(code):
    time.sleep(0.1)
    tmp = []
    roe2016 = getROE(code, 2016)
    roe2017 = getROE(code, 2017)
    roe2018 = getROE(code, 2018)
    roe2019 = getROE(code, 2019)
    roe2020 = getROE(code, 2020)

    time1 = "2021-06-30"
    time2 = getIPO(code)
    YOYNI = getYOYNI(code)
    cv = getCV([roe2016, roe2017, roe2018, roe2019, roe2020])
    try:
        if roe2016 > 0.05 and roe2017 > 0.05 and roe2018 > 0.05 and roe2019 > 0.05 and roe2020 > 0.05 and compare_time(
                time1, time2, 365 * 3) and YOYNI > -1 and 0 < cv < 0.4:
            tmp.append(code)
            tmp.append(getName(code))
            tmp.append(getClosePrice(code))
            tmp.append(getIndustry(code))
            tmp.append(YOYNI)
            tmp.append(roe2016)
            tmp.append(roe2017)
            tmp.append(roe2018)
            tmp.append(roe2019)
            tmp.append(roe2020)
            tmp.append(cv)
            tmp.append(time2)
    except:
        pass
    return tmp


def main():
    #  沪深300
    rs = bs.query_hs300_stocks()
    # 获取上证50成分股
    rs1 = bs.query_sz50_stocks()
    # 获取中证500成分股
    rs2 = bs.query_zz500_stocks()
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        re = Combine(rs.get_row_data()[1])
        if re:
            datalist.append(re)
    result = pd.DataFrame(datalist)
    result.to_csv("/tmp/a.csv", index=False)


main()

bs.logout()
