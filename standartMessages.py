start = '''<i>Выберите категорию</i>
/services - Услуги 
/thebook - Купить книгу 
/contacts - Контакты 
/FAQ – Частые вопросы
/documents – Документы об образовании
/start – Помощь'''
thebook = '''Книга Юрия Ермолаева «Четыре века истории одной семьи»
Книга посвящена истории одной русской семьи на протяжении 430 лет её истории. Это результат глубокого историко-генеалогического исследования. В книге прослеживается не только история одного рода и тех населённых пунктов, где проживала семья. В исследовании детально описан быт, нравы и обычаи русского крестьянина, и жизнь целой страны через призму семейной истории. Вместе с семьёй Лобковых читатель пройдёт через четыре столетия, через три русских уезда и через три войны.
«Четыре века истории одной семьи» – один из ярких образцов того, как можно оформить собственную родословную. Эта книга будет интересна не только потомкам семьи, но и всем, кто интересуется русской историей и невероятными поворотами судеб. 
'''
back_to_services = "Для перехода к услугам используйте /services"
unhandled = "Я не знаю такой команды. Воспользуйтесь /start для доступа к меню"
unhandled_1 = "Произошла ошибка при обработке кнопки. Попробуйте повторить сценарий выполнения."
contacts = '''Юрий Ермолаев
Телефон: +7 (926) 733-24-81 (Telegram, WhatsApp) 
Почта: dir@mgorod.com 
Интернет-платформы:
<a href="https://t.me/yuri_ermolaev">Telegram channel</a>
<a href="https://youtube.com/@yuriermolaev2552">YouTube channel</a>
<a href="https://instagram.com/yuri.ermolaev?igshid=NTdlMDg3MTY=">Instagram</a>
<a href="https://dzen.ru/id/63cf8c7b3d9be32e0f7d3834 ">Дзен</a>
'''
advert = '''<b>Фрагменты книг</b>:
-	<a href="https://disk.yandex.ru/i/W8Cp6yM5yAto5w">Родословная книга</a>
-	<a href="https://disk.yandex.ru/i/mnKsWoGFwYvFoQ">Историческая родословная касимовских татар</a>
-	<a href="https://disk.yandex.ru/i/5gLZJRhfWJ1mng">Четыре века истории одной семьи</a>
В данный момент к заказу доступна книга «Четыре века истории одной семьи». Цена экземпляра составляет 10400 рублей, включая почтовую отправку по РФ.
Для заказа книги обратитесь в /contacts
<a href="https://disk.yandex.ru/i/AO9XJLi1ZQ594Q">Посмотреть отзывы</a>
'''
documents = '''Документы об образовании'''
faq = '''❓<b><i>Сроки</i></b>
В среднем: от трёх месяцев до двух лет. При этом много зависит от локальных условий и прочих обстоятельств.
❓<b><i>От чего варьируется стоимость</i></b>
Цену можно точнее прояснить после анализа ваших вводных данных: регион, сословие, вероисповедание, степень глубины устных семейных преданий. Алгоритм поиска по разным сословиям и разным регионам может иметь свои особенности.
❓<b><i>До какого поколения можно найти предков</i></b>
Предельная глубина родословной зависит от степени сохранности источников. От региона к региону ситуация отличается. Также многое зависит от сословия и вероисповедания. По православным порой доходим до рубежа XVIII и XVII веков. Иногда, реже – до рубежа XVII и XVI веков. По иудеям до середины XVIII век. По мусульманам – всё зависит от региона. Если Ваши предки были татарами или башкирами, то порой можно шагнуть и в XVII-й век. По католикам и лютеранам – своя отдельная картина. Но хуже всего обычно по старообрядцам.
❓<b><i>Что нужно от Вас</i></b>
-	Соберите все имеющиеся у вас документы тех предков, кого вы знаете
-	Запишите устные предания
-	Пришлите мне для анализа на email
'''
services = '''В данном разделе вы можете ознакомиться с предоставляемыми услугами и приблизительными ценами. Для заказа индивидуальной услуги обратитесь напрямую к исполнителю при помощи /contacts.
Выберите категорию
'''
messageA = '''Счёт родства в России до революции традиционно вёлся по мужской линии родства. Одним родом считалась линия: прадед – дед – отец – сын – внук, причём каждый со своими жёнами и детьми. Любая женская (девичья) фамилия считается отдельным родом и считается аналогично: прадед – дед – отец девицы – девица. Все мужчины, соответственно, указываются с жёнами.'''
messageB = '''<i>Прайс</i>
Век считается от того года, которым датирован последний известный вам семейный документ. Например, свидетельство о рождении дедушки 1920 года рождения. Соответственно, век считается от начального 1920 года до условного 1820 года.
Средняя стоимость века (1920–1820) в среднем составляет 150 тысяч рублей.
Если выйдет три века (1920–1620-е годы), то цена составит около 450 тысяч рублей.
Однако стоимость зависит от многих факторов, некоторые из которых заранее трудно предвидеть. Например, предки могли часто переезжать с места на место. И в таком случае приходится искать их по разным губерниям и уездам Российской империи, совершать командировки в архивы других городов. Это усложняет поиск и влияет на цену. 
А бывает наоборот – выходит дешевле. Например, если предок вдруг оказался сиротой или подкидышем – и тогда работа неожиданно останавливается.
<i>Условия оплаты</i>
Первоначальный аванс на командировку в архив – от 90 тысяч рублей. Расходы на билеты и гостиницы оплачиваются отдельно, вне гонорара исследователя. 
Далее оплата услуг поэтапно. Можно сделать паузу, если вдруг расходы начнут превышать ожидаемую сумму. 
<i>Примеры</i>
-   <a href="https://disk.yandex.ru/i/GVBwQZCdMTPyqQ">Краткая генеалогическая роспись</a>
-   <a href="https://disk.yandex.ru/d/C0c-MJYIHc2rAA">Детальная родословная с описанием истории рода</a>
'''
services_1 = '''<b>Архивный поиск:</b>
📖<b>Генеалогия</b>
❓<i>Что это?</i> 
Поиск записей о предках в архивах России и других стран. За одну <i>патрилинейную</i> (/mean) родственную линию (одну фамилию) – в среднем выходит от 100 до 200 тысяч рублей за один век. Заранее неизвестно, сколько веков может получится в итоге исследования. Может выйти как один или два века, так и три, и даже порой четыре. Такие счастливые случаи бывали (/thebook). Цена при этом кратно увеличивается.
Генеалогия – это имена, фамилии, отчества предков, сведения о годах их жизни, а также сведения об их сословном статусе и месте жительства. Хотите узнать больше? Тогда вам нужен биографический поиск.
💰<i>Узнать прайс? </i>(/more)

📖<b>Биографический поиск </b>
❓<i>Что это?</i>
Поиск биографических подробностей жизни предков. Был ли предок репрессирован или раскулачен? Воевал в Великую Отечественную войну? Служил ли в Красной армии или у белых? Сколько коров, лошадей, земли, домов и прочего имущества было у семьи предков до революции? Какие события происходили в родовом селении предков в XIX и XVIII веках? Какие налоги и оброки им приходилось платить и сколько они могли зарабатывать? Какие местные диалекты известны в той местности, откуда происходят мои предки? Что сеяли, чем питались, как справляли свадьбы, какие песни пели? За какое происшествие лишили сана местного священника или сослали на каторгу односельчанина моих предков? Это и многое другое – биографистика и локальная микроистория.
💰 <i>Прайс</i>
Одна персона или один существенный биографический сюжет в жизни одной семьи: от 80 тысяч рублей.
'''
services_2 = '''<b>Семейная история</b>
📖<b>Генеалогическая экспертиза.</b> 
❓<i>Что это?</i>
Начальный этап генеалогического поиска, который уходит на глубину до середины XIX века. По итогам экспертизы Вы получите отчёт с фотокопиями документов с указанием архивного шифра, генеалогическое древо и алгоритм дальнейшего самостоятельного архивного поиска с анализом сохранности источников.
💰 <i>Прайс</i>
От 200 тысяч рублей за 1 фамильный род.

📖<b>Разбор семейного архива</b>
❓<i>Что это?</i>
Работа с документами из домашнего архива. Разбор и классификация документов (дореволюционные или фронтовые письма, мемуары, домашний фотоальбом, семейные документы: членские книжки, партийные билеты, военные билеты и прочее). Организация системы правильного архивного хранения, описание документов.
💰 <i>Прайс</i>
От 100 тысяч рублей.

📖<b>Интервью </b>
❓<i>Что это?</i>
Работа с ныне живущими родственниками. Проведение интервью, опроса старших членов семьи, дальних родственников, соседей, сослуживцев, односельчан. Работа с государственными учреждениями. Запись свидетельств, проверка сведений.
💰 <i>Прайс</i>
От 100 тысяч рублей.

📖<b>Анализ происхождения фамилии</b>
❓<i>Что это? </i>
Исследование происхождения фамилии на основе детального анализа всей совокупности собранных исторических и генеалогических данных. Разбор сложных случаев.
💰 <i>Прайс</i>
Индивидуально.

📖<b>Некрополистика</b>
❓<i>Что это?</i>
Посещение родовых кладбищ, работа по выявлению и фотофиксации надгробий.
💰 <i>Прайс</i>
От 80 тысяч рублей.

📖<b>Составление отчёта</b>
❓<i>Что это?</i>
Итог исследовательской работы. Возможен в трёх вариантах:
-   <a href="https://disk.yandex.ru/i/GVBwQZCdMTPyqQ">Краткая генеалогическая роспись</a>
-   <a href="https://disk.yandex.ru/d/C0c-MJYIHc2rAA">Детальная родословная с описанием истории рода</a>
-   Масштабная книга об истории семьи на протяжении нескольких столетий (/thebook)
'''
services_3 = '''<b>Писательские услуги</b>
Составление повести об истории семьи.
❓<i>Что это?</i>
Текст об истории вашего рода, написанный в художественной форме, изложенный хорошим русским языком. Будет читаться легко, увлекательно и интересно. При этом – со строгой системой научных ссылок на архивные источники.
💰<i>Прайс</i>
От 700 тысяч рублей.
'''
services_4 = '''<b>Издательские услуги</b>
Издание книги о вашей семейной истории
❓<i>Что это?</i>
Разработка уникального дизайна книги. Подбор и обработка иллюстраций: архивных документов, семейных фотографий. Вёрстка книги. Печать любым тиражом.
💰 <i>Прайс</i>
От 700 тысяч рублей.'''
services_5 = '''<b>Графика</b>
Родословное древо 
❓<i>Что это?</i>
Родословное древо в классическом виде настенного плаката. Неповторимый дизайн, которого не найдёте в интернете. Такого не встретите на массовом рынке.
💰 <i>Прайс</i>
Индивидуально.
'''
services_6 = '''<b>Фильмы о семейной истории</b>
❓<i>Что это?</i>
Повествование в виде единого фильма о семейной истории либо в виде серии видеосюжетов.
Форматы:
-   Интервью
-   Выезд на места жительства предков. Съёмка на местности и с воздуха
-   Съёмка артефактов: семейные реликвии, боевые награды, личные вещи предков, предметы старинного быта
💰 <i>Прайс</i> 
Индивидуально, от 300 тысяч рублей. На стоимость влияют параметры: хронометраж, количество выездов и локаций, количество интервью и дублей, количество артефактов для съёмки, сложность заданных технических параметров монтажа, привлечение актёров для дубляжа и озвучки и прочее.
<i>Примеры:</i>
<a href="https://disk.yandex.ru/i/xZb7Je4waVKojg">Фрагмент фильма</a>
'''