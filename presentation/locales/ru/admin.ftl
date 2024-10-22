# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = 👥 Команды
ADMIN-MCC = 🏦 MCC
ADMIN-MESSAGING = ✉️ Рассылка
ADMIN-PROFILE = 👤 Профиль

SKIP = ⏭️ Пропустить

# TEAMS ################################################################################
TEAMS-CREATE = ➕ Создать новую команду
TEAMS-CREATE-NAME = 🏷️ Название для команды:
TEAMS-CREATE-SUCCESS = ✅ Команда <b>{$team}</b> успешно создана
TEAMS-CREATE-FAIL = ❌ Ошибка при создании команды (<b>{$error}</b>)
#################
TEAMS-CREATE-NAME_ERROR = ⚠️ Слишком длинное название (<b>{$symballs}</b> символов), должно быть не более 50
################################################################################
TEAMS-DETAIL = ℹ️ ID: {$team_id}
    Команда: <b>{$team_name}</b>
    UUID команды: <code>{$team_uuid}</code>
    Пользователей: 👥 <b>{$count_users}</b>
    Создано: 🗓️ <b>{$created}</b>

    💵 Общая сумма всех транзакций: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = 🔑 Доступы команды
TEAMS-ACCESS-CREATE = ➕ Создать доступ
TEAMS-ACCESS-CREATE-CONFIRMANTION = ❓ Хотите создать одноразовый доступ к команде <b>{$team}</b>?
TEAMS-ACCESS-CREATE-SUCCESS = ✅ Доступ для (<b>{$team}</b>) успешно создан

    🔗 <code>{$deeplink}</code>
TEAMS-ACCESS-CREATE-FAIL = ❌ Ошибка при создании доступа для (<b>{$team}</b>)
################################################################################
TEAMS-ACCESS-DETAIL = 🔑 Команда: <b>{$team}</b>

    🔗 DeepLink: <code>{$deeplink}</code>

    👤 User ID: <code>{$user_id}</code>
    UserName: @{$username}
    Имя: {$firstname}
    Фамилия: {$lastname}

    🕒 Доступ создан: <b>{$created}</b>
    🕒 Доступ активирован: <b>{$activated}</b>
##################################################################################
TEAMS-ACCESS-DELETE = 🗑️ Удалить доступ
TEAMS-ACCESS-DELETE-WARNING = ⚠️ При удалении доступа пользователь потеряет свои функции

    ❗ <b>Точно удалить доступ?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = ✅ Подтвердить удаление
TEAMS-ACCESS-DELETE-SUCCESS = ✅ Доступ удален
TEAMS-ACCESS-DELETE-FAIL = ❌ Не удалось удалить доступ
#################################################################################
TEAMS-DELETE = 🗑️ Удалить команду
TEAMS-DELETE-WARNING = ⚠️ Вы точно хотите удалить команду (<b>{$team}</b>)?

    🔙 Это действие невозможно будет отменить!
TEAMS-DELETE-CONFIRMATION = ✅ Подтвердить удаление команды
TEAMS-DELETE-SUCCESS = ✅ Команда успешно удалена
TEAMS-DELETE-FAIL = ❌ Не удалось удалить команду
###############################################
TEAMS-MCC-ACCESS = 🏦 MCC доступные для команды <b>{$team_name}</b>
TEAMS-MCC-ACCESS-DETAIL = ℹ️ <b>{$name}</b>
    👥 Доступно аккаунтов: <b>{$account_available}</b>
    💰 Баланс команды: {$balance_team}$
    💰 Баланс: {$balance}$
TEAMS-MCC-ACCOUNTS-LIMIT = 🔢 Лимит аккаунтов
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE = 🔢 Введите количество аккаунтов:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_ERROR = ⚠️ Введите число от 0 до 999:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_DUBL = ℹ️ Текущий лимит уже <b>{$limit}</b>, введите новый или отмените операцию:
TEAMS-MCC-ACCOUNTS-LIMIT-SUCCESS = ✅ Лимит успешно изменен на <b>{$limit}</b>
TEAMS-MCC-ACCOUNTS-LIMIT-FAIL = ❌ Не удалось изменить лимит
TEAMS-MCC-SHARE = 🔗 Поделиться доступом
TEAMS-MCC-SHARE-CHOICE = 🏦 Выберите, какой MCC хотите предоставить для команды <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = ❌ Не удалось предоставить доступ к MCC <b>{$error}</b>
TEAMS-MCC-SHARE-SUCCESS = ✅ Доступ к MCC (<b>{$mcc_name}</b>) успешно предоставлен команде <b>{$team_name}</b>
TEAMS-MCC-RESHARE = 🔒 Убрать доступ
TEAMS-MCC-RESHARE-CONFIRMATION = ❓ Точно убрать доступ MCC (<b>{$mcc_name}</b>) для команды <b>{$team_name}</b>?
TEAMS-MCC-RESHARE-SUCCESS = ✅ Доступ убран
TEAMS-MCC-RESHARE-FAIL = ❌ Не удалось убрать доступ
########## MCC ############################################################################
MCC-AUTH-FAIL = ❌ Ошибка авторизации MCC <b>{$mcc_name}</b>
###############################################################
MCC-ADD = ➕ Добавить новый MCC
MCC-ADD-NAME = 🏷️ Введите имя для нового MCC:
MCC-ADD-ID = 🆔 Введите ID для нового MCC:
MCC-ADD-SECRET_TOKEN = 🔑 Введите Secret Token для нового MCC:
##########################################################
MCC-ADD-NAME_ERROR = ⚠️ Слишком длинное имя (<b>{$symballs}</b> символов), должно быть не более 50
MCC-ADD-SUCCESS = ✅ MCC <b>{$mcc_name}</b> успешно добавлен
MCC-ADD-FAIL = ❌ Ошибка при добавлении MCC (<b>{$error}</b>)
###########################
MCC-DETAIL = ℹ️ <b>{$name}</b>
    💰 Баланс: {$balance}$
    🔓 Доступен для новых команд: <b>{$general}</b>
