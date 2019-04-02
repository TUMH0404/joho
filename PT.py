#################
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

##############
##############

def Posture_Move():
    ## 定義 ##

    bodymove = {"仰臥位":None,"座位":None,"立位":None,"起き上がり":None,"立ち上がり":None}


    for qq in bodymove.keys():
        nv = 0
        coment = whiledef(f"{qq}について....{nv}\n")

        nv+=1;

        bodymove[qq] = coment


    return bodymove



######################################
###########    ROM   #################
######################################
def str2num(strname):

    while(1):

        r = input(strname)
        if r.isdigit():
            result = int(r)
            break
        elif r=="q":
            result = None
            break
        else:
            if "." in r and r.replace(".","").isdigit():
                result = float(r)
                break

    return result

## ROM1upper  ###
def ROM_UE():
    '''
    上肢のROMテストの結果を入力する
    返り値は辞書形式
    '''
    ##運動方向と関節部位の関連を定義する
    J_motion3L = {"屈曲":None,"伸展":None,"内転":None,"外転":None,"内旋":None,"外旋":None}
    J_motion2L = {"背屈":None,"掌屈":None,"橈屈":None,"尺屈":None}
    J_motion1L = {"屈曲":None,"伸展":None}
    J_motion4L = {"回内":None,"回外":None}
    J_motion3R = J_motion3L.copy()
    J_motion2R = J_motion2L.copy()
    J_motion1R = J_motion1L.copy()
    J_motion4R = J_motion4L.copy()

    J_jointL = {"肩":J_motion3L,"肘":J_motion1L,"手":J_motion2L,"前腕":J_motion4L}
    J_jointR = {"肩":J_motion3R,"肘":J_motion1R,"手":J_motion2R,"前腕":J_motion4R}

    ## 上記の部位と左右の定義
    JR,JL = J_jointR.copy(),J_jointL.copy()
    ROM_LR = {"L":JL,"R":JR}

    ################################

    for u in ROM_LR.keys():
        for i in ROM_LR[u].keys():
            for k in ROM_LR[u][i].keys():
                RR = str2num(f"({u}{i})_{k}....")
                ROM_LR[u][i][k] = RR

            else:
                continue
            break
        else:
            continue
        break
    return ROM_LR

#############

## ROM lower ##
def ROM_LE():
    ##定義
    J_motion3L = {"flex":None,"ext":None,"add":None,"abd":None,"e-rot":None,"i-rot":None}
    J_motion2L = {"d-f":None,"p-f":None}
    J_motion1L = {"flex":None,"ext":None}
    J_motion3R = J_motion3L.copy()
    J_motion2R = J_motion2L.copy()
    J_motion1R = J_motion1L.copy()

    J_jointL = {"Hip":J_motion3L,"Knee":J_motion1L,"Ankle":J_motion2L}
    J_jointR = {"Hip":J_motion3R,"Knee":J_motion1R,"Ankle":J_motion2R}

    ## 上記の部位と左右の定義
    JR,JL = J_jointR.copy(),J_jointL.copy()
    ROM_LR = {"L":JL,"R":JR}

    for u in ROM_LR.keys():
        for i in ROM_LR[u].keys():
            for k in ROM_LR[u][i].keys():
                RR = str2num(f"({u}{i})_{k}....")
                ROM_LR[u][i][k] = RR

            else:
                continue
            break
        else:
            continue
        break
    return ROM_LR


##  MMT  ##
def MMT_part1(mmt):
    '''
    入力のためのプログラム
    '''
    ##
    MMT_LR = {"L":None,"R":None}
    for k in MMT_LR.keys():
        name = mmt
        for i in name.keys():
            RR = input(f"MMT_{k}_{i}....")
            if len(RR)==0:
                name[i]="----"
            else:
                name[i]=RR

        MMT_LR[k] = name

    return MMT_LR


def MMT_TEST():
    '''
    上肢帯，上肢，下肢のMMT結果を入力する
    '''
    girdle_muscles={"僧帽筋(Trapezius)":None,"三角筋(Deltoid)":None,\
                "棘上筋(Supraspinatous)":None,"棘下筋(Infraspinatous)":None,\
                "菱形筋(Rhomboids)":None, "大胸筋(Pectralis major)":None,\
                "大円筋(Teres major)":None, "広背筋(Latissimus dorsi)":None}

    upper_extremity_muscles={"上腕二頭筋(Biceps brachii)":None,"上腕三頭筋(Triceps brachii)":None,\
                            "腕橈骨筋(brachio radialis)":None,"手関節屈筋群(wrist flexors)":None,\
                            "手関節伸筋群(wrist extensors)":None,"指関節屈筋群(digi flexors)":None,\
                            "指関節伸筋群(digi extensors)":None,"長母指外転筋(abductor pollicis longus)":None,\
                            "母指内転筋(adductor pollicis)":None,"短母指外転筋(abduttor pollicis brevis)":None}

    lower_extremity_muscles={"内転筋群(adductors of thigh)":None,"外転筋群(abdutors of thigh)":None,\
                            "腸腰筋(iliopsoas)":None,"大腿四頭筋(quadriceps)":None,\
                            "膝関節屈筋群(hamstrings)":None,"前脛骨筋(Tibial Anterior)":None,\
                            "下腿三頭筋 (triceps surae)":None,"長母趾伸筋(Extensor hallucis longs)":None}
    ###########################
    MMT_name = {"上肢帯":girdle_muscles,"上肢":upper_extremity_muscles,"下肢":lower_extremity_muscles}
    while(1):
        for nn in MMT_name.keys():
            qq0 = input(f"{nn}のMMTを記録しますか？\n はい---y，いいえ---n \n")
            if qq0== 'y':
                MMT_name[nn]=MMT_part1(MMT_name[nn])

            elif qq0 == 'n':
                pass

            qq1 = input("記録を終えますか？\n はい---y，いいえ---n \n")
            if qq1 == 'y':
                break
            else:
                pass

        qq2 = input("もう一度やり直しますか？\n はい---y，いいえ---n \n")
        if qq2 == 'y':
            continue
        else:
            break

    return MMT_name


####################
####################
####################
def TER():
    RL = {"R":{"上肢":{"上腕二頭筋":None,"上腕三頭筋":None,"大胸筋":None},\
               "下肢":{"大腿四頭筋":None,"内転筋群":None,"アキレス腱":None}},
          "L":{"上肢":{"上腕二頭筋":None,"上腕三頭筋":None,"大胸筋":None},\
                     "下肢":{"大腿四頭筋":None,"内転筋群":None,"アキレス腱":None}}}

    print("腱反射の結果")
    for k in RL.keys():
        for i in RL[k].keys():
            for u in RL[k][i].keys():
                RR = input(f"{k}_{u}...\n'+' or '-' or '++' or '+-'\n")
                RL[k][i][u] = RR

    return RL
    print("succsess")
