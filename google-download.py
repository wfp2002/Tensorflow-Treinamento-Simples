# -*- coding: latin-1 -*-
from google_images_download import google_images_download

#Google download Images
def downloadImages(s):
    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = {"keywords":str(s),"size":"medium", "limit":100,"format":"jpg","print_urls":True}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)


####INICIO
s = input('Digite sua busca: ')


downloadImages(s)