##############################################################
ACCOUNTS-DETAIL = ℹ️ <b>{$name}</b>
    =============================================
    🏦 MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    ✉️ Почта: <code>{$email}</code>
    🌐 Тайм-зона: <b>{$timezone}</b>
    🆔 Идентификатор клиента: <code>{$customer_id}</code>

    💰 Баланс: <b>{$balance}$</b>
    💸 Траты: <b>{$spend}$</b>
    🛑 Лимит: <b>{$limit}$</b>

    👥 Команда: <b>{$team_name}</b>
################## Messaging #################################################
MESSAGING-INPUT-MESSAGE = ✏️ Введите сообщение для рассылки:
MESSAGING-INPUT-IMAGE = 🖼️ Отправьте фото в сжатом формате или пропустите
MESSAGING-SEND = ✉️ Отправить сообщение
MESSAGING-RESULT = 📊 <b>-Результат рассылки-</b>

    📬 Получили сообщение: {$send}\{$users}
    🚫 Заблокировали бота: {$block}
    ⚙️ Другое: {$other}
###################################################################################
TEAMS-TRANSACTIONS = 💸 Транзакции
TEAMS-TRANSACTIONS-MCC = 💵 Пополнение MCC
TEAMS-TRANSACTIONS-SUB = 💰 Внутренние переводы
TEAMS-TRANSACTIONS-MCC-DETAIL = ℹ️ <b>MCC транзакция #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>

    💵 Сумма пополнения: <b>{$value}$</b>
    🗓️ Дата создания заявки: <b>{$date}</b>

    🆔 Идентификатор транзакции: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-SUB-DETAIL = ℹ️ <b>Внутренняя транзакция #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>
    📧 Аккаунт: <code>{$account_email}</code>

    💵 Сумма пополнения: <b>{$value}$</b>
    🗓️ Дата перевода: <b>{$date}</b>

    🆔 Идентификатор транзакции: <code>{$uuid_transaction}</code>
#####################
TEAMS-MCC-BALANCE-ADD = 💰 Пополнить баланс
TEAMS-MCC-BALANCE-VALUE = 💵 Сумма пополнения:
TEAMS-MCC-BALANCE-VALUE-ERROR = ⚠️ Введите число:
TEAMS-MCC-BALANCE-CONFIRMATION = 💵 Сумма пополнения <b>{$value}</b> указана верно?
TEAMS-MCC-BALANCE-CREATE-TRANSACTION = 🏦 Создать транзакцию
TEAMS-MCC-BALANCE-TOPUP-SUCCESS = ✅ MCC для команды успешно пополнен
TEAMS-MCC-BALANCE-TOPUP-TRANSACTION-FAIL = ❌ Не удалось пополнить MCC для команды (<b>{$error}</b>)
#################
MCC-GENERAL-SWITCH = 🔄 General Вкл\Выкл
################### CREATE ACCOUNT #########
ADMIN-ACCOUNT-CREATE = 🆕 Создать аккаунт
ADMIN-ACCOUNT-CREATE-NAME = 🏷️ Укажите название:
ADMIN-ACCOUNT-CREATE-NAME-ERROR = ⚠️ Название должно быть до 255 символов, сейчас <b>{$len}</b>
ADMIN-ACCOUNT-CREATE-TEAM = 🆔 Укажите uuid команды:
ADMIN-ACCOUNT-CREATE-TEAM-ERROR = ❌ Команды с таким uuid не существует
ADMIN-ACCOUNT-CREATE-TEAM-SKIP = ⏭️ Продолжить без команды
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_SKIP = ⏭️ Команда пропущена.
    ✉️ Укажите email:
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_CHOiCED = ✅ Выбрана команда (<b>{$team_name}</b>).
    ✉️ Укажите email:
