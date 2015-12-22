import time
import urllib2
import urllib
import simplejson
import ImageSize
import re
import glob
import json


def baixar(nomeArquivo,formato):
    for i in glob.glob("/home/andre/Workspaces/pycharm/RomsImageFinder/images/*"):
        nomeArquivoDir = i.split('/')[-1]
        if nomeArquivoDir.find(nomeArquivo.replace(formato, "")) == 0:
            print("[Ja Baixado]")
            return False
    return True


def getImage(searchTerm, console, formato):
    search_type='Image'
    imageName = searchTerm + " "+ console
    imageName = imageName.replace(formato, "")
    imageName = re.sub(r'\([^)]*\)', '', imageName)


    key= '+5I38bgcL34rRSRBblkPV8dPrRUJiUQL4Yt7ufdNP2Y'
    query = urllib2.quote(imageName)
    # create credential for authentication
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'

    if baixar(searchTerm, formato):
        request = urllib2.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        response = request_opener.open(request)
        response_data = response.read()
        nomeArquivoImagem = str("images/" + searchTerm + '.jpeg').replace(formato, "")
        dowload(response_data, nomeArquivoImagem)
        response.close()


def dowload(response, nomeArquivoImagem):
    json_result = json.loads(response)
    result_list = json_result['d']['results']
    print(result_list)
    flag = True
    aux = 0
    error = False
    while flag:
        try:
            imageUrl = result_list[aux]['MediaUrl']
            print imageUrl
            if imageUrl.find(".gif") == -1 and imageUrl.find(".png") == -1  and imageUrl.find("emuparadise") == -1 and imageUrl.find("ebayimg") == -1:
                arq = open(nomeArquivoImagem, 'wb')
                arq.write(urllib2.urlopen(imageUrl).read())
                arq.close()
                flag = False
            aux = aux + 1
        except Exception:
            print("[error tentando outro] " + str(aux))
            aux = aux + 1
            print(result_list)
            if aux == int(10):
                error = True
                print("[Nao eh possivel baixar imagem para ] " + nomeArquivoImagem + "] ")
                #time.sleep(120)
                break

    if not error:
        ImageSize.resize(nomeArquivoImagem)
        print "[OK]"
