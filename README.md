### 1. Выборка и генеральная совокупность( определения, чем отличаются)
**Генеральная совокупность и выборка: определения и отличия**

**Генеральная совокупность (популяция)**:
Генеральная совокупность, или популяция, - это полное множество всех объектов, событий или единиц, обладающих определенными характеристиками, которые исследователь желает изучить. Она включает в себя все элементы, которые соответствуют установленным критериям. Например, если исследователь хочет изучить предпочтения всех жителей города по отношению к новому парку, то генеральная совокупность будет включать всех жителей этого города.

**Выборка**:
Выборка - это подмножество генеральной совокупности, которое отбирается для проведения исследования. Цель выборки - получить представительные данные, которые можно обобщить на всю генеральную совокупность. Выборка должна быть достаточно большой и репрезентативной, чтобы результаты исследования были точными и надежными. Например, если из всех жителей города выбираются 1000 человек для опроса о новом парке, то эти 1000 человек составляют выборку.

**Отличия между генеральной совокупностью и выборкой**:
1. **Размер**: Генеральная совокупность включает всех возможных членов или объекты, соответствующие критериям исследования, тогда как выборка представляет собой лишь часть этой совокупности.
2. **Цель**: Генеральная совокупность используется для обозначения всех объектов исследования, а выборка используется для практического проведения исследований, когда невозможно опросить или изучить всю генеральную совокупность.
3. **Обобщение результатов**: Результаты, полученные на основе выборки, используются для обобщения на всю генеральную совокупность. Качество этих обобщений зависит от того, насколько репрезентативной является выборка.
4. **Практическая реализация**: Исследовать всю генеральную совокупность часто бывает невозможно из-за ограничений времени, ресурсов и затрат, поэтому выборка используется как практическое решение для получения данных.

Пример:
- **Генеральная совокупность**: Все студенты университета.
- **Выборка**: 200 студентов из этого университета, участвующие в опросе.
  
### 2. Формулы, выборочное среднее, выборочная дисперсия, выборочное отклонение и их отклонения.
Для работы с выборкой в статистике часто используют выборочное среднее, выборочную дисперсию и выборочное стандартное отклонение. Эти показатели помогают характеризовать данные выборки и делать выводы о генеральной совокупности. 

## Формулы

1. **Выборочное среднее (\(\bar{x}\))**:
   \[
   \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
   \]
   где \(x_i\) — значения выборки, а \(n\) — размер выборки.

2. **Выборочная дисперсия (\(s^2\))**:
   \[
   s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
   \]
   Выборочная дисперсия используется для оценки изменчивости данных выборки.

