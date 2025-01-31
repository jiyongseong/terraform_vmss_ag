from configparser import SafeConfigParser
#from logconfig import logger
import requests, json 

config = SafeConfigParser()
#loading config file
config.read('config.ini')

imds_url = config.get('imds', 'imds_url')
response = requests.get(imds_url, headers={"Metadata":"true"})
response_txt = json.loads(response.text)
print('Original Response : {}'.format(response_txt))
#populate required instance variables
vmId = response_txt['vmId']
name = response_txt['name']
location = response_txt['location']
subscriptionId = response_txt['subscriptionId']
vmScaleSetName = response_txt['vmScaleSetName']
resourceGroupName = response_txt['resourceGroupName']
#print('ResourceGroupName: {}'.format(resourceGroupName))
tags = response_txt['tags']
deleteTag = config.get('imds', 'pending_delete_tag')
if deleteTag in tags:
    print('Tag information found : {}'.format(tags))
else:
    print('There is no matching')
#populate access_token
accesstoken_url = config.get('imds', 'accesstoken_url')
#print('accesstoken_url : {}'.format(accesstoken_url))
access_token_response = requests.get(accesstoken_url, headers={"Metadata":"true"})
access_token_text = json.loads(access_token_response.text)
access_token = access_token_text['access_token']
#print('My access_token {}:'.format(access_token))
