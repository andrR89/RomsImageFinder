import time
import urllib2
import simplejson
import ImageSize
import glob


def baixar(nomeArquivo):
    for i in glob.glob("/home/andre/Workspaces/pycharm/RomsImageFinder/images/*"):
        nomeArquivoDir = i.split('/')[-1]
        if nomeArquivoDir.find(nomeArquivo.replace(".smc", "")) == 0:
            print("[Ja Baixado]")
            return False
    return True


def getImage(searchTerm, console, formato):
    imageName = searchTerm + " box art " + console
    imageName = imageName.replace(formato, "")
    searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=2.0&q=" + imageName.replace(" ", "%20")+"&as_filetype=jpeg&start=4"
    nomeArquivoImagem = str("images/" + searchTerm + '.jpeg').replace(formato, "")
    request = urllib2.Request(searchUrl)
    response = urllib2.urlopen(request, timeout=10)
    if baixar(searchTerm):
        dowload(response, nomeArquivoImagem)
    response.close()


def dowload(response, nomeArquivoImagem):
    deserialized_output = simplejson.load(response)

    flag = True
    aux = 0
    error = False
    while flag:
        try:
            imageUrl = deserialized_output['responseData']['results'][aux]['unescapedUrl']
            print imageUrl
            if imageUrl.find(".gif") == -1 and imageUrl.find("emuparadise") == -1:
                arq = open(nomeArquivoImagem, 'wb')
                arq.write(urllib2.urlopen(imageUrl).read())
                arq.close()
                flag = False
            aux = aux + 1
        except Exception:
            print("[error tentando outro] " + str(aux))
            aux = aux + 1
            print(deserialized_output)
            if aux == int(10):
                error = True
                print("[Nao eh possivel baixar imagem para ] " + nomeArquivoImagem + "] ")
                #time.sleep(120)
                break

    if not error:
        ImageSize.resize(nomeArquivoImagem)
        print "[OK]"
