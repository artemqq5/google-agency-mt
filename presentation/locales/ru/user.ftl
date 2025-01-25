#################################### General ################################################
NONAME-NO_ACCESS = 🛑 У вас нет доступа, обратитесь к администраторам

REGISTER-SUCCESS = Добро пожаловать! 👋 Вы присоединились к MT Agency - сервису, созданному командой Masons Traffic специально для работы с агентскими аккаунтами Google
REGISTER-FAIL = ❌ Ошибка регистрации

MENU = 📋 Меню
BACK = 🔙 Назад

CLIENT-ACCOUNT-NOT_EXIST = Аккаунт не существует

FAQ = ℹ️ FAQ
OPEN = Открыть
FAQ_MESSAGE = Инструкция по работе с агентскими аккаунтами MT Agency Google

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = ❗ Ключ не существует!
JOIN_KEY-ACTIVATED_BEFORE = 🔑 Ключ ранее был активирован другим пользователем!
JOIN_KEY-FAIL_UPDATE = ⚠️ Произошла ошибка. Ключ команды не установлен
JOIN_KEY-SUCCESS_UPDATE = 🔓 Ключ команды успешно установлен!

#################################### Accounts #################################################
CLIENT-ACCOUNTS = 👥 Аккаунты
CLIENT-ACCOUNTS-DETAIL = Аккаунт: <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Статус: <b>{$status}</b>

    Email: <code>{$email}</code>
    Часовой пояс: <b>{$timezone}</b>
    ID клиента: <code>{$customer_id}</code>

    Баланс: <b>{$balance}$</b>
    Расходы: <b>{$spend}$</b>
    Лимит: <b>{$limit}$</b>

########################## MCC ###################################################
CLIENT-MCC = 🏦 Выберите MCC для управления аккаунтами
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Доступно аккаунтов: <b>{$account_available}</b>
    Баланс: {$balance}$

CLIENT-MCC-BALANCE-ADD = 💰 Пополнить баланс
CLIENT-MCC-BALANCE-VALUE = Сумма пополнения от <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = ❗ Необходимо ввести число от <b>100$</b> до <b>10,000$</b>:
CLIENT-MCC-BALANCE-HASH-SEND = 📄❗ <b>Отправьте хэш транзакции</b>:
CLIENT-MCC-BALANCE-HASH =  📄 Пополните баланс на <b>{$sum}$</b>:

    ❗При пополнении на сумму меньше указанной, оплата не будет произведена автоматически❗

    <b>Кошельки для пополнения</b>

    📌 <code>TR5zws4EYZtrExwLc6EDGgdMfZ958EhVSm</code>
      USDT TRC20

    📌 <code>0x5129f986ef3751480aecaa9ddade59fbc48230fe</code>
      USDT ERC20

CLIENT-MCC-BALANCE-SUCCESS = ✅ Запрос на пополнение отправлен успешно
CLIENT-MCC-BALANCE-FAIL = ❌ Ошибка при отправке запроса

########################## Account (change email, refund, top-up) ###########################
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = ✉️ Изменить email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Укажите новый email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Ошибка при изменении email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Неверный формат Email
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email успешно изменен на <b>{$email}</b>

# Refund ###
CLIENT-ACCOUNT-REFUND = 💸 Возврат средств
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Вы уверены, что хотите вернуть средства с аккаунта <b>{$account_name}</b>?

    Баланс аккаунта <b>{$balance}$</b> будет возвращен на основной MCC
    ВНИМАНИЕ! Комиссия 4% = <b>{$commission}$</b>
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Подтвердить возврат средств
CLIENT-ACCOUNT-REFUND-FAIL = ❌ Ошибка. Возврат средств не выполнен
CLIENT-ACCOUNT-REFUND-SUCCESS = ✅ Запрос на возврат средств отправлен успешно

# TopUp ###
CLIENT-ACCOUNT-TOPUP = 💰 Пополнить
CLIENT-ACCOUNT-TOPUP-VALUE = Введите сумму пополнения от <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = ❗ Необходимо ввести число от <b>100$</b> до <b>10,000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Пополнить баланс аккаунта на <b>{$value}$</b>?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Недостаточный баланс.
    Ваш баланс: <b>{$balance}$</b>
    Запрос на пополнение: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Подтвердить пополнение
CLIENT-ACCOUNT-TOPUP-FAIL = ❌ Ошибка при пополнении
CLIENT-ACCOUNT-TOPUP-SUCCESS = ✅ Успешно пополнено

CLIENT-ACCOUNT-CREATE = 🆕 Создать аккаунт
CLIENT-ACCOUNT-CREATE-LIMIT = ❗ Лимит создания аккаунтов для данного MCC исчерпан
CLIENT-ACCOUNT-CREATE-NAME = Укажите название:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = ❗ Название должно быть до 255 символов, сейчас <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Укажите email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Сумма пополнения (мин 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = ❗ Недостаточно средств для пополнения аккаунта (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Укажите часовой пояс, UTC(от -12 до +14), введите число, например +12 или -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = ❗ Неверный формат. UTC(от -12 до +14), введите число, например +12 или -3:
CLIENT-ACCOUNT-CREATE-FAIL = ❌ Ошибка при создании аккаунта
CLIENT-ACCOUNT-CREATE-SUCCESS = ✅ Аккаунт успешно создан! Ожидайте, пока он появится в вашем списке аккаунтов в указанном MCC (<b>{$mcc_name}</b>)

CLIENT-ACCOUNT-NO_VERIFY_YET = ⏱️ Аккаунт еще не подтвержден, зайдите позже ⏱️
########################## TAX
CLIENT-TAXES = 🚕 Комиссии
CLIENT-TRANSACTIONS-TAX-DETAIL = ℹ️ <b>Транзакция комиссии #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b> ({$client_link})

    💵 Сумма комиссии: <b>{$amount} {$currency}</b>
    📅 Дата: <b>{$date}</b>

    📧 Email: <code>{$email}</code>

    📝 <b>{$desc}</b>

    🆔 Идентификатор транзакции: <code>{$uuid_transaction}</code>

CLIENT-WAIT_FOR_REQUEST = Подождите несколько секунд перед запросом!
#########################################
CLIENT-REFUND = 🔙 История рефаундов
CLIENT-REFUND-DETAIL = Рефаунд аккаунта <b>{$account_email}</b> 💰
    ━━━━━━━━━━━━━━━━
    Имя аккаунта: <b>{$account_name}</b>
    Сумма рефаунда: <b>{$refund_value}</b> 💰
    Комиссия: <b>{$commission}</b> 💳
    Спенд: <b>{$last_spend}</b>
    Таймзона: <b>{$account_timezone}</b> ⏰
    MCC: <b>{$mcc_name}</b>

    Статус рефаунда: <b>{$status}</b> ✔️
    Создание запроса на рефаунд: <b>{$created}</b> 🕒
    Подтверждение рефаунда: <b>{$completed_time}</b> 🕒
