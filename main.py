from colorama import init, Fore, Back, Style
from cmd import Cmd
import os
import sys
import time
import scan
import scan.scdir
from rich.console import Console

console = Console()



class Client(Cmd):
    prompt = time.strftime('\033[1;31mshell>\033[32m')  # 自定义交互式提示字符串
    intro = time.strftime('\033[1;35mWelcom to XianGsec!\033[36m')

    def __init(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        Cmd.__init__(self)
    
    def do_dir(self, arg):
            if not arg:
                self.help_dir()
            elif os.path.exists(arg):
                print("\n".join(os.listdir(arg)))
            else:
                print("No such pathexists.")

    def help_dir(self):
            print("syntax: dir path -- displaya list of files and directories")

    def emptyline(self):  # 当输入空行的时候
            pass
    
    def do_hello(self, arg):
        print('hello', arg)
    
    def do_install(self):
        scan.scdir.install()

    def do_exit(self, arg):
        print('Bye!')
        return True  # 返回True，直接输入exit命令将会退出
    
    def do_scandir(self,line):
        tar_url = input("\033[1;31m请输入扫描url:\033[32m")
        scan.scdir.scandir(tar_url)
#UI
init(autoreset=True)

class Colored(object):

    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.RED + Back.BLACK + s + Fore.RESET
    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + Back.BLACK + s + Fore.RESET

    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + Back.BLACK + s + Fore.RESET

    #  前景色:蓝色  背景色:默认
    def blue(self, s):
        return Fore.BLUE + Back.BLACK + s + Fore.RESET

    #  前景色:洋红色  背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + Back.BLACK + s  + Fore.RESET 

    #  前景色:青色  背景色:默认
    def cyan(self, s):
        return Fore.CYAN + Back.BLACK + s + Fore.RESET 

    #  前景色:白色  背景色:默认
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    #  前景色:黑色  背景色:默认
    def black(self, s):
        return Fore.BLACK 

    #  前景色:白色  背景色:绿色
    def w_g(self, s):
        return Fore.WHITE  + Back.GREEN + s

    def dave(self, s):
        return Style.BRIGHT + Back.BLACK + Fore.GREEN + s
                                                                                                                                                        

def main():
    space = ' '
    color = Colored()
    print(color.red("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
    print(color.green("@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@"))
    print(color.blue("@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@"))
    print(color.cyan("@@ @@@@@   @@@@@@@@   @@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@"))
    print(color.dave("@@ @@@@@@@  @@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@"))
    print(color.green("@@ @@@@@@@@   @@   @@@@@@  @@@@@      @@@@@@          @@@@  @@@@@@@@@@  @@@@@       @@@@@@@@     @@@@@@@@      @@@@@@ @@"))
    print(color.magenta("@@ @@@@@@@@@     @@@@@@@@  @@@   @@@@   @@@@   @@@@   @@@   @@@@@@@@@@@@@@@@@  @@@@   @@@@  @@@@@  @@@@   @@@@  @@@@@ @@"))
    print(color.yellow("@@ @@@@@@@@@@    @@@@@@@@  @@@@@@@@@@@  @@@@  @@@@@@  @@@   @@@@@        @@@   @@@@@@@@@@  @@@@@@@  @@  @@@@@@@  @@@@ @@"))
    print(color.red("@@ @@@@@@@@@  @   @@@@@@@  @@@@         @@@@  @@@@@@  @@@   @@@@@@@@@@@  @@@@@       @@@@           @@  @@@@@@@@@@@@@ @@"))
    print(color.yellow("@@ @@@@@@@   @@@@  @@@@@@  @@   @@@@@@  @@@@  @@@@@@  @@@@  @@@@@@@@@@   @@@@@@@@@@@  @@@  @@@@@@@@@@@  @@@@@@@@@@@@@ @@"))
    print(color.blue("@@ @@@@@@   @@@@@@   @@@@  @@   @@@@@   @@@@  @@@@@@  @@@@@   @@@@@@@    @@@  @@@@@@  @@@  @@@@@@   @@@  @@@@@  @@@@@ @@"))
    print(color.cyan("@@ @@@@@  @@@@@@@@@   @@@  @@@           @@@  @@@@@@  @@@@@@@           @@@@         @@@@@         @@@@         @@@@@ @@"))
    print(color.green("@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@"))
    print(color.magenta("@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@"))
    print(color.dave("@@@@@@@                                                                                                          @@@@@@@"))


if __name__ == '__main__':
    main()
    client = Client()
    client.cmdloop()
