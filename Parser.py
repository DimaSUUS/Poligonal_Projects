import requests
from bs4 import BeautifulSoup
import os.path
print("Нам нужна папка под Аниме? (Да\Нет)")
CheckingOtvet = input()
while CheckingOtvet != "Да" or CheckingOtvet != "Нет":
    AreWeCreate = 1
    if CheckingOtvet == "Да":
        AreWeCreate = 1
        break
    elif CheckingOtvet == "Нет":
        AreWeCreate = 0
        break
    else:
        print("Пожалуйста, проверьте правильность написания ответа и попрбоуйте еще раз" + "\n" + "Нужно написать Да или Нет")
        CheckingOtvet = input()
PlaceForAnime = ""
if AreWeCreate == 1:
    PlaceForAnime = str(input("Как назовем папку?" + "\n"))
CHECK_FOLDER = os.path.isdir(PlaceForAnime)
if AreWeCreate == 1:
    if not CHECK_FOLDER:
        os.makedirs(PlaceForAnime)
        print(PlaceForAnime + " создана, время ее заполнить :-) ")
    else:
        print(PlaceForAnime, " уже есть")
Tag = input("По какому тегу ищем картинки? (используйте латиницу для поиска, пробелы заменить нижним подчеркиванием)" + "\n")
Counter = int(input("Сколько картинок скачиваем? (число)" + "\n"))
name = input("Какое общее название дать картинкам? (Любое, подходящее вашей операционной системе)" + "\n")
Log_File = open("Log.txt", "a+")
Log_File.write(Tag + "\n")
Log_File.close()
NewTag = Tag.lower()
count = 0
url = str('https://safebooru.org/index.php?page=post&s=list&tags=' + NewTag + "&pid=")
countImage = 0
os.chdir(os.getcwd() + "\\" + PlaceForAnime)
for page in range(Counter):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    for elem in soup.find("div", id="post-list").find_all("span", class_ = "thumb"):
        img = elem.find("img", class_ = "preview").get("src")
        response2 = requests.get(img)
        count += 1
        if count < Counter + 1:
            with open(f"{name}{count}.jpg", "wb") as image:
                image.write(response2.content)
        else:
            print("Скачивание изображений звершено")
            exit()