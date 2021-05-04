# Использование техник аугментации данных для улучшения сходимости процесса обучения нейронной сети на примере решения задачи классификации Food-101
## Случайное горизонтальное и вертикальное отображение
Файл: `CNN-food-101-master/random_flip.py`

```python
flipped_data = tf.keras.layers.experimental.preprocessing.RandomFlip(mode="vertical")(inputs)
```

![legend1](https://github.com/actharsis/lab4/blob/main/legends/random_flip.png)

Метрика качества:
![gr1](https://github.com/actharsis/lab4/blob/main/graphs/random_flip/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr2](https://github.com/actharsis/lab4/blob/main/graphs/random_flip/epoch_loss.svg)

Пример изображений после аугментации:

Horizontal flip:
![ex6](https://github.com/actharsis/lab4/blob/main/images/horizontal.png)

Vertical flip:
![ex7](https://github.com/actharsis/lab4/blob/main/images/vertical.png)

Horizontal and vertical flip:
![ex8](https://github.com/actharsis/lab4/blob/main/images/horizontal_and_vertical.png)

Было использовано 3 режима отображения: vertical flip, horizontal flip и horizontal and vertical flip. Наилучший результат данного типа аугментации был достигнут при горизонтальном отображении - 67.50% точности на валидации, это на 0.14% выше, чем максимально достигнутая точность без аугментации. Остальные типы отображения снижали точность примерно на 1%.
## Использование случайной части изображения
Файл: `CNN-food-101-master/random_crop.py`

```python
cropped_data = tf.keras.layers.experimental.preprocessing.RandomCrop(CROP_TO_SIZE, CROP_TO_SIZE)(inputs)
```

![legend2](https://github.com/actharsis/lab4/blob/main/legends/random_crop.png)

Метрика качества:
![gr3](https://github.com/actharsis/lab4/blob/main/graphs/random_crop/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr4](https://github.com/actharsis/lab4/blob/main/graphs/random_crop/epoch_loss.svg)

Пример изображений после аугментации:
Cropping size 120x120:
![ex1](https://github.com/actharsis/lab4/blob/main/images/crop120.png)

Наилучшие результаты получились при размере кроппинга 200х200. Максимальное значение точности на валидации - ~63%. Использование случайной части изображения не дало положительных результатов в сравнении с вариантом без аугментации.
## Поворот на случайный угол
Файл: `CNN-food-101-master/random_rotation.py`

```python
rotated_data = tf.keras.layers.experimental.preprocessing.RandomRotation(factor=0.25, fill_mode="reflect")(inputs)
```

![legend3](https://github.com/actharsis/lab4/blob/main/legends/random_rotate.png)

Метрика качества:
![gr5](https://github.com/actharsis/lab4/blob/main/graphs/random_rotate/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr6](https://github.com/actharsis/lab4/blob/main/graphs/random_rotate/epoch_loss.svg)

Пример изображений после аугментации:
factor=0.04, fill_mode=constant:
![ex2](https://github.com/actharsis/lab4/blob/main/images/factor%3D0.04%2C%20fill_mode%3Dconstant.png)

factor=0.04, fill_mode=nearest:
![ex3](https://github.com/actharsis/lab4/blob/main/images/factor%3D0.04%2C%20fill_mode%3Dnearest.png)

factor=0.04, fill_mode=reflect:
![ex4](https://github.com/actharsis/lab4/blob/main/images/factor%3D0.04%2C%20fill_mode%3Dreflect.png)

factor=0.04, fill_mode=wrap:
![ex5](https://github.com/actharsis/lab4/blob/main/images/factor%3D0.04%2C%20fill_mode%3Dwrap.png)

Поворот изображения не дал улучшения результатов при протестированных параметрах. Наилучший результат был достигнут при factor=0.04 и режиме заполнения "nearest", максимальная точность на валидации составила 67.2%, что хуже результатов обучения без аугментации.
## Совместное использование всех техник аугментации
Файл: `CNN-food-101-master/all.py`

```python
new_data = tf.keras.layers.experimental.preprocessing.RandomCrop(CROP_TO_SIZE, CROP_TO_SIZE)(inputs)
new_data = tf.keras.layers.experimental.preprocessing.RandomFlip(mode="horizontal")(new_data)
new_data = tf.keras.layers.experimental.preprocessing.RandomRotation(factor=0.04, fill_mode="nearest")(new_data)
```

![legend4](https://github.com/actharsis/lab4/blob/main/legends/all.png)

Метрика качества:
![gr7](https://github.com/actharsis/lab4/blob/main/graphs/all/epoch_categorical_accuracy.svg)

Функция ошибок:
![gr8](https://github.com/actharsis/lab4/blob/main/graphs/all/epoch_loss.svg)

Пример изображений после аугментации:

![ex9](https://github.com/actharsis/lab4/blob/main/images/all.png)

Использование всех техник аугментации сразу не дало положительных результатов. Максимальная полученная точность на валидации составляет 63.4%, что на 4% меньше, чем наибольшая точность у сети без аугментации.
## Анализ результатов
Были опробованы различные техники аугментации. К улучшению результатов привело лишь горизонтальное отображение, которое показало точность на 0.14% больше, чем начальный вариант. Комбинирование нескольких техник не дало результатов. Можно сказать, что аугментация данных не во всех случаях может улучшить работу нейросети.
