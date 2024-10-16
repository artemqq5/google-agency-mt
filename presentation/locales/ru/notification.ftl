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

NOTIFICATION-TOPUP-ACCOUNT = 💳 Внутрішнє поповнення <b>{$account_name}</b> на <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Залишковий баланс: <b>{$balance}</b>
    Команда: <b>{$team_name}</b>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-REFAUND-ACCOUNT = 🔖 Рефаунд акаунта <b>{$account_name}</b> з балансом <b>{$balance}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Команда: <b>{$team_name}</b>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 Баланс для MCC (<b>{$mcc_name}</b>) був щойно поповнений на <b>{$value}$</b> !

########################################################################
########################################################################
########################################################################
#################### ERROR #############################################
NOTIFICATION-CHANGE-EMAIL-ERROR = 📨❌ (НЕ ВДАЛОСЯ) Пошту на акаунті <b>{$account_name}</b> НЕ БУЛО ЗМІНЕНО на <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    <b>База оновилась, але API запит не вдався!!!</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Команда: <b>{$team_name}</b>
    Команда UUID: <code>{$team_uuid}</code>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT-ERROR = 💳❌ (НЕ ВДАЛОСЯ) Внутрішнє поповнення <b>{$account_name}</b> на <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    MCC UUID: <b>{$mcc_uuid}</b>

    Залишковий баланс: <b>{$balance}</b>
    Баланс UUID: <b>{$balance_uuid}</b>

    Команда: <b>{$team_name}</b>
    Команда UUID: <b>{$team_uuid}</b>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>

NOTIFICATION-REFAUND-ACCOUNT-ERROR = 🔖❌ (НЕ ВДАЛОСЯ) Рефаунда акаунта <b>{$account_name}</b> з балансом <b>{$balance}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    MCC UUID: <b>{$mcc_uuid}</b>

    Баланс UUID: <b>{$balance_uuid}</b>

    Команда: <b>{$team_name}</b>
    Команда UUID: <b>{$team_uuid}</b>

    Нікнейм: <b>@{$username}</b>
    Телеграм ID: <code>{$user_id}</code>
