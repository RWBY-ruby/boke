def tran(x=[]):
    tranDict={
        '零':0,
        '一':1,
        '二':2,
        '三':3,
        '四':4,
        '五':5,
        '六':6,
        '七':7,
        '八':8,
        '九':9,
        '十':10,
        0:'零',
        1:'一',
        2:'二',
        3:'三',
        4:'四',
        5:'五',
        6:'六',
        7:'七',
        8:'八',
        9:'九',
        10:'十',
    }
    return tranDict[x]

def runSentence(sen=[],var={}):
    #创建变量
    if sen[0]=='整数' and sen[2]=='等于':
        var[sen[1]]=tran(sen[3])
    #变量计算
    if sen[0] in var:
        if sen[1]=='等于':
            var[sen[0]]=tran(sen[2])
        if sen[1]=='增加':
            var[sen[0]]+=tran(sen[2])
        if sen[1]=='减少':
            var[s1[i][0]]-=tran(sen[2])
    #变量输出
    elif sen[0]=='看看':
        if sen[1][0]=='“' and sen[1][-1]=='”':
            print(sen[1][1:-1])
        else:
            print(tran(var[sen[1]]))
    #变量判断
    elif sen[0]=='如果':
        c=[]
        a=[]
        b=[]
        j=0
        while j<len(sen):#c
            j+=1
            if sen[j]=='则':
                break
            c.append(sen[j])
        while j<len(sen):#a
            j+=1
            if sen[j]=='否则':
                break
            a.append(sen[j])
        b=sen[j+1:]#b
        if c[1]=='大于':
            if var[c[0]]>tran(c[2]):
                runSentence(a,var)
            else:
                runSentence(b,var)
        if c[1]=='小于':
            if var[c[0]]<tran(c[2]):
                runSentence(a,var)
            else:
                runSentence(b,var)
        if c[1]=='等于':
            if var[c[0]]==tran(c[2]):
                runSentence(a,var)
            else:
                runSentence(b,var)
        if c[1]=='大于等于':
            if var[c[0]]>=tran(c[2]):
                runSentence(a,var)
            else:
                runSentence(b,var)
        if c[1]=='小于等于':
            if var[c[0]]<=tran(c[2]):
                runSentence(a,var)
            else:
                runSentence(b,var)

word=''
words=''
sentence=[]
sentences=[]
#---------------------------------------------------------
print('请输入您要输入的中文，输入“结束”结束编程')
while(True):
    words=input()
    if(words=='结束'):
        break
    sentence=words.split(' ')
    sentences.append(sentence)
#---------------------------------------------------------
s1=sentences
tmp=s1
#print(s1)
word=''
words=''
sentence=[]
sentences=[]
s1=tmp
var={}
for i in range(len(s1)):
    runSentence(s1[i],var)
