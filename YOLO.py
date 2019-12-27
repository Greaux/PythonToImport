import sys

def greaux(strng):
    # dlinna progi
    a = len(strng)
  
    print "* &l: " , str(hex(id(a))).upper()[2:], ", l: ",a
    print strng, "^ &l: " , str(hex(id(a))).upper()[2:], ", l: ",a

# zapusk scripta
if __name__ == "__main__":
    greaux(sys.argv[1])
