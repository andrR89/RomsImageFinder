import urllib2
import simplejson
import ImageSize


def getImage(searchTerm, console, formato):
    imageName = searchTerm + " box art " + console
    imageName = imageName.replace(formato, "")
    fetcher = urllib2.build_opener()
    searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + imageName.replace(" ", "%20")

    f = fetcher.open(searchUrl)
    deserialized_output = simplejson.load(f)

    print deserialized_output

    flag = True
    nomeArquivoImagem = str("images/" + searchTerm + '.jpeg').replace(formato, "")
    arq = open(nomeArquivoImagem, 'wb')
    aux = 0

    while flag:
        try:
            imageUrl = deserialized_output['responseData']['results'][aux]['unescapedUrl']
            arq.write(urllib2.urlopen(imageUrl).read())
            flag = False
        except Exception:
            aux += 1

    print(imageUrl)
    arq.close()

    ImageSize.resize(nomeArquivoImagem)

