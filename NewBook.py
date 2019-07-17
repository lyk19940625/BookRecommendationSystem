import requests
from bs4 import BeautifulSoup
import pymysql
import jieba
import jieba.analyse



def searchBookInfo(url):
   #打开数据库连接
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    cur = db.cursor()
    sql_DeleteNewBook = "delete from NewBook"
    cur.execute(sql_DeleteNewBook)
    db.commit()
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    name = soup.title.text.split('_')[0]
    print(name)
    cur2 = db.cursor()
    sql_Insert= "INSERT INTO NewBook (name,href) VALUES ('"+name+"','"+url+"')"
    cur2.execute(sql_Insert)
    db.commit()
    content1 = ''
    index = 0
    for catalog in soup.select('.volume'):
        for li in catalog.select('li'):
            if index < 20:
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
    db.close()


def searchKeywords():
     #打开数据库连接
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    cur = db.cursor()
    sql_SelectKeyWord = """select * from SortKeyWords"""
    cur.execute(sql_SelectKeyWord)
    KeyWords = []
    for r1 in cur:
        KeyWords.append(str(r1[1]))
        db.commit()
    sql_SelectBook = """select * from NewBook"""
    cur2 = db.cursor()
    cur2.execute(sql_SelectBook)
    for r2 in cur2:
        BookName = str(r2[1])
        BookId = str(r2[0])
        for line in open(BookName+'.txt'):
            for j in range(int(len(KeyWords))):
                count = str(line.count(KeyWords[j]))
                a = 'KeyWord'+str(j+1)
                sql_Updata = "update NewBook set "+a+" = "+count+" where NewBookId = "+BookId
                cur3 = db.cursor()
                cur3.execute(sql_Updata)
                db.commit()
    print("搞定！！！！")
    db.close()

def getArray():
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_SelectAll = """select * from NewBook"""
    cur.execute(sql_SelectAll)
    for r in cur:
        array = []
        for i in range(30):
            array.append(int(r[i+3]))
        db.commit()
    return array


def search(bookName):
        res = requests.get('https://www.qidian.com/search?kw='+bookName)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        for bookInfo in soup.select('.book-mid-info'):
            a = bookInfo.select('a')
            p = bookInfo.select('p')
            info = p[1].text
            name = a[0].text
            href = a[0].get('href')
            break
        book = {"name":name,"href":href,"info":info.strip()}
        return book



#searchBookInfo("https:"+search("两界真武")["href"])
#searchKeywords()
