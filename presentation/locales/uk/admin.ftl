# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = 👥 Команди
ADMIN-MCC = 🏦 MCC
ADMIN-MESSAGING = ✉️ Розсилка
ADMIN-PROFILE = 👤 Профіль

SKIP = ⏭️ Пропустити

# TEAMS ################################################################################
TEAMS-CREATE = ➕ Створити нову команду
TEAMS-CREATE-NAME = 🏷️ Назва для команди:
TEAMS-CREATE-SUCCESS = ✅ Команду <b>{$team}</b> успішно створено
TEAMS-CREATE-FAIL = ❌ Помилка при створені команди (<b>{$error}</b>)
#################
TEAMS-CREATE-NAME_ERROR = ⚠️ Довга назва (<b>{$symballs}</b>) символів, вкладись в 50
################################################################################
TEAMS-DETAIL = ℹ️ ID: {$team_id}
    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>
    Users: 👥 <b>{$count_users}</b>
    Created: 🗓️ <b>{$created}</b>

    💵 Загальна сума з усіх транзакцій: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = 🔑 Доступи команди
TEAMS-ACCESS-CREATE = ➕ Створити доступ
TEAMS-ACCESS-CREATE-CONFIRMANTION = ❓ Бажаєте створити одноразовий доступ до команди <b>{$team}</b>?
TEAMS-ACCESS-CREATE-SUCCESS = ✅ Доступ для (<b>{$team}</b>) успішно створено

    🔗 <code>{$deeplink}</code>
TEAMS-ACCESS-CREATE-FAIL = ❌ Помилка при створені доступу для (<b>{$team}</b>)
################################################################################
TEAMS-ACCESS-DETAIL = 🔑 Команда: <b>{$team}</b>

    🔗 DeepLink: <code>{$deeplink}</code>

    👤 User ID: <code>{$user_id}</code>
    UserName: @{$username}
    Ім'я: {$firstname}
    Прізвище: {$lastname}

    🕒 Доступ створено: <b>{$created}</b>
    🕒 Доступ активовано: <b>{$activated}</b>
##################################################################################
TEAMS-ACCESS-DELETE = 🗑️ Видалити доступ
TEAMS-ACCESS-DELETE-WARNING = ⚠️ При видаленні доступу користувач втратить свій функціонал

    ❗ <b>Точно видалити доступ?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = ✅ Підтвердити видалення
TEAMS-ACCESS-DELETE-SUCCESS = ✅ Доступ видалено
TEAMS-ACCESS-DELETE-FAIL = ❌ Не вдалося видалити доступ
#################################################################################
TEAMS-DELETE = 🗑️ Видалити команду
TEAMS-DELETE-WARNING = ⚠️ Ви точно бажаєте видалити команду (<b>{$team}</b>)?

    🔙 Повернути рішення буде не можливо!
TEAMS-DELETE-CONFIRMATION = ✅ Підтвердити видалення команди
TEAMS-DELETE-SUCCESS = ✅ Команду успішно видалено
TEAMS-DELETE-FAIL = ❌ Не вдалося видалити команду
###############################################
TEAMS-MCC-ACCESS = 🏦 MCC Розшарені для команди <b>{$team_name}</b>
TEAMS-MCC-ACCESS-DETAIL = ℹ️ <b>{$name}</b>
    👥 Доступно акаунтів: <b>{$account_available}</b>
    💰 Баланс команди: {$balance_team}$
    💰 Баланс: {$balance}$
