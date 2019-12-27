import sys

def greaux(strng):
    # длинна проги
    a = len(strng)
  
    print "* &l: " , str(hex(id(a))).upper()[2:], ", l: ",a
    print strng, "^ &l: " , str(hex(id(a))).upper()[2:], ", l: ",a

# запуск скрипта
if __name__ == "__main__":
    greaux(sys.argv[1])
