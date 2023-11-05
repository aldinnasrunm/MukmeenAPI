import json
import os

# Load data from juzData.json
with open('juzData.json', 'r', encoding='utf-8') as juz_data_file:
    juz_data = json.load(juz_data_file)

output_folder = 'juz'
os.makedirs(output_folder, exist_ok=True)
final_data_json = []

# Create a folder for each juz_id
for juz in juz_data['juzs']:
    juz_id = juz['id']#
    verse_mapping = juz['verse_mapping']
    # output_folder = f'juz_{juz_id}'
    # os.makedirs(output_folder, exist_ok=True)

    # print(juz_id)
    # print(verse_mapping)
    ns = 0
    for nosurah, ayat in verse_mapping.items():
        ns = nosurah
        if juz_id > 0 :
            ayatStart, ayatEnd = ayat.split('-')
            # print(jus)
            print("Ayat start : ",ayatStart)
            print("Ayat end : ",ayatEnd)
            with open('surah/'+nosurah+'.json', 'r', encoding='utf-8') as surah_file:
                surah_file = json.load(surah_file)
            
            surah_data_json = {
                    "status": surah_file["status"],
        "nomor": surah_file["nomor"],
        "nama": surah_file["nama"],
        "nama_latin": surah_file["nama_latin"],
        "jumlah_ayat": surah_file["jumlah_ayat"],
        "tempat_turun": surah_file["tempat_turun"],
        "arti": surah_file["arti"],
        "deskripsi": surah_file["deskripsi"],
        "audio": surah_file["audio"],
        "ayat": surah_file["ayat"][int(ayatStart)-1:int(ayatEnd)]
            }
            # print(surah_file['nama_latin'])

            print(surah_data_json)
            final_data_json.append(surah_data_json)
        
#     final_data_json = {
# "data": final_data_json
# }
    # with open('final_data.json', 'w', encoding='utf-8') as final_data_file:
    #     json.dump(final_data_json, final_data_file, ensure_ascii=False, indent=4)

    # # save into json file
    # with open(f'{output_folder}', 'w', encoding='utf-8') as juz_file:
    #     json.dump(final_data_json, juz_file, ensure_ascii=False, indent=4)
# print(final_data_json)
    # juz_item_data_filename = os.path.join(output_folder, 'juz_item_data.json')
    # with open(juz_item_data_filename, 'w', encoding='utf-8') as juz_item_data_file:
    #         json.dump(juz_item_data, juz_item_data_file, ensure_ascii=False, indent=2)
    juz_item_data_filename = os.path.join(output_folder, str(juz_id)+'.json')
    with open(juz_item_data_filename, 'w', encoding='utf-8') as juz_item_data_file:
        json.dump(final_data_json, juz_item_data_file, ensure_ascii=False, indent=2)
        
        # break
