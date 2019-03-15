
import PT

class PT_TESTs:
    def __init__(self):
        self.ID = ""
        self.result_ROM_UE=None
        self.result_ROM_LE=None


    def IDinput(self):
        self.ID = input("your id:")

    def IDprint(self):
        print(self.ID)

    def ROM_Upper(self):
        self.result_ROM_UE = PT.ROM_UE()

    def ROM_Lower(self):
        self.result_ROM_LE = PT.ROM_LE()

    def MMT_Test(self):
        self.result = PT.MMT_TEST()

    def TER_test(self):
        return PT.TER()

    def Movements(self):
        PT.Posture_Move()

    def show_result(self):
        print(self.result_ROM_UE)
        print(self.result_ROM_LE)


if __name__=="__main__":
#def Start():

    a = PT_TESTs()
    b=a.TER_test()
    print(b)
    print("IDを入力してください。\n")
    a.IDinput()
    a.IDprint()
    com = input("上肢のROMをしましたか？\nはい---y，いいえ---n\n")
    if com=="n":
        pass
    elif com=="y":
        a.ROM_Upper()

    com1 = input("下肢はしましたか？\nはい---y，いいえ---n\n")
    if com1=="n":
        pass
    elif com1=="y":
        a.ROM_Lower()

    com1 = input("動作や姿勢を観察しましたか？\nはい---y，いいえ---n\n")
    if com1=="n":
        pass
    elif com1=="y":
        a.Movements()


    a.show_result()
