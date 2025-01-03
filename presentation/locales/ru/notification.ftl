NOTIFICATION-NEW_USER = 👤 <b>Новый пользователь подключился к боту!</b>
    ━━━━━━━━━━━━━━━━
    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Присоединился: <b>{$join_at}</b>

NOTIFICATION-CREATE_TRANSACTION = 💵 <b>Новый запрос на пополнение</b>
    ━━━━━━━━━━━━━━━━
    Хэш транзакции: <code>{$hash}</code>

    MCC для пополнения: <b>{$mcc_name}</b>
    КОШЕЛЕК: <code>{$wallet}</code>
    Сумма к пополнению: <b>{$value}$</b>

    Команда: <b>{$team_name}</b>
    Баланс команды в этом MCC: <b>{$balance_team_value}$</b>
    Идентификатор команды: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CHANGE-EMAIL = 📨 Email аккаунта <b>{$account_email}</b> был изменен на <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT = 💳 Внутреннее пополнение <b>{$account_email}</b> на сумму <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Остаток баланса: <b>{$balance}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT = 🔖 Возврат средств аккаунта <b>{$account_email}</b> с балансом <b>{$balance}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT = ❇️ Создан аккаунт <b>{$account_email}</b> с балансом <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>
    Лимит: <b>{$limit}</b>
    Остаток баланса: <b>{$balance}</b>

    Email: <code>{$email}</code>
    Часовой пояс: <b>{$timezone}</b>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 Баланс для MCC (<b>{$mcc_name}</b>) был только что пополнен на сумму <b>{$value}$</b> !

#################### ERROR #############################################
NOTIFICATION-CHANGE-EMAIL-ERROR = 📨❌ (НЕ УДАЛОСЬ) Email аккаунта <b>{$account_email}</b> НЕ был изменен на <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    <b>База обновлена, но API запрос завершился неудачно!!!</b>

    MCC: <b>{$mcc_name}</b>
    UUID MCC: <code>{$mcc_uuid}</code>

    Команда: <b>{$team_name}</b>
    UUID команды: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT-ERROR = 💳❌ (НЕ УДАЛОСЬ) Внутреннее пополнение <b>{$account_email}</b> на сумму <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    UUID MCC: <code>{$mcc_uuid}</code>

    Остаток баланса: <b>{$balance}</b>
    UUID баланса: <code>{$balance_uuid}</code>

    Команда: <b>{$team_name}</b>
    UUID команды: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT-ERROR = 🔖❌ (НЕ УДАЛОСЬ) Возврат средств аккаунта <b>{$account_email}</b> с балансом <b>{$balance}$</b> !
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    UUID MCC: <code>{$mcc_uuid}</code>

    UUID баланса: <code>{$balance_uuid}</code>

    Команда: <b>{$team_name}</b>
    UUID команды: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT-ERROR = ❇️❌ (НЕ УДАЛОСЬ) Аккаунт <b>{$account_email}</b> НЕ был создан с балансом <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    Ошибка: <b>{$error}</b>

    MCC: <b>{$mcc_name}</b>
    UUID MCC: <code>{$mcc_uuid}</code>

    Команда: <b>{$team_name}</b>
    UUID команды: <code>{$team_uuid}</code>

    Email: <code>{$email}</code>

    Лимит: <b>{$limit}</b>
    Баланс: <b>{$balance}</b>

    Никнейм: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TEAM-COMMISSIONS_REPORT = Отчет по комиссиям 💸
    Транзакций с комиссиями: {$taxes_count}
    Общая сумма: <b>{$taxes_amount} USD</b>

    Детальную информацию можно посмотреть в разделе "Комиссионные транзакции"
