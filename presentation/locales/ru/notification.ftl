NOTIFICATION-NEW_USER = 👤 <b>Новый пользователь присоединился к боту!</b>
    ━━━━━━━━━━━━━━━━
    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Присоединился: <b>{$join_at}</b>

NOTIFICATION-CREATE_TRANSACTION = 💵 <b>Новый запрос на пополнение</b>
    ━━━━━━━━━━━━━━━━
    Хеш транзакции: <code>{$hash}</code>

    MCC для пополнения: <b>{$mcc_name}</b>
    WALLET: <code>{$wallet}</code>
    Сумма для пополнения: <b>{$value}$</b>

    Команда: <b>{$team_name}</b>
    Баланс команды на этом MCC: <b>{$balance_team_value}$</b>
    Идентификатор команды: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CHANGE-EMAIL = 📨 Email на аккаунте <b>{$account_email}</b> был изменен на <b>{$email}</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT = 💳 Внутреннее пополнение <b>{$account_email}</b> на сумму <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Оставшийся баланс: <b>{$balance}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT = 🔖 Рефаунд аккаунта <b>{$account_email}</b> с балансом <b>{$balance}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT = ❇️ Аккаунт <b>{$account_email}</b> был создан с балансом <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>
    Лимит: <b>{$limit}</b>
    Оставшийся баланс: <b>{$balance}</b>

    Почта: <code>{$email}</code>
    Часовой пояс: <b>{$timezone}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 Баланс для MCC (<b>{$mcc_name}</b>) был только что пополнен на <b>{$value}$</b>!

#################### ERROR #############################################
NOTIFICATION-CHANGE-EMAIL-ERROR = 📨❌ (НЕ УДАЛОСЬ) Email на аккаунте <b>{$account_email}</b> НЕ был изменен на <b>{$email}</b>!
    ━━━━━━━━━━━━━━━━
    <b>База данных обновилась, но запрос API не удался!!!</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT-ERROR = 💳❌ (НЕ УДАЛОСЬ) Внутреннее пополнение <b>{$account_email}</b> на сумму <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Оставшийся баланс: <b>{$balance}</b>
    Баланс UUID: <code>{$balance_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT-ERROR = 🔖❌ (НЕ УДАЛОСЬ) Рефаунд аккаунта <b>{$account_email}</b> с балансом <b>{$balance}$</b>!
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Баланс UUID: <code>{$balance_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT-ERROR = ❇️❌ (НЕ УДАЛОСЬ) Аккаунт <b>{$account_email}</b> не был создан с балансом <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    Ошибка: <b>{$error}</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Почта: <code>{$email}</code>

    Лимит: <b>{$limit}</b>
    Баланс: <b>{$balance}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