3. **Выборочное стандартное отклонение (\(s\))**:
   \[
   s = \sqrt{s^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
   \]
   Это показатель, который измеряет среднеквадратическое отклонение значений выборки от ее среднего.

## Отклонения

- **Выборочное среднее** отклоняется от истинного среднего генеральной совокупности (\(\mu\)) на величину случайной ошибки, которая уменьшается с увеличением размера выборки.

- **Выборочная дисперсия** отклоняется от истинной дисперсии генеральной совокупности (\(\sigma^2\)), но при большом размере выборки (n) она является несмещенной оценкой дисперсии.

- **Выборочное стандартное отклонение** также отклоняется от истинного стандартного отклонения генеральной совокупности (\(\sigma\)), но это отклонение уменьшается с увеличением размера выборки.

## Пример

Рассмотрим пример, в котором даны следующие данные выборки: 5, 7, 8, 6, 9.

1. **Выборочное среднее**:
   \[
   \bar{x} = \frac{5 + 7 + 8 + 6 + 9}{5} = \frac{35}{5} = 7
   \]

2. **Выборочная дисперсия**:
   \[
   s^2 = \frac{1}{5-1} \sum_{i=1}^{5} (x_i - 7)^2 = \frac{1}{4} \left[(5-7)^2 + (7-7)^2 + (8-7)^2 + (6-7)^2 + (9-7)^2\right]
   \]
   \[
   s^2 = \frac{1}{4} \left[4 + 0 + 1 + 1 + 4\right] = \frac{1}{4} \cdot 10 = 2.5
   \]

3. **Выборочное стандартное отклонение**:
   \[
   s = \sqrt{2.5} \approx 1.58
   \]

## Заключение

Эти формулы и показатели играют ключевую роль в анализе выборочных данных и позволяют статистикам делать обоснованные выводы о свойствах генеральной совокупности на основе данных выборки.
### 3. Отличия частотной гистограммы от вероятностной гистограммы

**Частотная гистограмма**:
- Отображает количество наблюдений (частоту) в каждом интервале (бин).
- Высота столбцов показывает, сколько раз значения данных попадают в каждый интервал.
- Сумма высот столбцов равна общему количеству наблюдений.

**Вероятностная гистограмма**:
- Отображает относительные частоты или вероятности.
- Высота столбцов показывает вероятность попадания значения в данный интервал.
- Сумма площадей столбцов равна 1 (т.е. 100%).

### 4. Смысл функции плотности (геометрический) и её свойства

**Функция плотности вероятности (PDF)**:
- Геометрически: это кривая, под которой площадь равна 1. Площадь под кривой на интервале \([a, b]\) равна вероятности того, что случайная величина попадает в этот интервал.
- Свойства:
  - \(f(x) \geq 0\) для всех \(x\).
  - \(\int_{-\infty}^{\infty} f(x) \, dx = 1\).
  - Вероятность попадания случайной величины в интервал \([a, b]\) равна \(\int_{a}^{b} f(x) \, dx\).

### 5. Смысл функции распределения и её свойства

**Функция распределения (CDF)**:
- Геометрически: это кривая, которая растет от 0 до 1.
- Значение \(F(x)\) даёт вероятность того, что случайная величина \(X\) меньше или равна \(x\).
- Свойства:
  - \(0 \leq F(x) \leq 1\) для всех \(x\).
  - Функция непрерывна слева.
  - \(\lim_{x \to -\infty} F(x) = 0\) и \(\lim_{x \to \infty} F(x) = 1\).

### 6. Ошибка первого и второго рода

- **Ошибка первого рода (Type I error)**: ошибочное отклонение нулевой гипотезы (\(H_0\)), когда она истинна. Вероятность этой ошибки обозначается \(\alpha\).
- **Ошибка второго рода (Type II error)**: ошибочное принятие нулевой гипотезы (\(H_0\)), когда она ложна. Вероятность этой ошибки обозначается \(\beta\).

### 7. Виды гипотез

- **Нулевая гипотеза (H₀)**: утверждение о параметре генеральной совокупности, которое предполагается истинным, пока не доказано обратное.
- **Альтернативная гипотеза (H₁)**: утверждение, противоположное нулевой гипотезе, предлагающее новую теорию или эффект.

### 8. Уровень надежности доверительного оценивания

**Уровень надежности**:
- Вероятность, что доверительный интервал содержит истинное значение параметра.
- Обычно обозначается как \(1 - \alpha\), где \(\alpha\) — уровень значимости.
- Например, для 95%-го доверительного интервала уровень надежности равен 0.95.

### 9. Виды доверительных интервалов

- **Для среднего**: \(\bar{x} \pm t_{\alpha/2} \cdot \frac{s}{\sqrt{n}}\) (если распределение нормально, а выборка велика).
- **Для пропорции**: \(p \pm Z_{\alpha/2} \sqrt{\frac{p(1-p)}{n}}\).
- **Для разности средних**: \((\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2} \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}\).

### 10. Выборочная корреляция и ковариация. Свойства корреляции

- **Выборочная корреляция**:
  \[
  r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
  \]
  - Показатель линейной связи между двумя переменными.
  - \( -1 \leq r \leq 1 \).

- **Выборочная ковариация**:
  \[
  \text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
  \]

- **Свойства корреляции**:
  - Безразмерна.
  - Инвариантна к линейным преобразованиям.
  - Если \(r = 0\), переменные не линейно связаны (но могут быть связаны нелинейно).

### 11. Мода и медиана

- **Мода**: значение, которое встречается наиболее часто.
- **Медиана**: центральное значение выборки, делящее её на две равные части. Если выборка чётная, медиана — среднее двух центральных значений.

### 12. Метод моментов и метод максимального правдоподобия

- **Метод моментов**:
  - Параметры оцениваются путём приравнивания выборочных моментов (например, среднего, дисперсии) к теоретическим моментам.
  - Прост в вычислении, но может быть менее точным.

- **Метод максимального правдоподобия**:
  - Параметры оцениваются путём максимизации функции правдоподобия.
  - Вычислительно сложнее, но часто даёт более точные оценки.

### 13. Виды распределений

- **Непрерывные**: нормальное, экспоненциальное, бета, гамма.
- **Дискретные**: биномиальное, пуассоновское, геометрическое, гипергеометрическое.

### 14. Квантиль и квартиль

- **Квантиль**: значение, которое разделяет данные на заданные пропорции. Например, 25-й процентиль (первый квартиль \(Q1\)) делит данные на 25% ниже этого значения и 75% выше.
- **Квартиль**: тип квантиля, делящий данные на четыре части. 
  - \(Q1\) (25-й процентиль).
  - \(Q2\) (50-й процентиль или медиана).
  - \(Q3\) (75-й процентиль).

Квантили и квартиль используются для описания распределения данных, выявления аномалий и сравнения различных наборов данных.
