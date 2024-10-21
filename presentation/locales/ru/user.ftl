#################################### General ################################################
NONAME-NO_ACCESS = 🛑 У вас нет доступа, попросите у администраторов

REGISTER-SUCCESS = ✅ Успешно зарегистрировано!
REGISTER-FAIL = ❌ Ошибка регистрации

MENU = 📋 Меню
BACK = 🔙 Назад

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = ❗ Ключа не существует!
JOIN_KEY-ACTIVATED_BEFORE = 🔑 Ключ был активирован ранее до вас!
JOIN_KEY-FAIL_UPDATE = ⚠️ Какая-то ошибка. Ключ команды не установлен
JOIN_KEY-SUCCESS_UPDATE = 🔓 Ключ команды успешно установлен!

#################################### Accounts #################################################
CLIENT-ACCOUNTS = 👥 Аккаунты
CLIENT-ACCOUNTS-DETAIL = Аккаунт: <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    Почта: <code>{$email}</code>
    Тайм-зона: <b>{$timezone}</b>
    Идентификатор клиента: <code>{$customer_id}</code>

    Баланс: <b>{$balance}$</b>
    Спенд: <b>{$spend}$</b>
    Лимит: <b>{$limit}$</b>

########################## MCC ###################################################
CLIENT-MCC = 🏦 Выберите MCC для управления аккаунтами
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Доступно аккаунтов: <b>{$account_available}</b>
    Баланс: {$balance}$

CLIENT-MCC-BALANCE-ADD = 💰 Пополнить баланс
CLIENT-MCC-BALANCE-VALUE = Сумма пополнения от <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = ❗ Нужно ввести число от <b>100$</b> до <b>10.000$</b>:
CLIENT-MCC-BALANCE-SUCCESS = ✅ Запрос на пополнение отправлен
CLIENT-MCC-BALANCE-FAIL = ❌ Не удалось отправить запрос

########################## Account (change email, refund, topup) ###########################
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = ✉️ Изменить email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Укажите новый email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Не удалось изменить email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Неверный формат Email
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email успешно изменён на <b>{$email}</b>

# Refund ###
CLIENT-ACCOUNT-REFUND = 💸 Рефаунд
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Вы точно хотите сделать рефаунд аккаунта <b>{$account_name}</b>?

    Баланс аккаунта (<b>{$balance}$</b>) будет возвращён на главный MCC
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Подтвердить рефаунд
CLIENT-ACCOUNT-REFUND-FAIL = ❌ Возникла ошибка. Не удалось сделать рефаунд
CLIENT-ACCOUNT-REFUND-SUCCESS = ✅ Запрос на рефаунд успешно отправлен

# TopUp ###
CLIENT-ACCOUNT-TOPUP = 💰 Пополнить
CLIENT-ACCOUNT-TOPUP-VALUE = Введите сумму пополнения от <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = ❗ Нужно ввести число от <b>100$</b> до <b>10.000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Пополнить баланс аккаунта на <b>{$value}$</b>?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Недостаточный баланс на аккаунте.
    Ваш баланс: <b>{$balance}$</b>
    Запрос на пополнение: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Подтвердить пополнение
CLIENT-ACCOUNT-TOPUP-FAIL = ❌ Ошибка при пополнении
CLIENT-ACCOUNT-TOPUP-SUCCESS = ✅ Успешно пополнено

CLIENT-ACCOUNT-CREATE = 🆕 Создать аккаунт
CLIENT-ACCOUNT-CREATE-LIMIT = ❗ У вас исчерпан лимит создания аккаунтов для этого MCC
CLIENT-ACCOUNT-CREATE-NAME = Укажите название:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = ❗ Название должно быть до 255 символов, сейчас <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Укажите email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Сумма пополнения (мин 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = ❗ Недостаточно средств для пополнения аккаунта (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Укажите тайм-зону, UTC(от -12 до +14), введите число, например +12 или -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = ❗ Неверный формат. UTC(от -12 до +14), введите число, например +12 или -3:
CLIENT-ACCOUNT-CREATE-FAIL = ❌ Ошибка при создании аккаунта
CLIENT-ACCOUNT-CREATE-SUCCESS = ✅ Аккаунт успешно создан! Ожидайте его появления в аккаунтах MCC (<b>{$mcc_name}</b>)

CLIENT-ACCOUNT-NO_VERIFY_YET = ⏱️ Аккаунт ещё не верифицирован, зайдите позже ⏱️
