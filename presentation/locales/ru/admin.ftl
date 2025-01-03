#### Russian Translation ####

# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = 👥 Команды
ADMIN-MCC = 🏦 MCC
ADMIN-MESSAGING = ✉️ Рассылка
ADMIN-PROFILE = 👤 Профиль

SKIP = ⏭️ Пропустить

# TEAMS ################################################################################
TEAMS-CREATE = ➕ Создать новую команду
TEAMS-CREATE-NAME = 🏛️ Название команды:
TEAMS-CREATE-SUCCESS = ✅ Команда <b>{$team}</b> успешно создана
TEAMS-CREATE-FAIL = ❌ Ошибка при создании команды (<b>{$error}</b>)
#################
TEAMS-CREATE-NAME_ERROR = ⚠️ Слишком длинное название (<b>{$symballs}</b> символов), должно быть до 50
################################################################################
TEAMS-DETAIL = ℹ️ ID: {$team_id}
    Команда: <b>{$team_name}</b>
    UUID команды: <code>{$team_uuid}</code>
    Пользователей: 👥 <b>{$count_users}</b>
    Создана: 🗓️ <b>{$created}</b>

    💵 Общая сумма всех транзакций: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = 🔑 Доступ к команде
TEAMS-ACCESS-CREATE = ➕ Создать доступ
TEAMS-ACCESS-CREATE-CONFIRMANTION = ❓ Хотите создать одноразовый доступ для команды <b>{$team}</b>?
TEAMS-ACCESS-CREATE-SUCCESS = ✅ Доступ для (<b>{$team}</b>) успешно создан

    🔗 <code>{$deeplink}</code>
TEAMS-ACCESS-CREATE-FAIL = ❌ Ошибка при создании доступа для (<b>{$team}</b>)
################################################################################
TEAMS-ACCESS-DETAIL = 🔑 Команда: <b>{$team}</b>

    🔗 DeepLink: <code>{$deeplink}</code>

    👤 ID пользователя: <code>{$user_id}</code>
    Имя пользователя: @{$username}
    Имя: {$firstname}
    Фамилия: {$lastname}

    🕒 Доступ создан: <b>{$created}</b>
    🕒 Доступ активирован: <b>{$activated}</b>
##################################################################################
TEAMS-ACCESS-DELETE = 🗑️ Удалить доступ
TEAMS-ACCESS-DELETE-WARNING = ⚠️ Удаление доступа аннулирует все связанные функции.

    ❗ <b>Вы уверены, что хотите удалить доступ?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = ✅ Подтвердить удаление
TEAMS-ACCESS-DELETE-SUCCESS = ✅ Доступ удалён
TEAMS-ACCESS-DELETE-FAIL = ❌ Ошибка при удалении доступа
#################################################################################
TEAMS-DELETE = 🗑️ Удалить команду
TEAMS-DELETE-WARNING = ⚠️ Вы уверены, что хотите удалить команду (<b>{$team}</b>)?

    🖙 Это действие необратимо!
TEAMS-DELETE-CONFIRMATION = ✅ Подтвердить удаление команды
TEAMS-DELETE-SUCCESS = ✅ Команда успешно удалена
TEAMS-DELETE-FAIL = ❌ Ошибка при удалении команды
###############################################
TEAMS-MCC-ACCESS = 🏦 Общие MCC для команды <b>{$team_name}</b>
TEAMS-MCC-ACCESS-DETAIL = ℹ️ <b>{$name}</b>
    👥 Доступные аккаунты: <b>{$account_available}</b>
    💰 Баланс команды: {$balance_team}$
    💰 Баланс: {$balance}$