ADMIN-ACCOUNT-CREATE-AMOUNT = 💵 Сумма пополнения (мин 50$):
ADMIN-ACCOUNT-CREATE-TIMEZONE = 🌐 Укажите тайм-зону, UTC (от -12 до +14), введите число, например +12 или -3:
ADMIN-ACCOUNT-CREATE-TIMEZONE-ERROR = ⚠️ Неверный формат. UTC (от -12 до +14), введите число, например +12 или -3:
ADMIN-ACCOUNT-CREATE-FAIL = ❌ Ошибка при создании аккаунта
    Ошибка: <b>{$error}</b>
ADMIN-ACCOUNT-CREATE-SUCCESS = ✅ Аккаунт успешно создан! Ожидайте его появления в аккаунтах в соответствующем MCC (<b>{$mcc_name}</b>)
##########
ADMIN-ACCOUNT-NO_VERIFY_YET = ⏱️ Аккаунт еще не верифицирован, зайдите позже
##################### CHANGE TEAM #################
ADMIN-ACCOUNT-CHANGE_TEAM = 🔄 Изменить команду
ADMIN-ACCOUNT-CHANGE_TEAM-UUID = 🆔 Укажите идентификатор команды:
ADMIN-ACCOUNT-CHANGE_TEAM-EXIST = ℹ️ Команда с таким идентификатором уже имеет этот аккаунт
ADMIN-ACCOUNT-CHANGE_TEAM-ERROR = ❌ Команды с таким идентификатором не существует
ADMIN-ACCOUNT-CHANGE_TEAM-SUCCESS = ✅ Успешно передано команде <b>{$team_name}</b>
ADMIN-ACCOUNT-CHANGE_TEAM-FAIL = ❌ Не удалось изменить команду для аккаунта

#######################################
# Account (change email, refund, topup)
Change Email ###
ADMIN-ACCOUNT-CHANGE_EMAIL = ✉️ Изменить email
ADMIN-ACCOUNT-CHANGE_EMAIL-INPUT = ✉️ Укажите новый email
ADMIN-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Не удалось изменить email
ADMIN-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Неверный формат Email
ADMIN-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email успешно изменён на <b>{$email}</b>
# Refund ###
ADMIN-ACCOUNT-REFUND = 💸 Возврат
ADMIN-ACCOUNT-REFUND-CONFIRMATION-WARNING = ❓ Вы точно хотите сделать возврат аккаунта <b>{$account_name}</b>?

    💵 Баланс аккаунта (<b>{$balance}$</b>) будет возвращён на основной MCC
ADMIN-ACCOUNT-REFUND-CONFIRMATION = ✅ Подтвердить возврат
ADMIN-ACCOUNT-REFUND-FAIL = ❌ Возникла ошибка. Не удалось сделать возврат
ADMIN-ACCOUNT-REFUND-SUCCESS = ✅ Запрос на возврат успешно отправлен
# TopUp ###
ADMIN-ACCOUNT-TOPUP = 💳 Пополнить
ADMIN-ACCOUNT-TOPUP-VALUE = 💵 Введите сумму пополнения от <b>50$</b>:
ADMIN-ACCOUNT-TOPUP-VALUE-ERROR = ⚠️ Введите число от <b>50$</b> до <b>10.000$</b>:
ADMIN-ACCOUNT-TOPUP-WARNING = ❓ Пополнить баланс аккаунта на <b>{$value}$</b>?
ADMIN-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Недостаточно средств на аккаунте.
    Ваш баланс: <b>{$balance}$</b>
    Запрос на пополнение: <b>{$value}$</b>
ADMIN-ACCOUNT-TOPUP-CONFIRMATION = ✅ Подтвердить пополнение
ADMIN-ACCOUNT-TOPUP-FAIL = ❌ Ошибка при пополнении
ADMIN-ACCOUNT-TOPUP-SUCCESS = ✅ Успешно пополнено
################################## Specific API Functions #################################
ADMIN-SPECIFIC = ⚙️ Дополнительно
ADMIN-SPECIFIC-LOAD = 🔄 Загрузить аккаунты
ADMIN-SPECIFIC-LOAD-WARNING = ⚠️ Сейчас будет запущен процесс загрузки новых аккаунтов со всех добавленных в бота MCC! Все аккаунты, которых ещё нет в базе данных бота, будут добавлены в соответствующий MCC.

    ❗ <b>Нажмите только один раз, это ресурсозатратный процесс</b>
ADMIN-SPECIFIC-LOAD-CONFIRMATION = ✅ Подтвердить загрузку
ADMIN-SPECIFIC-LOAD-PROCESSING = ⏳ Загрузка началась, это займет около 1-2 минут
ADMIN-SPECIFIC-LOAD-RESULT = ✅ Успешно загружено новых аккаунтов: <b>{$new_accounts}</b> 📊

    {$statistic}
ADMIN-SPECIFIC-LOAD-FAIL = ❌ Ошибка добавления аккаунта <b>{$email}</b> в MCC <b>{$mcc_name}</b>
