import requests
from bs4 import BeautifulSoup
import pymysql

def getRankInfo():
    info = []
    res = requests.get('https://www.qidian.com/rank')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    for timeInfo in soup.select('.book-list'):
        for li in timeInfo.select('li'):
            name = li.select('.name')
            if len(name) > 0:
                href = "https:"+name[0].get('href')
                name = name[0].text
                newInfo = {}
                newInfo['name'] = name
                newInfo['href'] = href
                for i in range(0,len(info)):
                    if(newInfo == info[i]):
                        del info[i]
                        break
                info.append(newInfo)

    return info

def searchRankInfo():
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    cur = db.cursor()
    sql_DeleteBook_Rank = "delete from Book_Rank"
    cur.execute(sql_DeleteBook_Rank)
    db.commit()
    book = []
    for i in range(len(getRankInfo())):
        url = getRankInfo()[i]['href']
        name = getRankInfo()[i]['name']

        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        writer = ''
        for writer in soup.select('.writer'):
            writer = writer.text

        cur = db.cursor()
        sql_Insert= "INSERT INTO Book_Rank (name,href,writer) VALUES ('"+name+"','"+url+"','"+writer+"')"
        cur.execute(sql_Insert)
        db.commit()

        content1 = ''
        index = 0
        for catalog in soup.select('.volume'):
            for li in catalog.select('li'):
                if index < 80:
                    a = li.select('a')
                    if (len(a)):
                        part1 = a[0].text
                        content1 = content1 + part1
                        index += 1
                else:
                    break
        content2 = ''
        for tag in soup.select('.tag'):
            a = tag.select('a')
            if(len(a)):
                for num in range(len(a)):
                    part2 = (a[num].text)*2
                    content2 = content2 + part2
        content = content1+content2
        with open(name+".txt","a") as f:
            f.write(name+" "+content)
    print("输出完成")
    db.close()


def getSortInfo():
    info = []
    head = 'https://www.qidian.com/'
    x = ['xuanhuan','dushi','xianxia','kehuan','youxi','lishi']
    for i in range(6):
        res = requests.get(head+x[i])
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        for timeInfo in soup.select('.rec-list'):
            for li in timeInfo.select('li'):
                a = li.select('a')
                if len(a) > 0:
                    href = "https:"+a[0].get('href')
                    name = a[0].text
                    newInfo = {}
                    newInfo['name'] = name
                    newInfo['href'] = href
                    for i in range(len(info)):
                        if(newInfo == info[i]):
                            del info[i]
                    info.append(newInfo)

    return info

def searchSortInfo():
    book = []
    for i in range(len(getSortInfo())):
        url = getSortInfo()[i]['href']
        name = getSortInfo()[i]['name']
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        content1 = ''
        index = 0
        for catalog in soup.select('.volume'):
            for li in catalog.select('li'):
                if index < 50:
                    a = li.select('a')
                    if (len(a)):
                        part1 = a[0].text
                        content1 = content1 + part1
                        index += 1
                else:
                    break
        content2 = ''
        for tag in soup.select('.tag'):
            a = tag.select('a')
            if(len(a)):
                for num in range(len(a)):
                    part2 = (a[num].text)*2
                    content2 = content2 + part2
        content = content1+content2

        with open("sort.txt","a") as f:
            if (i+1)%10==0:
                f.write(name+" "+content+'\n')
            else:
                f.write(name+" "+content)
    print('输出完成')



#searchRankInfo()
#searchSortInfo()
