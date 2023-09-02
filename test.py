import json


num = 1   #surah number

# Load data from 'surah.json'
with open('surah_data.json', 'r', encoding='utf-8') as surah_file:
    surah_data = json.loads(str(surah_file.read()))

# Load data from 'Arr.json'
# fileLocation = str('./dataSurah/'+ str(num)+'.json')
# with open(fileLocation, 'r', encoding='utf-8') as arr_file:
#     arr_data = json.loads(str(arr_file.read()))
    
doc ={}
# y = 0
# for x in surah_data:
#     if(x["sura"] == arr_data["nomor"]):
#         if(x["aya"] == arr_data["ayat"][y]["id"]):
#             print(x["makhraj"], "pasangin di", arr_data["ayat"][y]["tr"])
#             print("-----------------------------------------------------------")
    
#     y = y + 1

last = 0
for x in surah_data:
# Set the surah data 
    # print( "Surah data : ",str(x["sura"]))
    print("-----------------------------------------------------------")
    print()
    if(last == 0 or arr_data["nomor"] != x["sura"]):
        fileLocation = str('./dataSurah/'+ str(x["sura"])+'.json')
        with open(fileLocation, 'r', encoding='utf-8') as arr_file:
            arr_data = json.loads(str(arr_file.read()))
        last = 1

    # print(x["sura"])
    if(x["sura"] == arr_data["nomor"]):
        # print("CecK")
        # print("Ayat : " ,str(x["aya"]))
        # print(arr_data["ayat"][x["aya"] - 1]["nomor"])
        if(x["aya"] == arr_data["ayat"][x["aya"] - 1]["nomor"]):
            # append x["signCode"] into arr_data["ayat"][x["aya"] - 1]
            # print(x["signCode"])
            if "signCode" not in arr_data["ayat"][x["aya"] - 1]:
                # arr_data["ayat"][x["aya"] - 1].add("signCode")
                arr_data["ayat"][x["aya"] - 1]["signCode"] = x["signCode"]  
            # arr_data["ayat"][x["aya"] - 1]["signCode"] = x["signCode"]
            # print(x["makhraj"], "pasangin di", arr_data["ayat"][x["aya"] - 1]["tr"])
            # print("-----------------------------------------------------------")
            # print(arr_data["ayat"][x["aya"] - 1]["signCode"])
    print(x["aya"])
    print(arr_data["ayat"][x["aya"] - 1])

    with open(str('./newData/'+ str(x["sura"])+'.json'), 'w', encoding='utf-8') as file:
        json.dump(arr_data, file, ensure_ascii=False, indent=4)



print("Complete")


# print(arr_data['ayat'][0]['idn'])
# print(surah_data[0]['sura'])













