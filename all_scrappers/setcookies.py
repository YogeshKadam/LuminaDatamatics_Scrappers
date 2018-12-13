

#convert cookies
from Cookie import SimpleCookie

Cookie11 = 'Cookie: akavpau_p6=1492510799~id=bad5a5f677b9c92fd22ae7ce69a953d7; search.perf.metric=timerPromiseAll=404ms|timerHeaderAction=53ms|timerSearchAction=404ms|timerFooterAction=26ms|timerPreso=402ms; akavpau_p3=1492510790~id=d7334d155b9d5313f20c6c8b19e356d7; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1492510198882; DL=98105%2C47.66059875488281%2C-122.29190063476562%2Cip%2C98105%2CUSA%2CWA; prefper=PREFSTORE~13098~2PREFCITY~1Bellevue~2PREFFULLSTREET~115063%20Main%20St~2PREFSTATE~1WA~2PREFZIP~198105; bstc=ZYcj-sZzb56LzolJAq24WY; NSID=3098.8-5939.8-5678.13-2594.13-2516.13-2317.16-5195.16-3053.18-5272.18-2325.19-5628.21-5073.22-2571.23-2385.25-3794.25-3801.29-2595.29-4137.30-3537.34-3757.34; vtc=ZYcj-sZzb56LzolJAq24WY; exp-ck=vOXNpEqkz0MWIxT; exp=0%2B1492510198%2BZYcj-sZzb56LzolJAq24WY%2B0%2BCcvJB.vOXNp|K8foX.Eqkz0|VxHIY.MWIxT; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1492510198883@firstcreate:1492510198883"'	

output = {'akavpau_p6':'1492510799~id=bad5a5f677b9c92fd22ae7ce69a953d7', 'search.perf.metric':'timerPromiseAll=404ms|timerHeaderAction=53ms|timerSearchAction=404ms|timerFooterAction=26ms|timerPreso=402ms', 'akavpau_p3':'1492510790~id=d7334d155b9d5313f20c6c8b19e356d7', 'AID':'wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1492510198882', 'DL':'98105%2C47.66059875488281%2C-122.29190063476562%2Cip%2C98105%2CUSA%2CWA', 'prefper':'PREFSTORE~13098~2PREFCITY~1Bellevue~2PREFFULLSTREET~115063%20Main%20St~2PREFSTATE~1WA~2PREFZIP~198105', 'bstc':'ZYcj-sZzb56LzolJAq24WY', 'NSID':'3098.8-5939.8-5678.13-2594.13-2516.13-2317.16-5195.16-3053.18-5272.18-2325.19-5628.21-5073.22-2571.23-2385.25-3794.25-3801.29-2595.29-4137.30-3537.34-3757.34', 'vtc':'ZYcj-sZzb56LzolJAq24WY', 'exp-ck':'vOXNpEqkz0MWIxT', 'exp':'0%2B1492510198%2BZYcj-sZzb56LzolJAq24WY%2B0%2BCcvJB.vOXNp|K8foX.Eqkz0|VxHIY.MWIxT', 'com.wm.reflector':'"reflectorid:0000000000000000000000@lastupd:1492510198883@firstcreate:1492510198883"'}

cookie = SimpleCookie()
cookie.load(Cookie11)

cookies12 = {}
for key, morsel in cookie.items():
    cookies12[key] = morsel.value
	
print cookies12