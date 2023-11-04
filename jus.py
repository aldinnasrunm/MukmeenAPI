import json
import os

# Load data from juzData.json
with open('juzData.json', 'r', encoding='utf-8') as juz_data_file:
    juz_data = json.load(juz_data_file)

# Create a folder for each juz_id
for juz in juz_data['juzs']:
    juz_id = juz['id']
    verse_mapping = juz['verse_mapping']
    # output_folder = f'juz_{juz_id}'
    # os.makedirs(output_folder, exist_ok=True)

    # print(juz_id)
    # print(verse_mapping)

    for nosurah, ayat in verse_mapping.items():
        ayatStart, ayatEnd = ayat.split('-')
        # print(jus)
        print("Ayat start : ",ayatStart)
        print("Ayat end : ",ayatEnd)
        with open('surah/'+nosurah+'.json', 'r', encoding='utf-8') as surah_file:
            surah_file = json.load(surah_file)
        
        print(surah_file['nama_latin'])
