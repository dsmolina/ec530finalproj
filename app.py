# Copyright 2023 Dasha Smolina dsmolina@bu.edu
import pyttsx3
import PyPDF2
import googletrans
from google.cloud import storage

pdf_file = "example.pdf"
# provide pdf file name in pdf_file 
pdf = open(pdf_file, 'rb')

# GOOGLE CLOUD UPLOAD
storage_client = storage.Client.from_service_account_json(
        'ec530-final-6f633954b3d3.json')

    #print(buckets = list(storage_client.list_buckets())

bucket = storage_client.get_bucket('ec530final')
blob = bucket.blob('pdf_files')
blob.upload_from_filename(r'example.pdf')

# accessing pdf contents 
contents = PyPDF2.PdfFileReader(pdf)

# processing the total page count 
page_count = contents.numPages

# showing user with page number along with uploaded file name
print('---------------------------------------------------------')
print('Successfully uploaded {} with {} pages'.format(pdf_file, page_count))
print('---------------------------------------------------------')
# create a dictionary to store languages with its short names
lang_dict = {'arabic': 'ar', 'bengali': 'bn', 'chinese': 'zh-cn', 'dutch': 'nl',
             'english': 'en', 'french': 'fr', 'german': 'de', 'hindi': 'hi', 'indonesian': 'id',
             'japanese': 'ja', 'korean': 'ko', 'latin': 'la', 'malayalam': 'ml', 'nepali': 'ne',
             'persian': 'fa', 'portuguese': 'pt', 'russian': 'ru', 'spanish': 'es', 'tamil': 'ta',
             'urdu': 'te', 'turkish': 'tr', 'vietnamese': 'vi'}

# showing users available values to select
while(True):
    choice = input("Do you want to translate the document or make it an audio book? (translate/audio/both): \n *translated audio is not spoken with correct accent* \n  (translate/audio/both): ")
    if choice.lower() == "translate" or choice.lower() == "both":
        print('\nList of languages available')
        print('------------------------------------------------------------')

        for key, val in lang_dict.items():
            print(key, end=' , ')
        print('\n----------------------------------------------------------')
        # checking user selected language in the provided dictionary
        while True:
            # getting user desired language
            lang_choice = input("Select language for translation: ")

            if lang_choice.lower() in lang_dict:
            # if found the input will be passed to translator
                selected = lang_dict[lang_choice.lower()]
                break
            else:
            # if not found will prompt user to input correct value
                print('\nFormat not accepted\n')

        # prompting user whether to process full pdf or some certain range or a certain page
        while True:
            input_choice = input("\nTranslate all pages? (y/n): ")

            # if user input is yes process whole text by providing range as total page count

            if input_choice.lower() == "y" or input_choice.lower() == "yes":

                for pages in range(page_count):
                    read_page = contents.getPage(pages)
                    text = read_page.extractText()
                    # create object to access translator functionalities
                    translator = googletrans.Translator()
                    # converting the text using translator
                    converted_text = translator.translate(text, dest=selected)
                    print('page - {}'.format(pages+1))
                    print('----------------------------------------------------')
                    # showing converted text by referencing with page number
                    print(converted_text)
                    print('\n')
                    break

        # if user inputs no ask user about page selection criteria
            elif input_choice.lower() == "n" or input_choice.lower() == "no":
            # taking user criteria for selection
                while True:
                    page_select = input('\nCustom selection or single selection ? : (c/s) : ')

                    if page_select.lower() == "s" or page_select.lower() == "single":
                        try:
                            selected_page_number = int(input('Enter page number to translate : '))
                        except ValueError as v:
                            print('\nUnacceptable format\n')

                    # if page value provided by user greater than page limit , will get a false message
                        if selected_page_number > page_count:
                            print('Enter value within page limit')
                        else:
                            read_page = contents.getPage(selected_page_number-1)
                            text = read_page.extractText()
                            # create object to access translator functionalities
                            translator = googletrans.Translator()
                            # converting the text using translator
                            converted_text = translator.translate(text, dest=selected)
                            print('page - {}'.format(selected_page_number))
                            print('----------------------------------------------------')
                            # showing converted text by referencing with page number
                            print(converted_text)
                            print('\n')
                            break

                    elif page_select.lower() == "c" or page_select.lower() == "custom":
                        while True:
                            try:
                                lowlimit = int(input('Enter Range from: '))
                                uplimit =  int(input('Enter Range to: '))
                            except ValueError as v:
                                print('\nUnacceptable format\n')

                            if uplimit > page_count or lowlimit > page_count:
                                print('\nEnter value within page limit\n')
                                print('\n')
                            else:
                                for val in range(lowlimit-1, uplimit):
                                    read_page = contents.getPage(val)
                                    text = read_page.extractText()
                                    # create object to access translator functionalities
                                    translator = googletrans.Translator()
                                    # converting the text using translator
                                    converted_text = translator.translate(text, dest=selected)
                                    print('\npage - {}'.format(val+1))
                                    print('----------------------------------------------------')
                                    # showing converted text by referencing with page number
                                    print(converted_text)
                                    print('\n')
                                    break
                            break
                    else:
                        print('\nValue not accepted\n')
                    break
            else:
                print('\nInput not accepted\n')
                print('\n')
            break
        if choice.lower() == "both":
            voice = pyttsx3.init()
            voice.save_to_file(converted_text, "test.txt")
            voice.say(converted_text)
            voice.runAndWait()
    elif choice.lower() == "audio":
        print(page_count)

        voice = pyttsx3.init()
        for num in range(0, page_count):
            page = contents.getPage(num)
            text = page.extractText()
            voice.say(text)
            voice.runAndWait()
    else:
        print("Input not accepted")

'''''Translated contents can also be heard using configuring pyttsx3 module in python . We can either save the final output as 
a file and can adjust translation sound volume, voice and speed'''

# speaker = pyttsx3.init()
# voices = speaker.getProperty('voices')
# speaker.setProperty('voice', voices[1].id)
# rate = speaker.getProperty('rate')
# speaker.setProperty('rate', 100)
# speaker.save_to_file(converted_text, "test.txt")
# speaker.runAndWait()
