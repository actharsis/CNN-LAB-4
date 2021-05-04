# Использование техник аугментации данных для улучшения сходимости процесса обучения нейронной сети на примере решения задачи классификации Food-101
## Случайное горизонтальное и вертикальное отображение
Файл: `CNN-food-101-master/random_flip.py`

![legend1](https://github.com/actharsis/lab4/blob/main/legends/random_flip.png)

Метрика качества:
![gr1](https://github.com/actharsis/lab4/blob/main/graphs/random_flip/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr2](https://github.com/actharsis/lab4/blob/main/graphs/random_flip/epoch_loss.svg)

Пример изображений после аугментации:


Наилучший результат данного типа аугментации был достигнут при горизонтальном отображении - 67.50% точности на валидации, это на 0.14% выше, чем максимально достигнутая точность без аугментации. Остальные типы отображения снижали точность примерно на 1%.
## Использование случайной части изображения
Файл: `CNN-food-101-master/random_crop.py`

![legend2](https://github.com/actharsis/lab4/blob/main/legends/random_crop.png)

Метрика качества:
![gr3](https://github.com/actharsis/lab4/blob/main/graphs/random_crop/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr4](https://github.com/actharsis/lab4/blob/main/graphs/random_crop/epoch_loss.svg)

Пример изображений после аугментации:

Наилучшие результаты получились при размере кроппинга 200х200. Максимальное значение точности на валидации - ~63%. Использование случайной части изображения не дало положительных результатов в сравнении с вариантом без аугментации.
## Поворот на случайный угол
Файл: `CNN-food-101-master/random_rotation.py`

![legend3](https://github.com/actharsis/lab4/blob/main/legends/random_rotate.png)

Метрика качества:
![gr5](https://github.com/actharsis/lab4/blob/main/graphs/random_rotate/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr6](https://github.com/actharsis/lab4/blob/main/graphs/random_rotate/epoch_loss.svg)

Пример изображений после аугментации:

Поворот изображения не дал улучшения результатов при протестированных параметрах. Наилучший результат был достигнут при factor=0.04 и режиме заполнения "nearest", максимальная точность на валидации составила 67.2%, что хуже результатов обучения без аугментации.
## Совместное использование всех техник аугментации
Файл: `CNN-food-101-master/all.py`

![legend4]()

Метрика качества:
![gr7]()

Функция ошибок:
![gr8]()

Пример изображений после аугментации:


## Анализ результатов
