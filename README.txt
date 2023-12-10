A small program for converting an image into a picture consisting of letters.
The main file is main.py .
When creating an instance of the Main class, we pass:
1. the name of the image (the image should be placed in the image folder)
2. how many characters will be in the final image in width
3. the width of the final image

The resulting image will be placed in the result folder

It is possible to select the levels of image separation by brightness
To do this, you need to run the file prepare_data.py specifying the number of levels (in the text of the file)
The console displays a dictionary that must be placed in the Main class in the CHARS variable

Libraries used:
1. pygame 2.1.2
2. PIL 9.0.1
3. numpy 1.22.0

//=======

Небольшая программа для перевода изображения в картинку, состоящую из букв.
Главный файл - main.py.
При создании экзепляра класса Main передаем:
1. наименование картинки (картинку стоит поместить в папку image)
2. сколько символов будет в итоговом изображении по ширине
3. ширину итоговой картинки

Картинка, полученная в результате, будет помещена в папку result

Существует возможность выбирать уровни разделения изображения по яркости
Для это необходимо запустить файл prepare_data.py, указав при этом количество уровней (в тексте файла)
В консоли выведется словарь, который необходимо поместить в класс Main в переменуюю CHARS

Используемые библиотеки:
1. pygame 2.1.2
2. PIL 9.0.1
3. numpy 1.22.0
