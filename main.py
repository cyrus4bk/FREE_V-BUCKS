import os, time, secrets, random
from pystyle import *

banner = Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"""

  ┌─────────────────────────────────────────┐
  │                                         │
  │ REJOIDN MON DISCORD discord.gg/cAJs68Ub │
  │                                         │
  └─────────────────────────────────────────┘

"""))

banner1 = Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"""



  ╔═══════════════════════════════════════════════════════════════════╗
  ║                                                 █       █         ║
  ║   ████████    █      █ ██████    █     █ ██████ ██    ███  ██████ ║
  ║   █           ██    ██ █    ██   █     █ █      ██  ████   █      ║
  ║   ████         █    █  █     █   █     █ █      ██████     ██     ║
  ║   █            ██   █  █  ███    █     █ █      ████       ████   ║
  ║   █     █████   █  ██  █ ████    █     █ █      ████         ███  ║
  ║   █             ██ █   █    ███  █     █ █      ██  ██         █  ║
  ║   █              ███   █      ██ █     █ ██     ██   ██       ██  ║
  ║   █               █    █████████ ███████ ██████ ██    ██  █████   ║
  ║                                                                   ║
  ║                                                                   ║
  ║  by cyrusbk#3630                                                  ║
  ╚═══════════════════════════════════════════════════════════════════╝


[+] Free v-bucks ?

[+] Free Robux ?

[+] Free Nitro ?

> """))

Screen = Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"""
T Stupid :) ?

> """))

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
hit=0
fail=0
os.system('cls' if os.name == 'nt' else 'clear')


 
choice = int(input(banner1+" "))

if choice not in [1,2]:
    os.system('cls' if os.name == 'nt' else 'clear')
    input(Screen)
