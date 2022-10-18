import os
import sys
import time
import argparse
from pyfiglet import Figlet
from rich.console import Console
import telnetlib
import threading

lock = threading.Lock()

def install():
    os.system("pip3 install -r main/requirements.txt --user")
   
def scandir(tar_url):
    os.system("python scan/dirsearch/dirsearch.py -u " + tar_url)
    
