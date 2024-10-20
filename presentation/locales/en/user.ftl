#################################### General ################################################
NONAME-NO_ACCESS = У вас відсутній доступ, попросіть у адміністраторів

REGISTER-SUCCESS = Зареєстровано успішно
REGISTER-FAIL = Помилка реєстрації

MENU = Меню
BACK = Назад

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = Ключа не існує!
JOIN_KEY-ACTIVATED_BEFORE = Ключ був активований раніше до вас!
JOIN_KEY-FAIL_UPDATE = Якась помилка. Ключ команди не встановлено
JOIN_KEY-SUCCESS_UPDATE = Ключ команди встановлено успішно!


#################################### Accounts #################################################
CLIENT-ACCOUNTS = Акаунти
CLIENT-ACCOUNTS-DETAIL = Акаунт: <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    Пошта: <code>{$email}</code>
    Тайм-зона: <b>{$timezone}</b>
    Ідентифікатор клієнта: <code>{$customer_id}</code>

    Баланс: <b>{$balance}$</b>
    Спенд: <b>{$spend}$</b>
    Ліміт: <b>{$limit}$</b>

########################## MCC ###################################################
CLIENT-MCC = Оберіть MCC для управління акаунтами
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Доступно акаунтів: <b>{$account_available}</b>
    Баланс: {$balance}$
CLIENT-MCC-BALANCE-ADD = Поповнити баланс
CLIENT-MCC-BALANCE-VALUE = Сума поповнення від <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = Потрібно ввести число від <b>100$</b> до <b>10.000$</b>:
CLIENT-MCC-BALANCE-SUCCESS = Запит на поповнення надіслано
CLIENT-MCC-BALANCE-FAIL = Невдалося надіслати запит
##############################################################################
# Account (change email, refund, topup)
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = Змінити email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Вкажіть новий email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = Не вийшло змінити email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = Формат Email не дійсний
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = Email успішно змінено на <b>{$email}</b>
# Refond ###
CLIENT-ACCOUNT-REFUND = Рефаунд
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Ви точно хочете зробити рефаунд акаунту <b>{$account_name}</b> ?

    Баланс акаунту (<b>{$balance}$</b>) буде повернено на головний MCC
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Підтвердити рефаунд
CLIENT-ACCOUNT-REFUND-FAIL = Виникла помилка. Не вийшло зробити рефаунд
CLIENT-ACCOUNT-REFUND-SUCCESS = Запит на рефаунд відправлено успішно
# TopUp ###
CLIENT-ACCOUNT-TOPUP = Поповнити
CLIENT-ACCOUNT-TOPUP-VALUE = Введіть суму поповнення від <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = Потрібно ввести число від <b>100$</b> до <b>10.000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Поповнити баланс акаунту на <b>{$value}$</b> ?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = Недостатній баланс на акаунті.
    Ваш баланс: <b>{$balance}$</b>
    Запит на поповнення: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Підтвердити поповнення
CLIENT-ACCOUNT-TOPUP-FAIL = Помилка при поповненні
CLIENT-ACCOUNT-TOPUP-SUCCESS = Успішно поповненно
###########################################################################################
CLIENT-ACCOUNT-CREATE = Створити акаунт
CLIENT-ACCOUNT-CREATE-LIMIT = У вас вичерпано ліміт створення акаунтів на цей MCC
CLIENT-ACCOUNT-CREATE-NAME = Вкажіть назву:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = Назва має бути до 255 симолів, зараз <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Вкажіть email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Сума поповнення (мін 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = Сума на балансі не достатня для поповнення кабу (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Вкажіть тайм-зону, UTC(від -12 до +14), введіть число, наприклад +12 або -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = Невірний формат. UTC(від -12 до +14), введіть число, наприклад +12 або -3:
CLIENT-ACCOUNT-CREATE-FAIL = Помилка при створенні акаунту
CLIENT-ACCOUNT-CREATE-SUCCESS = Акаунт успішно створено! Чекай поки він з'явиться у тебе в акаунтах до вказаного MCC (<b>{$mcc_name}</b>)
##############
CLIENT-ACCOUNT-NO_VERIFY_YET = Акаунт ще не верифіковано, зайдіть пізніше ⏱️

