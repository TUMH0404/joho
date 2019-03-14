########

### 動作観察  #####

def whiledef(text,n=0):
    '''
    動作観察を入力するためのプログラム
    終わるときは"y"のみを入力してEnterをおす。
    それ以外は，文字を入力する。
    testoo
    '''
    rrr=""
    while(1):
        rr = input(text+str(n))
        if rr=="y":
            break
        else:
            n=n+1
            rrr=rrr+rr+'\n'

    return rrr



def Posture_Move():
    ## 定義 ##

    bodymove = {"仰臥位":None,"座位":None,"立位":None,"起き上がり":None,"立ち上がり":None}


    for qq in bodymove.keys():
        nv = 0
        coment = whiledef(f"{qq}について....{nv}\n")
 
        nv+=1;       
            
        bodymove[qq] = coment
        
    
    return bodymove
