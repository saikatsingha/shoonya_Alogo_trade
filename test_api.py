from api_helper import ShoonyaApiPy
import logging
 
#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = ShoonyaApiPy()
#print(api)

#credentials
user    = input("Enter your User ID: ")
pwd     = input("Enter your Password: ")
factor2 = input("Enter your PAN: ")
vc      = 'FA164640_U'
app_key = input("Enter your API Key: ")
imei    = 'abc1234'

print(user, pwd, factor2, app_key)
#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

print(ret)