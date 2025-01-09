NOTIFICATION-NEW_USER = 👤 <b>New user joined the bot!</b>
    ━━━━━━━━━━━━━━━━
    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>
    Joined: <b>{$join_at}</b>

NOTIFICATION-CREATE_TRANSACTION = 💵 <b>New top-up request</b>
    ━━━━━━━━━━━━━━━━
    Transaction hash: <code>{$hash}</code>

    MCC for top-up: <b>{$mcc_name}</b>
    WALLET: <code>{$wallet}</code>
    Top-up amount: <b>{$value}$</b>

    Team: <b>{$team_name}</b>
    Team balance for this MCC: <b>{$balance_team_value}$</b>
    Team ID: <code>{$team_uuid}</code>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CHANGE-EMAIL = 📨 Email for account <b>{$account_email}</b> has been changed to <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Team: <b>{$team_name}</b>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT = 💳 Internal top-up for <b>{$account_email}</b> of <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Remaining balance: <b>{$balance}</b>
    Team: <b>{$team_name}</b>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT = 🔖 Refund of account <b>{$account_email}</b> | <b>{$team_name}</b>!
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    MCC Balance: <b>{$mcc_balance}</b>

    Account Spend: <b>{$spend}</b>
    Account Balance: <b>{$balance_account}</b>
    Refund tax: <b>{$commission}</b>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT = ❇️ Account <b>{$account_email}</b> created with a balance of <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    MCC: <b>{$mcc_name}</b>
    Team: <b>{$team_name}</b>
    Limit: <b>{$limit}</b>
    Remaining balance: <b>{$balance}</b>

    Email: <code>{$email}</code>
    Timezone: <b>{$timezone}</b>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CLIENT-NEW_TOPUP = 💵 The balance for MCC (<b>{$mcc_name}</b>) has just been topped up by <b>{$value}$</b> !

#################### ERROR #############################################
NOTIFICATION-CHANGE-EMAIL-ERROR = 📨❌ (FAILED) Email for account <b>{$account_email}</b> was NOT changed to <b>{$email}</b> !
    ━━━━━━━━━━━━━━━━
    <b>The database was updated, but the API request failed!!!</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TOPUP-ACCOUNT-ERROR = 💳❌ (FAILED) Internal top-up for <b>{$account_email}</b> of <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Remaining balance: <b>{$balance}</b>
    Balance UUID: <code>{$balance_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-REFUND-ACCOUNT-ERROR = 🔖❌ (FAILED) Refund of account <b>{$account_email}</b> | <b>{$team_name}</b>!
    ━━━━━━━━━━━━━━━━
    <code>{$error}</code>

    MCC: <b>{$mcc_name}</b>
    UUID Balance: <code>{$balance_uuid}</code>

    MCC Balance: <b>{$balance_mcc}</b>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-CREATE-ACCOUNT-ERROR = ❇️❌ (FAILED) Account <b>{$account_email}</b> was NOT created with a balance of <b>{$amount}$</b> !
    ━━━━━━━━━━━━━━━━
    Error: <b>{$error}</b>

    MCC: <b>{$mcc_name}</b>
    MCC UUID: <code>{$mcc_uuid}</code>

    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>

    Email: <code>{$email}</code>

    Limit: <b>{$limit}</b>
    Balance: <b>{$balance}</b>

    Nickname: <b>@{$username}</b>
    Telegram ID: <code>{$user_id}</code>

NOTIFICATION-TEAM-COMMISSIONS_REPORT = Commission report 💸
    Commission transactions: {$taxes_count}
    Total amount: <b>{$taxes_amount} USD</b>

    Detailed information is available in "Commission transactions"
