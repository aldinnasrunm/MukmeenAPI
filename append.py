import json







def startAppend(num):
    # Load data from 'surah.json'
    with open('surah_data.json', 'r', encoding='utf-8') as surah_file:
        surah_data = json.load(surah_file)

    # Load data from 'Arr.json'
    fileLocation = str('./dataSurah/'+num+'.json')
    with open(fileLocation, 'r', encoding='utf-8') as arr_file:
        arr_data = json.load(arr_file)

    # Create a dictionary to store signCodes by surah and ayat IDs
    sign_codes = {}

    # Populate the sign_codes dictionary
    for item in arr_data:
        surah_id = item['surat']
        ayat_id = item['ayat']
        sign_code = item['signCode']
        sign_codes[(surah_id, ayat_id)] = sign_code

    # Append the signCode to the surah_data where surah and ayat IDs match
    for surah in surah_data['ayat']:
        surah_id = surah['surah']
        ayat_id = surah['id']
        key = (surah_id, ayat_id)

        if key in sign_codes:
            surah['signCode'] = sign_codes[key]

    # Save the updated surah_data to a new JSON file
    with open('surah_with_signCode.json', 'w', encoding='utf-8') as updated_surah_file:
        json.dump(surah_data, updated_surah_file, indent=4, ensure_ascii=False)

    print("signCode appended to surah.json and saved to surah_with_signCode.json successfully.")



startAppend('1')

