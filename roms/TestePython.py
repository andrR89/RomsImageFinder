# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
 
def main():
    query = "sunshine"
    print bing_search(query, 'Web')
    print bing_search(query, 'Image')
 
def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= '+5I38bgcL34rRSRBblkPV8dPrRUJiUQL4Yt7ufdNP2Y'
    query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    print result_list
    return result_list
 
if __name__ == "__main__":
    main()