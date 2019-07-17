import jieba
import jieba.analyse
import xlwt #写入Excel表的库
from collections import Counter
import pymysql

#分词筛选分类关键字
def sort():
    #jieba.analyse.set_idf_path("word.txt")
    jieba.analyse.set_stop_words("stop.txt")
    wbk = xlwt.Workbook(encoding = 'ascii')
    sheet = wbk.add_sheet("wordCount")#Excel单元格名字
    key_list=[]
    word_dict= {}
    lyk = []
    word_lst = []
    result = []
    for line in open('sort.txt'):#.txt是需要分词统计的文档
        item  = line.strip('\n\r').split('\t') #制表格切分
        data = jieba.analyse.extract_tags(item[0], topK=5, withWeight=False, allowPOS=('nv'))
        result = result+data
        result[4] = '玄幻'
    return result

#数据库写入分类关键字
def sort_db():
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_SelectAll = """select * from SortKeyWords"""
    cur.execute(sql_SelectAll)
    if cur.execute(sql_SelectAll) == 0:
        for i in range(int(len(sort()))):
            skwid = str(i+1)
            skw = sort()[i]
            sql_Insert= "INSERT INTO SortKeyWords (skwid,skw) VALUES ('"+skwid+"','"+skw+"')"
            cur.execute(sql_Insert)
            db.commit()
    else:
        sql_Delete = "delete from SortKeyWords"
        cur.execute(sql_Delete)
        db.commit()
        for i in range(int(len(sort()))):
            skwid = str(i+1)
            skw = sort()[i]
            sql_Insert= "INSERT INTO SortKeyWords (skwid,skw) VALUES ('"+skwid+"','"+skw+"')"
            cur.execute(sql_Insert)
            db.commit()

    print("更新完成")
    db.close()

def searchKeywords():
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_SelectKeyWord = """select * from SortKeyWords"""
    cur.execute(sql_SelectKeyWord)
    KeyWords = []
    for r1 in cur:
        KeyWords.append(str(r1[1]))
        db.commit()
    #寻找每本书关键字出现次数
    sql_SelectBook = """select * from Book_Rank"""
    cur2 = db.cursor()
    cur2.execute(sql_SelectBook)
    for r2 in cur2:
        BookName = str(r2[1])
        bid = r2[0]
        #print(bid)
        for line in open(BookName+'.txt'):
            for j in range(int(len(KeyWords))):
                count = str(line.count(KeyWords[j]))
                a = 'KeyWord'+str(j+1)
                sql_Updata = "update Book_Rank set "+a+" = "+count+" where BookId = "+str(bid)
                cur3 = db.cursor()
                cur3.execute(sql_Updata)
                db.commit()
    print("搞定！！！！")
    db.close()


def getArrays():
    #打开数据库连接
    db= pymysql.connect(host="localhost",user="root",
    password="123456",db="booksrecommendationsystem",charset="utf8")
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    sql_SelectAll = """select * from Book_Rank"""
    cur.execute(sql_SelectAll)
    arrays = []
    names = []
    for r in cur:
        name = r[1]
        array = []
        for i in range(30):
            array.append(int(r[i+3]))
        db.commit()
        arrays.append(array)
        names.append(name)
    return arrays,names


#sort_db()
#searchKeywords()
