NOTIFICATION-NEW_USER = 👤 <b>New user joined the bot!</b>
    ━━━━━━━━━━━━━━━━
    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Joined: <b>{$join_at}</b>

NOTIFICATION-CREATE_TRANSACTION = 💵 <b>New top-up request</b>
    ━━━━━━━━━━━━━━━━
    Transaction hash: <code>{$hash}</code>

    MCC for top-up: <b>{$mcc_name}</b>
    Amount to top-up: <b>{$value}$</b>

    Team: <b>{$team_name}</b>
    Team balance on this MCC: <b>{$balance_team_value}$</b>
    Team ID: <code>{$team_uuid}</code>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CHANGE-EMAIL = 📨 The email on account <b>{$account_name}</b> was changed to <b>{$email}</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Team: <b>{$team_name}</b>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT = 💳 Internal top-up of <b>{$account_name}</b> for <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Remaining balance: <b>{$balance}</b>
    Team: <b>{$team_name}</b>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT = 🔖 Refund for account <b>{$account_name}</b> with balance <b>{$balance}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Team: <b>{$team_name}</b>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT = ❇️ Account <b>{$account_name}</b> was created with a balance of <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Team: <b>{$team_name}</b>
    Limit: <b>{$limit}</b>
    Remaining balance: <b>{$balance}</b>

    Email: <code>{$email}</code>
    Time zone: <b>{$timezone}</b>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 Balance for MCC (<b>{$mcc_name}</b>) has just been topped up by <b>{$value}$</b>!

#################### ERROR #############################################
NOTIFICATION-CHANGE-EMAIL-ERROR = 📨❌ (FAILED) The email on account <b>{$account_name}</b> was NOT changed to <b>{$email}</b>!
    ━━━━━━━━━━━━━━━━
    <b>Database updated, but API request failed!!!</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT-ERROR = 💳❌ (FAILED) Internal top-up of <b>{$account_name}</b> for <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Remaining balance: <b>{$balance}</b>
    Balance UUID: <code>{$balance_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT-ERROR = 🔖❌ (FAILED) Refund for account <b>{$account_name}</b> with balance <b>{$balance}$</b>!
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Balance UUID: <code>{$balance_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT-ERROR = ❇️❌ (FAILED) Account <b>{$account_name}</b> was NOT created with balance <b>{$amount}$</b>!
    ━━━━━━━━━━━━━━━━
    Error: <b>{$error}</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Email: <code>{$email}</code>

    Limit: <b>{$limit}</b>
    Balance: <b>{$balance}</b>

    Username: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