TEAMS-MCC-ACCOUNTS-LIMIT = 🔢 Ліміт акаунтів
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE = 🔢 Введіть кількість акаунтів:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_ERROR = ⚠️ Потрібно ввести число від 0 до 999:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_DUBL = ℹ️ Наразі цей ліміт <b>{$limit}</b> вже встановлено, напишіть новий або скасуйте операцію:
TEAMS-MCC-ACCOUNTS-LIMIT-SUCCESS = ✅ Ліміт успішно змінено на <b>{$limit}</b>
TEAMS-MCC-ACCOUNTS-LIMIT-FAIL = ❌ Не вийшло змінити ліміт
TEAMS-MCC-SHARE = 🔗 Розшарити
TEAMS-MCC-SHARE-CHOICE = 🏦 Оберіть котрий MCC бажаєте розшарити для команди <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = ❌ Невдалося розшарити MCC <b>{$error}</b>
TEAMS-MCC-SHARE-SUCCESS = ✅ MCC (<b>{$mcc_name}</b>) Успішно розшарено для <b>{$team_name}</b>
TEAMS-MCC-RESHARE = 🔒 Прибрати доступ
TEAMS-MCC-RESHARE-CONFIRMATION = ❓ Точно прибрати доступ MCC (<b>{$mcc_name}</b>) для команди <b>{$team_name}</b>?
TEAMS-MCC-RESHARE-SUCCESS = ✅ Доступ прибрано
TEAMS-MCC-RESHARE-FAIL = ❌ Невдалося прибрати доступ
########## MCC ############################################################################
MCC-AUTH-FAIL = ❌ Помилка авторизації MCC <b>{$mcc_name}</b>
###############################################################
MCC-ADD = ➕ Додати новий MCC
MCC-ADD-NAME = 🏷️ Введіть ім'я для нового MCC:
MCC-ADD-WALLET = 👛 Введіть адресу гаманця для цього MCC:
MCC-ADD-ID = 🆔 Введіть ID для нового MCC:
MCC-ADD-SECRET_TOKEN = 🔑 Введіть Secret Token для нового MCC:
##########################################################
MCC-ADD-NAME_ERROR = ⚠️ Довга назва (<b>{$symballs}</b>) символів, вкладись в 50
MCC-ADD-SUCCESS = ✅ MCC <b>{$mcc_name}</b> успішно додано
MCC-ADD-FAIL = ❌ Помилка при додаванні MCC (<b>{$error}</b>)
###########################
MCC-DETAIL = ℹ️ <b>{$name}</b>
    💰 Баланс: {$balance}$
    🔓 Доступний для нових команд: <b>{$general}</b>
##############################################################
ACCOUNTS-DETAIL = ℹ️ <b>{$name}</b>
    =============================================
    🏦 MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    ✉️ Пошта: <code>{$email}</code>
    🌐 Тайм-зона: <b>{$timezone}</b>
    🆔 Ідентифікатор клієнта: <code>{$customer_id}</code>

    💰 Баланс: <b>{$balance}$</b>
    💸 Спенд: <b>{$spend}$</b>
    🛑 Ліміт: <b>{$limit}$</b>

    👥 Команда: <b>{$team_name}</b>
################## Messaging #################################################
MESSAGING-INPUT-MESSAGE = ✏️ Введіть повідомлення для розсилки:
MESSAGING-INPUT-IMAGE = 🖼️ Відправте фото в стисненому форматі або пропустіть
MESSAGING-SEND = ✉️ Відправити повідомлення
MESSAGING-RESULT = 📊 <b>-Результат розсилки-</b>

    📬 Отримали повідомлення: {$send}\{$users}
    🚫 Заблокували бота: {$block}
    ⚙️ Інше: {$other}
###################################################################################
TEAMS-TRANSACTIONS = 💸 Транзакції
TEAMS-TRANSACTIONS-MCC = 💵 Поповнення MCC
TEAMS-TRANSACTIONS-SUB = 💰 Внутрішні перекази
TEAMS-TRANSACTIONS-TAX = 🚕 Комісії
TEAMS-TRANSACTIONS-MCC-DETAIL = ℹ️ <b>MCC транзакція #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>

    💵 Сума поповнення: <b>{$value}$</b>
    🗓️ Дата створення заявки: <b>{$date}</b>

    🆔 Ідентифікатор транзакції: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-SUB-DETAIL = ℹ️ <b>Внутрішня транзакція #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>
    📧 Акаунт: <code>{$account_email}</code>

    💵 Сума поповнення: <b>{$value}$</b>
    🗓️ Дата переводу: <b>{$date}</b>

    🆔 Ідентифікатор транзакції: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-TAX-DETAIL = ℹ️ <b>Комісійна транзакція #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏢 Команда: <b>{$team_name}</b>
    🏦 MCC: <b>{$mcc_name}</b> ({$client_link})

    💼 Тип транзакції: <b>{$kind}</b>
    💵 Сума комісії: <b>{$amount} {$currency}</b>
    📄 Статус: <b>{$status}</b>
    📅 Дата: <b>{$date}</b>

    📧 Електронна пошта: <code>{$email}</code>

    📝 <b>{$desc}</b>

    🆔 Ідентифікатор транзакції: <code>{$uuid_transaction}</code>
