NOTIFICATION-NEW_USER = 👤 <b>Новий користувач доєднався до боту!</b>
    ━━━━━━━━━━━━━━━━
    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
    Приєднався: <b>{$join_at}</b>

NOTIFICATION-CREATE_TRANSACTION = 💵 <b>Новий запит на поповнення</b>
    ━━━━━━━━━━━━━━━━
    MCC для поповнення: <b>{$mcc_name}</b>
    Сума до поповнення: <b>{$value}$</b>

    Команда: <b>{$team_name}</b>
    Баланс у команди на цьому MCC: <b>{$balance_team_value}$</b>
    Ідкнтифікатор команди: <code>{$team_uuid}</code>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CHANGE-EMAIL = 📨 Пошту на акаунті <b>{$account_name}</b> було змінено на <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 Баланс для MCC (<b>{$mcc_name}</b>) був щойно поповнений на <b>{$value}$</b> !
