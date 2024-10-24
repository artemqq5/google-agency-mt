#################################### General ################################################
NONAME-NO_ACCESS = 🛑 У вас нет доступа, обратитесь к администраторам

REGISTER-SUCCESS = ✅ Регистрация успешна!
REGISTER-FAIL = ❌ Ошибка регистрации

MENU = 📋 Меню
BACK = 🔙 Назад

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = ❗ Ключ не существует!
JOIN_KEY-ACTIVATED_BEFORE = 🔑 Ключ был активирован до вас!
JOIN_KEY-FAIL_UPDATE = ⚠️ Что-то пошло не так. Ключ команды не установлен
JOIN_KEY-SUCCESS_UPDATE = 🔓 Ключ команды успешно установлен!

#################################### Accounts #################################################
CLIENT-ACCOUNTS = 👥 Аккаунты
CLIENT-ACCOUNTS-DETAIL = Аккаунт: <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    Почта: <code>{$email}</code>
    Часовой пояс: <b>{$timezone}</b>
    Идентификатор клиента: <code>{$customer_id}</code>

    Баланс: <b>{$balance}$</b>
    Траты: <b>{$spend}$</b>
    Лимит: <b>{$limit}$</b>

########################## MCC ###################################################
CLIENT-MCC = 🏦 Выберите MCC для управления аккаунтами
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Доступно аккаунтов: <b>{$account_available}</b>
    Баланс: {$balance}$

CLIENT-MCC-BALANCE-ADD = 💰 Пополнить баланс
CLIENT-MCC-BALANCE-VALUE = Сумма пополнения от <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = ❗ Введите сумму от <b>100$</b> до <b>10,000$</b>:
CLIENT-MCC-BALANCE-HASH = 📄 Пополните баланс на указанную сумму и <b>отправьте хеш транзакции</b>:

    <b>Кошельки для пополнения</b>

    📌 <code>TR5zws4EYZtrExwLc6EDGgdMfZ958EhVSm</code>
      USDT TRC20

    📌 <code>0x5129f986ef3751480aecaa9ddade59fbc48230fe</code>
      USDT ERC20

CLIENT-MCC-BALANCE-SUCCESS = ✅ Запрос на пополнение успешно отправлен
CLIENT-MCC-BALANCE-FAIL = ❌ Не удалось отправить запрос на пополнение

########################## Account (change email, refund, topup) ###########################
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = ✉️ Изменить email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Введите новый email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Не удалось изменить email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Неверный формат email
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email успешно изменён на <b>{$email}</b>

# Refund ###
CLIENT-ACCOUNT-REFUND = 💸 Рефаунд
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Вы уверены, что хотите сделать рефаунд аккаунта <b>{$account_name}</b>?

    Баланс аккаунта (<b>{$balance}$</b>) будет возвращён на главный MCC
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Подтвердить рефаунд
CLIENT-ACCOUNT-REFUND-FAIL = ❌ Произошла ошибка. Не удалось сделать рефаунд
CLIENT-ACCOUNT-REFUND-SUCCESS = ✅ Запрос на рефаунд успешно отправлен

# TopUp ###
CLIENT-ACCOUNT-TOPUP = 💰 Пополнить
CLIENT-ACCOUNT-TOPUP-VALUE = Введите сумму пополнения от <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = ❗ Введите сумму от <b>100$</b> до <b>10,000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Пополнить баланс аккаунта на <b>{$value}$</b>?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Недостаточный баланс на аккаунте.
    Ваш баланс: <b>{$balance}$</b>
    Запрошенное пополнение: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Подтвердить пополнение
CLIENT-ACCOUNT-TOPUP-FAIL = ❌ Ошибка пополнения
CLIENT-ACCOUNT-TOPUP-SUCCESS = ✅ Успешно пополнено

CLIENT-ACCOUNT-CREATE = 🆕 Создать аккаунт
CLIENT-ACCOUNT-CREATE-LIMIT = ❗ Вы исчерпали лимит создания аккаунтов на этот MCC
CLIENT-ACCOUNT-CREATE-NAME = Введите название аккаунта:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = ❗ Название должно быть до 255 символов, сейчас <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Введите email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Сумма пополнения (мин 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = ❗ Баланс недостаточен для пополнения аккаунта (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Введите часовой пояс, UTC (от -12 до +14), введите число, например +12 или -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = ❗ Неверный формат. UTC (от -12 до +14), введите число, например +12 или -3:
CLIENT-ACCOUNT-CREATE-FAIL = ❌ Ошибка создания аккаунта
CLIENT-ACCOUNT-CREATE-SUCCESS = ✅ Аккаунт успешно создан! Ожидайте его появления в вашем MCC (<b>{$mcc_name}</b>)

CLIENT-ACCOUNT-NO_VERIFY_YET = ⏱️ Аккаунт еще не верифицирован, попробуйте позже ⏱️