#####################
TEAMS-MCC-BALANCE-ADD = 💰 Поповнити баланс
TEAMS-MCC-BALANCE-VALUE = 💵 Сума поповнення:
TEAMS-MCC-BALANCE-VALUE-ERROR = ⚠️ Потрібно ввести число:
TEAMS-MCC-BALANCE-CONFIRMATION = 💵 Сума поповнення <b>{$value}</b> вказана вірно?
TEAMS-MCC-BALANCE-CREATE-TRANSACTION = 🏦 Створити транзакцію
TEAMS-MCC-BALANCE-TOPUP-SUCCESS = ✅ MCC для команди успішно поповнено
TEAMS-MCC-BALANCE-TOPUP-TRANSACTION-FAIL = ❌ Не вдалося поповнити MCC для команди (<b>{$error}</b>)
#################
MCC-GENERAL-SWITCH = 🔄 General Вкл\Викл
################### CREATE ACCOUNT #########
ADMIN-ACCOUNT-CREATE = 🆕 Створити акаунт
ADMIN-ACCOUNT-CREATE-NAME = 🏷️ Вкажіть назву:
ADMIN-ACCOUNT-CREATE-NAME-ERROR = ⚠️ Назва має бути до 255 символів, зараз <b>{$len}</b>
ADMIN-ACCOUNT-CREATE-TEAM = 🆔 Вкажіть uuid команди:
ADMIN-ACCOUNT-CREATE-TEAM-ERROR = ❌ Тіми з таким uuid не існує
ADMIN-ACCOUNT-CREATE-TEAM-SKIP = ⏭️ Продовжити без команди
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_SKIP = ⏭️ Команду пропущено.
    ✉️ Вкажіть email:
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_CHOiCED = ✅ Обрана команда (<b>{$team_name}</b>).
    ✉️ Вкажіть email:
ADMIN-ACCOUNT-CREATE-AMOUNT = 💵 Сума поповнення (мін 50$):
ADMIN-ACCOUNT-CREATE-TIMEZONE = 🌐 Вкажіть тайм-зону, UTC(від -12 до +14), введіть число, наприклад +12 або -3:
ADMIN-ACCOUNT-CREATE-TIMEZONE-ERROR = ⚠️ Невірний формат. UTC(від -12 до +14), введіть число, наприклад +12 або -3:
ADMIN-ACCOUNT-CREATE-FAIL = ❌ Помилка при створенні акаунту
    Помилка: <b>{$error}</b>
ADMIN-ACCOUNT-CREATE-SUCCESS = ✅ Акаунт успішно створено! Чекай поки він з'явиться у тебе в акаунтах до вказаного MCC (<b>{$mcc_name}</b>)
##########
ADMIN-ACCOUNT-NO_VERIFY_YET = ⏱️ Акаунт ще не верифіковано, зайдіть пізніше
##################### CHANGE TEAM #################
ADMIN-ACCOUNT-CHANGE_TEAM = 🔄 Змінити команду
ADMIN-ACCOUNT-CHANGE_TEAM-UUID = 🆔 Вкажіть ідентифікатор команди:
ADMIN-ACCOUNT-CHANGE_TEAM-EXIST = ℹ️ Команда з таким ідентифікатором вже має цей акаунт
ADMIN-ACCOUNT-CHANGE_TEAM-ERROR = ❌ Немає команди з таким ідентифікатором
ADMIN-ACCOUNT-CHANGE_TEAM-SUCCESS = ✅ Успішно передано команді <b>{$team_name}</b>
ADMIN-ACCOUNT-CHANGE_TEAM-FAIL = ❌ Не вийшло змінити команду для акаунта

#######################################
# Account (change email, refund, topup)
Change Email ###
ADMIN-ACCOUNT-CHANGE_EMAIL = ✉️ Змінити email
ADMIN-ACCOUNT-CHANGE_EMAIL-INPUT = ✉️ Вкажіть новий email
ADMIN-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Не вийшло змінити email
ADMIN-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Формат Email не дійсний
ADMIN-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email успішно змінено на <b>{$email}</b>
# Refund ###
ADMIN-ACCOUNT-REFUND = 💸 Рефаунд
ADMIN-ACCOUNT-REFUND-CONFIRMATION-WARNING = ❓ Ви точно хочете зробити рефаунд акаунту <b>{$account_name}</b>?

    💵 Баланс акаунту (<b>{$balance}$</b>) буде повернено на головний MCC
