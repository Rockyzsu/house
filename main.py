#-*-coding=utf-8-*-
__author__ = 'xda'

import urllib2,re
import database
def getContent():
    url="http://ris.szpl.gov.cn/"
    one_hand="credit/showcjgs/ysfcjgs.aspx"
    second_hand="credit/showcjgs/esfcjgs.aspx"
    req=urllib2.Request(url+one_hand)
    content=urllib2.urlopen(req).read()
    #print content
    date=re.compile(r'<SPAN class=titleblue><span id=\"lblCurTime5\">(.*)</span>')
    reg=re.compile(r'<td width="14%"><b>(\d+)</b>')
    result=reg.findall(content)
    current_date=date.findall(content)
    '''
    for i in current_date:
        print i
    '''
    print current_date[0]
    print '一手商品房成交套数：%s'  % result[0]
    print '一手商品房成交面积： %s'  % result[1]


    sec_req=urllib2.Request(url+second_hand)
    sec_content=urllib2.urlopen(sec_req).read()
    #print sec_content
    #sec_quantity=re.compile(r'<td style="border-color:#DEEFF5;width:30%;">(\d+)</td>')
    sec_quantity=re.compile(r'<td width="30%">(\d+)</td>')
    sec_result=sec_quantity.findall(sec_content)
    '''
    k=0
    for j in sec_result:
        print k
        print j
        k=k+1
    '''
    print '二手商品房成交套数：%s'  % sec_result[1]
    print '二手商品房成交面积： %s'  % sec_result[5]
    database.create_table()
    database.insert(current_date[0],result[0],'0',sec_result[1],'0')

getContent()