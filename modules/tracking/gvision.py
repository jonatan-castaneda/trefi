import io
import os
import re
from google.cloud import vision
from django.shortcuts import render, redirect

def getInformacion(url="media/tickets/ticket.png"):
    # Imports the Google Cloud client library

    # Instantiates a client
    vision_client = vision.Client()

    # The name of the image file to annotate
    file_name = os.path.join(os.getcwd(),url)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

    # Performs label detection on the image file
    text = image.detect_text()

    regexp = re.compile(r'([Tt][Oo][Tt][Aa][Ll])')
    regdate = re.compile(r'(([0-9]+)/([0-9]+)/([0-9]+))')
    regtotal = re.compile(r'([0-9]+(\.[0-9][0-9]?)?)')

    f = open("test.txt", "w")
    f.write(text[0].description)
    f.close

    b = False
    with open("test.txt") as f:
        for line in f:
            if b:
                total = line
                break
            match = regexp.match(line)
            if match:
                b=True
                total = line
                if regtotal.match(total):
                    print(total)
                    break
                #print (match.group(1))
    print("Total = %s" % (total))

    b = False
    with open("test.txt") as f:
        for line in f:
            if b:
                break
            match = regdate.findall(line)
            if match:
                b=True
                #print (match.group(1))
                fecha = match
    print("Fecha = %s" % (str(fecha[0][0])))

    with open("test.txt") as f:
        for line in f:
            descripcion = line
            break
    print("Descripcion = %s" % (descripcion))
    return render({
        'fecha': fecha[0][0],
        'descripcion': descripcion,
        'total': total,
    })
    #print('Text:')
    #print(text[0].description)