ADMIN-ACCOUNT-REFUND-CONFIRMATION = ✅ Підтвердити рефаунд
ADMIN-ACCOUNT-REFUND-FAIL = ❌ Виникла помилка. Не вийшло зробити рефаунд
ADMIN-ACCOUNT-REFUND-SUCCESS = ✅ Запит на рефаунд відправлено успішно
# TopUp ###
ADMIN-ACCOUNT-TOPUP = 💳 Поповнити
ADMIN-ACCOUNT-TOPUP-VALUE = 💵 Введіть суму поповнення від <b>50$</b>:
ADMIN-ACCOUNT-TOPUP-VALUE-ERROR = ⚠️ Потрібно ввести число від <b>50$</b> до <b>10.000$</b>:
ADMIN-ACCOUNT-TOPUP-WARNING = ❓ Поповнити баланс акаунту на <b>{$value}$</b>?
ADMIN-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Недостатній баланс на акаунті.
    Ваш баланс: <b>{$balance}$</b>
    Запит на поповнення: <b>{$value}$</b>
ADMIN-ACCOUNT-TOPUP-CONFIRMATION = ✅ Підтвердити поповнення
ADMIN-ACCOUNT-TOPUP-FAIL = ❌ Помилка при поповненні
ADMIN-ACCOUNT-TOPUP-SUCCESS = ✅ Успішно поповненно
################################## Specific API Functions #################################
ADMIN-SPECIFIC = ⚙️ Додатково
#LOAD ACCOUNTS#
ADMIN-SPECIFIC-LOAD = 🔄 Підгрузити акаунти
ADMIN-SPECIFIC-LOAD-CHOICE_MCC = Оберіть MCC
ADMIN-SPECIFIC-LOAD-WARNING = ⚠️ Зараз буде запущено процес завантаження нових акаунтів з усіх доданих в бота MCC! При виконанні цього процесу акаунти яких ще немає в базі бота, будуть записані до відповідного MCC.

    ❗ <b>Натисніть тільки один раз, це ресурсозатратний процес</b>
ADMIN-SPECIFIC-LOAD-CONFIRMATION = ✅ Підтвердити завантаження
ADMIN-SPECIFIC-LOAD-PROCESSING = ⏳ Почалося завантаження, це займе деякий час
ADMIN-SPECIFIC-LOAD-PART = MCC <b>{$mcc_name}</b> Завантажено <b>{$new_accounts}</b> нових акаунтів. ({$current_accounts}/{$all_accounts})
ADMIN-SPECIFIC-LOAD-RESULT = ✅ Успішно завантажено нових акаунтів: <b>{$new_accounts}</b> 📊

    {$statistic}
ADMIN-SPECIFIC-LOAD-FAIL = ❌ Помилка додавання акаунту <b>{$email}</b> на MCC <b>{$mcc_name}</b>


#TAX PAYMENT#
ADMIN-SPECIFIC-TAX = 🔎 Завантажити комісійні транзакції
ADMIN-SPECIFIC-TAX-DOCUMENT = Надішліть <b>.csv</b> документ для аналізу
ADMIN-SPECIFIC-TAX-NO_DOCUMENT = Неправильний формат файлу ❌ Надішліть <b>.csv</b> документ
ADMIN-SPECIFIC-TAX-ERROR = Виникла помилка ❌
    <code>{$error}</code>
ADMIN-SPECIFIC-TAX-FAIL = Виникла помилка ❌ <b>{$email}</b>
    <code>{$error}</code>
ADMIN-SPECIFIC-TAX-SUCCESS = Транзакція додана ✅ | <b>{$amount} {$currency}</b>
    {$client_link}➡️{$mcc_name} | {$team} | {$date}
    {$status} | {$email}
    {$desc}
ADMIN-SPECIFIC-TAX-SUMMARY = Аналіз файлу закінчено

    Знайдено операцій у файлі: {$taxes_count}
    Успішно оброблених: {$taxes_success} ✅
    Помилка або повтор: {$taxes_fail} ❌

    Оброблені транзакції можна подивитися в історії транзакцій або в google таблицях по посиланню ничже
    (Аналітика в Google Sheet оновлюється кожен день зранку, проте в боті миттєво)
ADMIN-SPECIFIC-TAX-GOOGLE_SHEET = Аналітика в Google Таблицях

MESSAGING-TAX-RESULT = <b>{$team_name}</b>
    -------
    📬 Отримали: {$send}\{$users}
    🚫 Заблокували бота: {$block}
    ⚙️ Інше: {$other}
    ====================================


###########################################
ADMIN-SEARCH-ACCOUNT = 🔎 Пошук акаунту
ADMIN-SEARCH-ACCOUNT-EMAIL = 📨 Введіть email для пошуку акаунта:
ADMIN-SEARCH-ACCOUNT-NOTHING = ❌ Акаунту з таким email не знайдено

