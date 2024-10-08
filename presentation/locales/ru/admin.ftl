# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = Команди
ADMIN-MCC = MCC
ADMIN-MESSAGING = Розсилка
ADMIN-PROFILE = Профіль

# TEAMS ################################################################################
TEAMS-CREATE = Створити нову команду
TEAMS-CREATE-NAME = Назва для команди:
TEAMS-CREATE-LIMIT = Ліміт MCC для команди:
TEAMS-CREATE-SUCCESS = Команду <b>{$team}</b> успішно створено ✅
TEAMS-CREATE-FAIL = Помилка при створені команди (<b>{$error}</b>) ❌
#################
TEAMS-CREATE-NAME_ERROR = Довга назва (<b>{$symballs}</b>) символів, вкладись в 50
TEAMS-CREATE-LIMIT_ERROR = Потрібно ввести число від 0 до 999:
################################################################################
TEAMS-DETAIL = ID: {$team_id}
    Team: <b>{$team_name}</b>
    Users: <b>{$count_users}</b>
    MCC Limit: <b>{$mcc_limit}</b>
    Created: <b>{$created}</b>

    Загальна сума з усіх транзакцій: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = Доступи команди
TEAMS-ACCESS-CREATE = Створити доступ
TEAMS-ACCESS-CREATE-CONFIRMANTION = Бажаєте створити одноразовий доступ до команди <b>{$team}</b> ?
TEAMS-ACCESS-CREATE-SUCCESS = Доступ для (<b>{$team}</b>) успішно створено ✅

    <code>{$deeplink}</code>
TEAMS-ACCESS-CREATE-FAIL = Помилка при створені доступу для (<b>{$team}</b>) ❌
################################################################################
TEAMS-ACCESS-DETAIL = Команда: <b>{$team}</b>

    DeepLink: <code>{$deeplink}</code>

    User ID: <code>{$user_id}</code>
    UserName: @{$username}
    Ім'я: {$firstname}
    Прізвище: {$lastname}

    Доступ створено: <b>{$created}</b>
    Доступ активовано: <b>{$activated}</b>
##################################################################################
TEAMS-ACCESS-DELETE = Видалити доступ
TEAMS-ACCESS-DELETE-WARNING = При видаленні доступу користувач втратить свій функціонал

    <b>Точно видалити доступ?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = Підтвердити видалення
TEAMS-ACCESS-DELETE-SUCCESS = Доступ видалено
TEAMS-ACCESS-DELETE-FAIL = Не вдалося видалити доступ
#################################################################################
TEAMS-DELETE = Видалити команду
TEAMS-DELETE-WARNING = Ви точно бажаєте видалити команду (<b>{$team}</b>)?

    Повернути рішення буде не можливо!
TEAMS-DELETE-CONFIRMATION = Підтвердити видалення команди
TEAMS-DELETE-SUCCESS = Команду успішно видалено
TEAMS-DELETE-FAIL = Не вдалося видалити команду
####################################################################################
TEAMS-MCC-LIMIT = редагувати MMC ліміт
TEAMS-MCC-LIMIT-VALUE = Введіть кількість MCC для (<b>{$team}</b>):
TEAMS-MCC-LIMIT-VALUE_ERROR = Потрібно ввести число від 0 до 999:
TEAMS-MCC-LIMIT-VALUE_DUBL = Наразі цей ліміт <b>{$limit}</b> вже встановлено, напишіть новий або скасуйте операцію:
TEAMS-MCC-LIMIT-SUCCESS = Ліміт успішно змінено на <b>{$limit}</b>
TEAMS-MCC-LIMIT-FAIL = Не вийшло змінити ліміт
###############################################
TEAMS-MCC-ACCESS = MCC Розшарені для команди <b>{$team_name}</b>
TEAMS-MCC-SHARE = Розшарити
TEAMS-MCC-SHARE-CHOICE = Оберіть котрий MCC бажаєте розшарити для команди <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = Невдалося розшарити MCC для <b>{$team_name}</b> ❌
TEAMS-MCC-SHARE-SUCCESS = MCC (<b>{$mcc_name}</b>) Успішно розшарено для <b>{$team_name}</b>
TEAMS-MCC-RESHARE = Прибрати доступ
TEAMS-MCC-RESHARE-CONFIRMATION = Точно прибрати доступ MCC (<b>{$mcc_name}</b>) для команди <b>{$team_name}</b> ?
TEAMS-MCC-RESHARE-SUCCESS = Доступ прибрано
TEAMS-MCC-RESHARE-FAIL = Невдалося прибрати доступ
########## MCC ############################################################################
MCC-AUTH-FAIL = Помилка авторизації MCC <b>{$mcc_name}</b> ❌
###############################################################
MCC-ADD = Додати новий MCC
MCC-ADD-NAME = Введіть ім'я для нового MCC:
MCC-ADD-ID = Введіть ID для нового MCC:
MCC-ADD-SECRET_TOKEN = Введіть Secret Token для нового MCC:
##########################################################
MCC-ADD-NAME_ERROR = Довга назва (<b>{$symballs}</b>) символів, вкладись в 50
MCC-ADD-SUCCESS = MCC <b>{$mcc_name}</b> успішно додано ✅
MCC-ADD-FAIL = Помилка при додаванні MCC (<b>{$error}</b>) ❌
###########################
MCC-DETAIL = <b>{$name}</b>
    Баланс: {$balance}$
##############################################################
ACCOUNTS-DETAIL = <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    Пошта: <code>{$email}</code>
    Тайм-зона: <b>{$timezone}</b>
    Ідентифікатор клієнта: <code>{$customer_id}</code>

    Баланс: <b>{$balance}$</b>
    Спенд: <b>{$spend}$</b>
    Ліміт: <b>{$limit}$</b>

    Команда: <b>{$team_name}</b>