TEAMS-MCC-ACCOUNTS-LIMIT = 🔢 Лимит аккаунтов
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE = 🔢 Введите количество аккаунтов:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_ERROR = ⚠️ Нужно ввести число от 0 до 999:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_DUBL = ℹ️ Текущий лимит <b>{$limit}</b> уже установлен, укажите новый или отмените операцию:
TEAMS-MCC-ACCOUNTS-LIMIT-SUCCESS = ✅ Лимит успешно обновлён до <b>{$limit}</b>
TEAMS-MCC-ACCOUNTS-LIMIT-FAIL = ❌ Ошибка при обновлении лимита
TEAMS-MCC-SHARE = 🔗 Поделиться
TEAMS-MCC-SHARE-CHOICE = 🏦 Выберите MCC, который хотите предоставить команде <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = ❌ Ошибка при предоставлении MCC <b>{$error}</b>
TEAMS-MCC-SHARE-SUCCESS = ✅ MCC (<b>{$mcc_name}</b>) успешно предоставлен команде <b>{$team_name}</b>
TEAMS-MCC-RESHARE = 🔒 Удалить доступ
TEAMS-MCC-RESHARE-CONFIRMATION = ❓ Вы уверены, что хотите удалить доступ к MCC (<b>{$mcc_name}</b>) для команды <b>{$team_name}</b>?
TEAMS-MCC-RESHARE-SUCCESS = ✅ Доступ удалён
TEAMS-MCC-RESHARE-FAIL = ❌ Ошибка при удалении доступа
########## MCC ############################################################################
MCC-AUTH-FAIL = ❌ Ошибка авторизации MCC <b>{$mcc_name}</b>
###############################################################
MCC-ADD = ➕ Добавить новый MCC
MCC-ADD-NAME = 🏛️ Укажите имя нового MCC:
MCC-ADD-WALLET = 💼 Укажите адрес кошелька для этого MCC:
MCC-ADD-ID = 🖔 Укажите ID для нового MCC:
MCC-ADD-SECRET_TOKEN = 🔑 Укажите Secret Token для нового MCC:
##########################################################
MCC-ADD-NAME_ERROR = ⚠️ Слишком длинное название (<b>{$symballs}</b> символов), должно быть до 50
MCC-ADD-SUCCESS = ✅ MCC <b>{$mcc_name}</b> успешно добавлен
MCC-ADD-FAIL = ❌ Ошибка при добавлении MCC (<b>{$error}</b>)
###########################
MCC-DETAIL = ℹ️ <b>{$name}</b>
    💰 Баланс: {$balance}$
    🔒 Доступен для новых команд: <b>{$general}</b>
##############################################################
ACCOUNTS-DETAIL = ℹ️ <b>{$name}</b>
    =============================================
    🏦 MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    ✉️ Почта: <code>{$email}</code>
    🌐 Часовой пояс: <b>{$timezone}</b>
    🖔 ID клиента: <code>{$customer_id}</code>

    💰 Баланс: <b>{$balance}$</b>
    💸 Расходы: <b>{$spend}$</b>
    🚷 Лимит: <b>{$limit}$</b>

    👥 Команда: <b>{$team_name}</b>
################## Messaging #################################################
MESSAGING-INPUT-MESSAGE = ✏️ Введите сообщение для рассылки:
MESSAGING-INPUT-IMAGE = 🖼️ Отправьте сжатое изображение или пропустите
MESSAGING-SEND = ✉️ Отправить сообщение
MESSAGING-RESULT = 📊 <b>-Результаты рассылки-</b>

    📨 Сообщения получили: {$send}\{$users}
    ⛔ Заблокировали бота: {$block}
    ⚙️ Другое: {$other}
###################################################################################
TEAMS-TRANSACTIONS = 💸 Транзакции
TEAMS-TRANSACTIONS-MCC = 💵 Пополнения MCC
TEAMS-TRANSACTIONS-SUB = 💰 Внутренние переводы
TEAMS-TRANSACTIONS-TAX = 🚓 Комиссии
TEAMS-TRANSACTIONS-MCC-DETAIL = ℹ️ <b>Транзакция MCC #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>

    💵 Сумма пополнения: <b>{$value}$</b>
    🗓️ Дата подачи заявки: <b>{$date}</b>

    🖔 ID транзакции: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-SUB-DETAIL = ℹ️ <b>Внутренняя транзакция #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>
    ✉️ Аккаунт: <code>{$account_email}</code>

    💵 Сумма перевода: <b>{$value}$</b>
    🗓️ Дата перевода: <b>{$date}</b>

    🖔 ID транзакции: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-TAX-DETAIL = ℹ️ <b>Комиссионная транзакция #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━
    🏢 Команда: <b>{$team_name}</b>
    🏦 MCC: <b>{$mcc_name}</b> ({$client_link})

    💼 Тип транзакции: <b>{$kind}</b>
    💵 Сумма комиссии: <b>{$amount} {$currency}</b>
    📄 Статус: <b>{$status}</b>
    🔢 Дата: <b>{$date}</b>

    ✉️ Почта: <code>{$email}</code>

    🗋 <b>{$desc}</b>

    🖔 ID транзакции: <code>{$uuid_transaction}</code>
