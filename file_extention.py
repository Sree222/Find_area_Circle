#program to accept a filename from user,print its file  extentions
#commonly used file extentions

mydict={
    "py":"python",
    "c":"c,c++",
    "txt":"text",
    "java":"java",
    "doc":"word ",
    "xml":"XML ",
    "sql":"SQL database ",
    "apk":"Android package ",
    "jpeg":"JPEG ",
    "jpg":"JPEG ",
    "png":"PNG ",
    "htm":"HTML ",
    "html":"HTML ",
    "php":"PHP ",
    "js":"javascript",
    "pl":"perl",
    "sh":"bash",
    "cs":"visual c",
    "cpp":"c++"
     }





filename = input("Enter fie name :").casefold()
f_extns=filename.split(".")

if ((f_extns[-1])== "py"):
     print("the extention of the file is:" + mydict["py"])
elif((f_extns[-1])== "c"):
     print("the extention of the file is:" + mydict["c"])
elif((f_extns[-1])== "txt"):
     print("the extention of the file is:" + mydict["txt"])
elif((f_extns[-1])== "java"):
     print("the extention of the file is:" + mydict["java"])
elif((f_extns[-1])== "doc"):
     print("the extention of the file is:" + mydict["doc"])
elif((f_extns[-1])== "xml"):
     print("the extention of the file is:" + mydict["xml"])
elif((f_extns[-1])== "sql"):
     print("the extention of the file is:" + mydict["sql"])
elif((f_extns[-1])== "apk"):
     print("the extention of the file is:" + mydict["apk"])
elif((f_extns[-1])== "jpeg"):
     print("the extention of the file is:" + mydict["jpeg"])
elif((f_extns[-1])== "jpg"):
     print("the extention of the file is:" + mydict["jpg"])
elif((f_extns[-1])== "png"):
     print("the extention of the file is:" + mydict["png"])
elif((f_extns[-1])== "htm"):
     print("the extention of the file is:" + mydict["htm"])
elif((f_extns[-1])== "html"):
     print("the extention of the file is:" + mydict["html"])
elif((f_extns[-1])== "php"):
     print("the extention of the file is:" + mydict["php"])
elif((f_extns[-1])== "js"):
     print("the extention of the file is:" + mydict["js"])
elif((f_extns[-1])== "pl"):
     print("the extention of the file is:" + mydict["pl"])
elif((f_extns[-1])== "sh"):
     print("the extention of the file is:" + mydict["sh"])
elif((f_extns[-1])== "cs"):
     print("the extention of the file is:" + mydict["cs"])
elif((f_extns[-1])== "cpp"):
     print("the extention of the file is:" + mydict["cpp"]) 
else:
    print("The above extension is not present in dictonary,will add the extention soon!")



































     
    
