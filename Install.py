import os

print("Установка библиотек")
os.system("pip3 install --upgrade pip")
bib = ["pyowm"]
for i in range(len(bib)):
    print("Установка "+bib[i]+"...\033[0m")
    os.system("pip3 install "+bib[i])
os.system('cls')
print("Установка завершена!")
