import numpy as np
import word
import pymysql

def kMeans(dataset, k):
    a = dataset.shape[0]
    b = dataset.shape[1]
    c = int(b/k)
    x = np.zeros((k,b))
    countAll = np.zeros(a)
    for i in range(k):
        for j in range(c):
            x[i][i*c+j] = 1
    while True:
        y = np.zeros((k,b))
        count = np.zeros(k)
        for i in range(a):
            dist = 100
            for j in range(k):
                if np.linalg.norm(dataset[i] - x[j]) < dist:
                    dist = np.linalg.norm(dataset[i] - x[j])
                    num = j
                countAll[i] = num
            y[num] = y[num] + dataset[i]
            count[num] = count[num] + 1
        for i in range(k):
            y[i] = y[i]/count[i]
        if np.linalg.norm(x - y) == 0:
            break
        for i in range(k):
            x[i] = y[i]
    return countAll,count

def classifyDateset(dateset,countAll,count,k):
    Count =[]
    for i in range(len(count)):
        Count.append(count[i])
    for i in range(len(Count)):
        Count[i] = int(Count[i])
    datesetC = [[],[],[],[],[],[]]
    for i in range(len(countAll)):
        for l in range(k):
            if countAll[i] == l:
                datesetC[l].append(dateset[i])
    return datesetC

def getKeyword():
    keyword = []
    db = pymysql.connect("localhost","root","123456","booksrecommendationsystem",charset="utf8" )

    # 浣跨敤cursor()鏂规硶鑾峰彇鎿嶄綔娓告爣
    cursor = db.cursor()

    # SQL 鏌ヨ璇彞
    sql = "SELECT * FROM sortkeywords WHERE skwid = '%d'"
    for i in range(30):
        try:
           # 鎵цSQL璇彞
           cursor.execute(sql%(i+1))
           # 鑾峰彇鎵�鏈夎褰曞垪琛�
           results = cursor.fetchall()
           for row in results:
              keywords = row[1]
              keyword.append(keywords)
        except:
           print ("Error: unable to fetch data")
    # 鍏抽棴鏁版嵁搴撹繛鎺�
    db.close()
    return keyword

def getMax(sum):
    max = 0
    num = 0
    for i in range(len(sum)):
        if sum[i] > max:
            max = sum[i]
            num = i
    return num

def getKeywordNum(dateset,keyword):
    sum = np.zeros((30))
    for i in range(len(dateset)):
        sum = dateset[i] + sum
    num1 = getMax(sum)
    sum[num1] = 0
    num2 = getMax(sum)
    type = keyword[num1] + ','+ keyword[num2]
    return type


def sort_type(countAll,types,labels):
    db = pymysql.connect("localhost","root","123456","booksrecommendationsystem",charset="utf8")
    CountAll = []
    for i in range(len(countAll)):
        CountAll.append(countAll[i])
    for i in range(len(CountAll)):
        CountAll[i] = int(CountAll[i])
    print(len(CountAll))
    # 浣跨敤cursor()鏂规硶鑾峰彇鎿嶄綔娓告爣
    cursor = db.cursor()
    sqlselect ="select BookId from book_rank limit 1"

    cursor.execute(sqlselect)
    bookid2 = cursor.fetchone()
    print(bookid2)
    sql_update ="update book_rank set type = '%s' where BookId = '%d'"
    for i in range(81):
       # try:
        num = CountAll[i]

        cursor = db.cursor()
        cursor.execute(sql_update %(types[num],i+bookid2[0]))
        db.commit()
        #except:
            #print("异常")
           # db.rollback()
    db.close()

def mainKMeans():
    group,labels = word.getArrays()
    dateset = np.array(group)
    k = 6
    countAll,count = kMeans(dateset, k)
    datesetC = classifyDateset(dateset,countAll,count,k)
    keyword = getKeyword()
    types = []
    for i in range(k):
        types.append(getKeywordNum(datesetC[i],keyword))
    sort_type(countAll,types,labels)

def mainKMeans2():
    group,labels = word.getArrays()
    dateset = np.array(group)
    k = 6
    countAll,count = kMeans(dateset, k)
    datesetC = classifyDateset(dateset,countAll,count,k)
    keyword = getKeyword()
    types = []
    for i in range(k):
        types.append(getKeywordNum(datesetC[i],keyword))
    sort_type(countAll,types,labels)
    return types
#mainKMeans()
