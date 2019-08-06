import csv
from osint_sources.tinder import *
from osint_sources.model import *
from osint_sources.google import *
from osint_sources.twitter import *
from osint_sources.facebook import *
from osint_sources.instagram import *
from osint_sources.boe import *
from osint_sources.yandex import *


def tinder(token):

	#start_tinder_scrap
	scan=Tinder()
	authtk=scan.get_auth_token(token)

	print(authtk)
	unique_list_ids=[]
	#load existent ids from database
	unique_list_ids=User.getIds()
	print(len(unique_list_ids))

	while True:
		response=scan.getUserInfo()
		if 'error' in response:
			if response['msg']=='limit rate':
				break
			elif response['msg']=='no data':
				print('no data')
				break
		else:
			if response == "Error":
				break
			ids=response['ids']
			data=response['data']
			differents= list(set(ids) - set(unique_list_ids))
			unique_list_ids.extend(differents)
			for d in differents:
				userInfo = [usr['user_info'] for usr in data if usr['id']==d]
				for user in userInfo:
					User.insertUser(user)
				scan.diskike_users(userInfo)
			print(len(unique_list_ids))



def yandex_scrapper(name,img,token):
	yandex(name,img,token)


def linkedin():
	pass


def google_scrapper(toSearch,place,knownImage):
	google(toSearch,place,knownImage)


def twitter_scrapper(name,size):
	twitter(name,size)

def facebook_scrapper(name,knownImage):
	facebook(name,knownImage)

def instagram_scrapper(name,knownImage):
	instagram(name,knownImage)

def boe_scrapper(toSearch,initDate,finalDate,size,explicit):
	if explicit==None:
		explicit=True
	boe(toSearch,initDate,finalDate,size,explicit)