#####################
TEAMS-MCC-BALANCE-ADD = 💰 Пополнить баланс
TEAMS-MCC-BALANCE-VALUE = 💵 Сумма пополнения:
TEAMS-MCC-BALANCE-VALUE-ERROR = ⚠️ Нужно ввести число:
TEAMS-MCC-BALANCE-CONFIRMATION = 💵 Сумма пополнения <b>{$value}</b> указана верно?
TEAMS-MCC-BALANCE-CREATE-TRANSACTION = 🏦 Создать транзакцию
TEAMS-MCC-BALANCE-TOPUP-SUCCESS = ✅ MCC успешно пополнен для команды
TEAMS-MCC-BALANCE-TOPUP-TRANSACTION-FAIL = ❌ Ошибка при пополнении MCC для команды (<b>{$error}</b>)
#################
MCC-GENERAL-SWITCH = 🔄 General Вкл\Выкл
################### CREATE ACCOUNT #########
ADMIN-ACCOUNT-CREATE = 🔧 Создать аккаунт
ADMIN-ACCOUNT-CREATE-NAME = 🏛️ Укажите название:
ADMIN-ACCOUNT-CREATE-NAME-ERROR = ⚠️ Название должно быть до 255 символов, сейчас <b>{$len}</b>
ADMIN-ACCOUNT-CREATE-TEAM = 🖔 Укажите UUID команды:
ADMIN-ACCOUNT-CREATE-TEAM-ERROR = ❌ Команды с таким UUID не существует
ADMIN-ACCOUNT-CREATE-TEAM-SKIP = ⏭️ Продолжить без команды
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_SKIP = ⏭️ Команда пропущена.
    ✉️ Укажите почту:
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_CHOiCED = ✅ Выбрана команда (<b>{$team_name}</b>).
    ✉️ Укажите почту:
ADMIN-ACCOUNT-CREATE-AMOUNT = 💵 Сумма пополнения (мин $50):
ADMIN-ACCOUNT-CREATE-TIMEZONE = 🌐 Укажите часовой пояс, UTC(от -12 до +14), введите число, например +12 или -3:
ADMIN-ACCOUNT-CREATE-TIMEZONE-ERROR = ⚠️ Неверный формат. UTC(от -12 до +14), введите число, например +12 или -3:
ADMIN-ACCOUNT-CREATE-FAIL = ❌ Ошибка при создании аккаунта
    Ошибка: <b>{$error}</b>
ADMIN-ACCOUNT-CREATE-SUCCESS = ✅ Аккаунт успешно создан! Ожидайте, пока он появится в ваших аккаунтах в указанном MCC (<b>{$mcc_name}</b>)
##########
ADMIN-ACCOUNT-NO_VERIFY_YET = ⏳ Аккаунт ещё не подтверждён, зайдите позже
##################### CHANGE TEAM #################
ADMIN-ACCOUNT-CHANGE_TEAM = 🔄 Изменить команду
ADMIN-ACCOUNT-CHANGE_TEAM-UUID = 🖔 Укажите ID команды:
ADMIN-ACCOUNT-CHANGE_TEAM-EXIST = ℹ️ Эта команда уже содержит данный аккаунт
ADMIN-ACCOUNT-CHANGE_TEAM-ERROR = ❌ Команда с таким ID не найдена
ADMIN-ACCOUNT-CHANGE_TEAM-SUCCESS = ✅ Успешно передано команде <b>{$team_name}</b>
ADMIN-ACCOUNT-CHANGE_TEAM-FAIL = ❌ Не удалось изменить команду для аккаунта

#######################################
# Account (change email, refund, topup)
Change Email ###
ADMIN-ACCOUNT-CHANGE_EMAIL = ✉️ Изменить почту
ADMIN-ACCOUNT-CHANGE_EMAIL-INPUT = ✉️ Укажите новую почту
ADMIN-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Ошибка при изменении почты
ADMIN-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Неверный формат почты
ADMIN-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Почта успешно изменена на <b>{$email}</b>
# Refund ###
ADMIN-ACCOUNT-REFUND = 💸 Возврат средств
ADMIN-ACCOUNT-REFUND-CONFIRMATION-WARNING = ❓ Вы уверены, что хотите сделать возврат средств для аккаунта <b>{$account_name}</b>?

    💵 Баланс аккаунта (<b>{$balance}$</b>) будет возвращён на основной MCC
