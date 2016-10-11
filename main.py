#-*-coding=utf-8-*-
__author__ = 'rocky'
#获取每天深圳一手房，二手房的成交套数与面积，并且写入数据库
#主要就是正则表达抓取几个数字
import urllib2,re
import database
def getContent():
    url="http://ris.szpl.gov.cn/"
    one_hand="credit/showcjgs/ysfcjgs.aspx"
    second_hand="credit/showcjgs/esfcjgs.aspx"
    req=urllib2.Request(url+one_hand)
    content=urllib2.urlopen(req).read()
    #返回的就是网页的源码，没有做任何防爬虫的处理，zf网站，呵呵
    #print content
    date=re.compile(r'<SPAN class=titleblue><span id=\"lblCurTime5\">(.*)</span>')
    reg=re.compile(r'<td width="14%"><b>(\d+)</b>')
    result=reg.findall(content)
    current_date=date.findall(content)

    reg2=re.compile(r'<td align="right"><b>(.*?)</b>')
    yishou_area=reg2.findall(content)


    print current_date[0]
    print '一手商品房成交套数：%s'  % result[0]
    print '一手商品房成交面积： %s'  % yishou_area[0]


    sec_req=urllib2.Request(url+second_hand)
    sec_content=urllib2.urlopen(sec_req).read()

    sec_quantity=re.compile(r'<td width="30%">(\d+)</td>')
    sec_result=sec_quantity.findall(sec_content)
    second_area=re.findall(r'<td align="right">(.*?)</td>',sec_content)

    print '二手商品房成交套数：%s'  % sec_result[1]
    print '二手商品房成交面积： %s'  % second_area[2]
    database.create_table()
    database.insert(current_date[0],result[0],yishou_area[0],sec_result[1],second_area[2])

getContent()