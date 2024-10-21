NOTIFICATION-NEW_USER = 👤 <b>Новый пользователь присоединился к боту!</b>
    ━━━━━━━━━━━━━━━━
    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Присоединился: <b>{$join_at}</b>

NOTIFICATION-CREATE_TRANSACTION = 💵 <b>Новый запрос на пополнение</b>
    ━━━━━━━━━━━━━━━━
    MCC для пополнения: <b>{$mcc_name}</b>
    Сумма для пополнения: <b>{$value}$</b>

    Команда: <b>{$team_name}</b>
    Баланс команды на этом MCC: <b>{$balance_team_value}$</b>
    Идентификатор команды: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CHANGE-EMAIL = 📨 Почта аккаунта <b>{$account_name}</b> была изменена на <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT = 💳 Внутреннее пополнение <b>{$account_name}</b> на <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Остаток баланса: <b>{$balance}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT = 🔖 Возврат аккаунта <b>{$account_name}</b> с балансом <b>{$balance}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT = ❇️ Создан аккаунт <b>{$account_name}</b> с балансом <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>
    Лимит: <b>{$limit}</b>
    Остаток на балансе: <b>{$balance}</b>

    Почта: <code>{$email}</code>
    Часовой пояс: <b>{$timezone}</b>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 Баланс для MCC (<b>{$mcc_name}</b>) был только что пополнен на <b>{$value}$</b> !

#################### ERROR #############################################
NOTIFICATION-CHANGE-EMAIL-ERROR = 📨❌ (НЕ УДАЛОСЬ) Почта аккаунта <b>{$account_name}</b> НЕ БЫЛА ИЗМЕНЕНА на <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    <b>База обновилась, но API запрос не удался!!!</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT-ERROR = 💳❌ (НЕ УДАЛОСЬ) Внутреннее пополнение <b>{$account_name}</b> на <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Остаток баланса: <b>{$balance}</b>
    Баланс UUID: <code>{$balance_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT-ERROR = 🔖❌ (НЕ УДАЛОСЬ) Возврат аккаунта <b>{$account_name}</b> с балансом <b>{$balance}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Баланс UUID: <code>{$balance_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Никнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT-ERROR = ❇️❌ (НЕ УДАЛОСЬ) Создан аккаунт <b>{$account_name}</b> с балансом <b>{$amount}$</b> !
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
