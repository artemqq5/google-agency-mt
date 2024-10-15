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
# Account (change email, refound, topup)
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = Змінити email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Вкажіть новий email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = Не вийшло змінити email
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = Email успішно змінено на <b>{$email}</b>
# Refound ###
CLIENT-ACCOUNT-REFOUND = Рефаунд
CLIENT-ACCOUNT-REFOUND-CONFIRMATION-WARNING = Ви точно хочете зробити рефаунд акаунту <b>{$account_name}<\b> ?

    Баланс акаунту (<b>{$balance}$</b>) буде повернено на головний MCC
CLIENT-ACCOUNT-REFOUND-CONFIRMATION = Підтвердити рефаунд
CLIENT-ACCOUNT-REFOUND-FAIL = Виникла помилка. Не вийшло зробити рефаунд
CLIENT-ACCOUNT-REFOUND-SUICCESS = Запит на рефаунд відправлено успішно
# TopUp ###
CLIENT-ACCOUNT-TOPUP = Поповнити
CLIENT-ACCOUNT-TOPUP-VALUE = Введіть суму поповнення від <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = Потрібно ввести число від <b>100$</b> до <b>10.000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Поповнити баланс акаунту на <b>{$value}$</b> ?
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Підтвердити поповнення
CLIENT-ACCOUNT-TOPUP-FAIL = Помилка при поповненні
CLIENT-ACCOUNT-TOPUP-SUCCESS = Успішно поповненно



