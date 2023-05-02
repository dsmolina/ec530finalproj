# ec530finalproj

Final project for BU EC530 course. This is a smart pdf reader. It takes a pdf file as input and can translate the file to another language. It can also read the pdf out loud as an audio book for users that have trouble reading and would rather listen. Finally, it combines these two features and can read translated pdf documents out loud. 

It uses the googletrans api to translate the text. The documentation for this api can be found here: https://pypi.org/project/googletrans/ 

To run: 

pip install -r requirements.txt 

python app.py 

Thank you!

Example of Translation: 
![image](https://user-images.githubusercontent.com/79925931/235543170-8d7317a7-26f2-4f07-8570-1bb70a8c730f.png)


I tested the audio for different files, the translate in every language, and the audio for the translated text in every language. I tested for functionality and speed. The use cases for this app are for people that cannot understand/read english and would like to translate their documents. It is also helpful for people that cannot read very well due to eyesight or other reasons and would rather listen to their documents be read to them.

I also tried to have this upload to MongoDB but was not successful so I decided to have it upload to a Google Cloud bucket so the files are uploaded to Google Cloud rather than a SQL database. The audio files are also downloaded to the user's local drive. For this, I had to use a Google Cloud API.
