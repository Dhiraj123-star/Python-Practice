from mod1 import zoo
class Boo:
    def goo(self)->None:
        zoo()

def main():
    b=Boo()
    b.goo()

if __name__=='__main__':
    main()