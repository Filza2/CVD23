import os
print("""
                                  .
     .              .   .'.     \   /
   \   /      .'. .' '.'   '  -=  o  =-
 -=  o  =-  .'   '              / | /
   / | \                          |
     |                            |
     |                            |
     |                      .=====|
     |=====.                |.---.|
     |.---.|                ||=o=||
     ||=o=||                ||   ||
     ||   ||                ||   ||
     ||   ||                ||___||
     ||___||                |[:::]|
     |[:::]|                '-----'
     '-----'

Don't Trust anyone/anything , including your internet connection ...\t\n\n-Filza
""")
try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('clear')
try:
    import time
except ModuleNotFoundError:
    os.system('pip install time')
    os.system('clear')
try:
    import platform
except ModuleNotFoundError:
    os.system('pip install platform')
    os.system('clear')
try:
    import colorama
except ModuleNotFoundError:
    os.system('pip install colorama')
    os.system('clear')
os.system('python3 CVD-23.py')
