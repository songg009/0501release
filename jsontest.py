import json

#字典类型转换为json对象
datas = {
    "code":200,
    "msg":"ok",
    "dataObj":{
        "name":"xiaoming",
	    "age":"15"
    }
}

for i in datas:
    print(i, datas[i])
jsonStr = open("json.txt", "rb")

s = json.loads(jsonStr.read().decode("utf-8"))
print("assettype:",s['assetcontent']["assettype"])
print("filename:",s["assetcontent"]["content"]["videos"]["file"]["filename"])
#s = json.data
#print(data["code"])