
import PT

class PT_TESTs:
    def __init__(self):
        self.ID = ""
        self.result=None

    def IDinput(self):
        self.ID = input("your id:")

    def IDprint(self):
        print(self.ID)

    def ROM_Upper(self):
        self.result = PT.ROM_UE()


if __name__=="__main__":
    #a = PT_TESTs()
    #a.IDinput()
    #a.IDprint()
    #a.ROM_Upper()
    #print(a.result)
    while(1):

        r = input("test")
        if r.isdigit():
            print(int(r))
            break
        elif r=="q":
            break
        else:
            if "." in r and r.replace(".","").isdigit():
                print(float(r))
                break
