def savehtml(filename,content):
    path = ""+filename+".html"
    file = open(path,"w",encoding="utf8")
    file.write(content)
    file.close()