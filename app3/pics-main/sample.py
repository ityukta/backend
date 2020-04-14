import base64
 
with open("suman.jpg", "rb") as imageFile:
    st = base64.b64encode(imageFile.read())
    print(st)
    print("abfhea")