# coding: utf-8

import random

def str2list(df):
    tt = df.split("\n")
    tt = [i.split("\t") for i in tt]
    return tt

def list2dic(data):
    dicdata = {}
    for k,i in enumerate(data):
        u = {"筋名":None,"起始":None,"停止":None,"神経":None,"作用":None}
        u["筋名"]=i[0]
        u["起始"]=i[1]
        u["停止"]=i[2]
        u["神経"]=i[3]
        u["作用"]=i[4]
        dicdata.update({k:u})

    return dicdata


def ssss(qq,numbersel,l=["停止",'起始','神経','作用'],c= "筋名"):

    kkk = qq
    answer = 0
    mm = random.sample(list(range(len(kkk))),len(kkk))
    for n in mm:
        aaaa = []
        bbbb = []
        # 何を問う？
        ab=random.choice(l)
    
        # 解答肢の選択
        ccc = list(kkk.keys())
        mm2 = random.sample(ccc,len(ccc))
        for u,i in enumerate(mm2):
            if kkk[n][ab]==kkk[i][ab]:
                bbbb.append(i)
            
        # 選択肢の選択
        for a in bbbb:
            mm2.remove(a)
        samp = random.sample(mm2,numbersel)   ##### 選択肢の数を変更する。
    
        # 選択肢の作成
        for aa in bbbb:
            ll = random.choice(range(len(samp)))
            samp.insert(ll,aa)
        
        # 問題の作成
        num = [samp.index(i)+1 for i in bbbb]
        for uu,i in enumerate(samp):
            aaaa.append(f"{uu+1}__{kkk[i][c]}")
        #print("###",samp,bbbb,num)######
        print("\n".join(aaaa))
    
        # 問い
        for st in range(len(num)):
            if st==0:
                string = f'Q:{ab}が"{kkk[n][ab]}"の{c}:\n'
            else:
                string = f'それと・・・・:\n'
            tt = input(string) 
            if int(tt) in num:
                num.remove(int(tt))
        
    
        if len(num)==0:
            print("正解!!!")
            answer = answer + 10
            
        else:
            print("wrong")
            for i in bbbb:
                print(f"正解：{kkk[i][c]}")
    
        input("Enter キーを押して次へ進む\n")
        print("\n\n") 

    print(f"今回の結果・・・・\n {answer}  点！！")
    return answer