ADMIN-ACCOUNT-REFUND-CONFIRMATION = ✅ Подтвердить возврат средств
ADMIN-ACCOUNT-REFUND-FAIL = ❌ Ошибка. Не удалось выполнить возврат средств
ADMIN-ACCOUNT-REFUND-SUCCESS = ✅ Запрос на возврат средств успешно отправлен
# TopUp ###
ADMIN-ACCOUNT-TOPUP = 💳 Пополнение
ADMIN-ACCOUNT-TOPUP-VALUE = 💵 Введите сумму пополнения от <b>$50</b>:
ADMIN-ACCOUNT-TOPUP-VALUE-ERROR = ⚠️ Введите число от <b>$50</b> до <b>$10,000</b>:
ADMIN-ACCOUNT-TOPUP-WARNING = ❓ Пополнить баланс аккаунта на <b>{$value}$</b>?
ADMIN-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Недостаточный баланс на аккаунте.
    Ваш баланс: <b>{$balance}$</b>
    Запрос на пополнение: <b>{$value}$</b>
ADMIN-ACCOUNT-TOPUP-CONFIRMATION = ✅ Подтвердить пополнение
ADMIN-ACCOUNT-TOPUP-FAIL = ❌ Ошибка при пополнении
ADMIN-ACCOUNT-TOPUP-SUCCESS = ✅ Успешно пополнено
################################## Specific API Functions #################################
ADMIN-SPECIFIC = ⚙️ Дополнительно
#LOAD ACCOUNTS#
ADMIN-SPECIFIC-LOAD = 🔄 Загрузить аккаунты
ADMIN-SPECIFIC-LOAD-CHOICE_MCC = Выберите MCC
ADMIN-SPECIFIC-LOAD-WARNING = ⚠️ Начинается процесс загрузки новых аккаунтов из всех MCC, добавленных в бота! В процессе выполнения аккаунты, которых ещё нет в базе бота, будут привязаны к соответствующему MCC.

    ❗ <b>Нажмите только один раз, этот процесс требует много ресурсов</b>
ADMIN-SPECIFIC-LOAD-CONFIRMATION = ✅ Подтвердить загрузку
ADMIN-SPECIFIC-LOAD-PROCESSING = ⏳ Загрузка началась, это может занять некоторое время
ADMIN-SPECIFIC-LOAD-PART = MCC <b>{$mcc_name}</b> Загружено <b>{$new_accounts}</b> новых аккаунтов. ({$current_accounts}/{$all_accounts})
ADMIN-SPECIFIC-LOAD-RESULT = ✅ Успешно загружено новых аккаунтов: <b>{$new_accounts}</b> 📊

    {$statistic}
ADMIN-SPECIFIC-LOAD-FAIL = ❌ Ошибка при добавлении аккаунта <b>{$email}</b> в MCC <b>{$mcc_name}</b>


#TAX PAYMENT#
ADMIN-SPECIFIC-TAX = 🔎 Загрузить комиссионные транзакции
ADMIN-SPECIFIC-TAX-DOCUMENT = Отправьте документ <b>.csv</b> для анализа
ADMIN-SPECIFIC-TAX-NO_DOCUMENT = Неверный формат файла ❌ Отправьте документ <b>.csv</b>
ADMIN-SPECIFIC-TAX-ERROR = Произошла ошибка ❌
    <code>{$error}</code>
ADMIN-SPECIFIC-TAX-FAIL = Произошла ошибка ❌ <b>{$email}</b>
    <code>{$error}</code>
ADMIN-SPECIFIC-TAX-SUCCESS = Транзакция добавлена ✅ | <b>{$amount} {$currency}</b>
    {$client_link}➡️{$mcc_name} | {$team} | {$date}
    {$status} | {$email}
    {$desc}
ADMIN-SPECIFIC-TAX-SUMMARY = Анализ файла завершён

    Найдено транзакций в файле: {$taxes_count}
    Успешно обработано: {$taxes_success} ✅
    Ошибки или дубликаты: {$taxes_fail} ❌

    Обработанные транзакции можно просмотреть в истории транзакций или в Google Sheets по ссылке ниже.
    (Аналитика в Google Sheets обновляется каждое утро, а в боте моментально)
ADMIN-SPECIFIC-TAX-GOOGLE_SHEET = Аналитика в Google Sheets

MESSAGING-TAX-RESULT = <b>{$team_name}</b>
    -------
    📨 Получено: {$send}\{$users}
    ⛔ Заблокировали бота: {$block}
    ⚙️ Другое: {$other}
    ====================================


###########################################
ADMIN-SEARCH-ACCOUNT = 🔎 Поиск аккаунта
ADMIN-SEARCH-ACCOUNT-EMAIL = ✉️ Введите почту для поиска аккаунта:
ADMIN-SEARCH-ACCOUNT-NOTHING = ❌ Аккаунт с такой почтой не найден
