#################################### General ################################################
NONAME-NO_ACCESS = 🛑 You don't have access, please ask administrators

REGISTER-SUCCESS = ✅ Successfully registered!
REGISTER-FAIL = ❌ Registration failed

MENU = 📋 Menu
BACK = 🔙 Back

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = ❗ The key doesn't exist!
JOIN_KEY-ACTIVATED_BEFORE = 🔑 The key was activated before you!
JOIN_KEY-FAIL_UPDATE = ⚠️ Some error occurred. The team key was not set
JOIN_KEY-SUCCESS_UPDATE = 🔓 Team key set successfully!

#################################### Accounts #################################################
CLIENT-ACCOUNTS = 👥 Accounts
CLIENT-ACCOUNTS-DETAIL = Account: <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Status: <b>{$status}</b>

    Email: <code>{$email}</code>
    Timezone: <b>{$timezone}</b>
    Customer ID: <code>{$customer_id}</code>

    Balance: <b>{$balance}$</b>
    Spend: <b>{$spend}$</b>
    Limit: <b>{$limit}$</b>

########################## MCC ###################################################
CLIENT-MCC = 🏦 Choose MCC for account management
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Available accounts: <b>{$account_available}</b>
    Balance: {$balance}$

CLIENT-MCC-BALANCE-ADD = 💰 Add balance
CLIENT-MCC-BALANCE-VALUE = Amount to add from <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = ❗ Enter an amount between <b>100$</b> and <b>10,000$</b>:
CLIENT-MCC-BALANCE-SUCCESS = ✅ Balance top-up request sent
CLIENT-MCC-BALANCE-FAIL = ❌ Failed to send top-up request

########################## Account (change email, refund, topup) ###########################
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = ✉️ Change email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Enter the new email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Failed to change email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Invalid email format
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email successfully changed to <b>{$email}</b>

# Refund ###
CLIENT-ACCOUNT-REFUND = 💸 Refund
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Are you sure you want to refund the account <b>{$account_name}</b>?

    The account balance (<b>{$balance}$</b>) will be returned to the main MCC
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Confirm refund
CLIENT-ACCOUNT-REFUND-FAIL = ❌ An error occurred. Refund failed
CLIENT-ACCOUNT-REFUND-SUCCESS = ✅ Refund request successfully sent

# TopUp ###
CLIENT-ACCOUNT-TOPUP = 💰 Top up
CLIENT-ACCOUNT-TOPUP-VALUE = Enter top-up amount from <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = ❗ Enter an amount between <b>100$</b> and <b>10,000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Top up the account balance with <b>{$value}$</b>?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Insufficient balance.
    Your balance: <b>{$balance}$</b>
    Requested top-up: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Confirm top-up
CLIENT-ACCOUNT-TOPUP-FAIL = ❌ Top-up failed
CLIENT-ACCOUNT-TOPUP-SUCCESS = ✅ Successfully topped up

CLIENT-ACCOUNT-CREATE = 🆕 Create account
CLIENT-ACCOUNT-CREATE-LIMIT = ❗ You have reached the account creation limit for this MCC
CLIENT-ACCOUNT-CREATE-NAME = Enter account name:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = ❗ The name must be up to 255 characters, currently <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Enter email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Top-up amount (min 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = ❗ Insufficient funds to top up account (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Enter the timezone, UTC (from -12 to +14), enter a number, e.g., +12 or -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = ❗ Invalid format. UTC (from -12 to +14), enter a number, e.g., +12 or -3:
CLIENT-ACCOUNT-CREATE-FAIL = ❌ Account creation failed
CLIENT-ACCOUNT-CREATE-SUCCESS = ✅ Account successfully created! Wait for it to appear in your accounts under MCC (<b>{$mcc_name}</b>)

CLIENT-ACCOUNT-NO_VERIFY_YET = ⏱️ Account not verified yet, check back later ⏱️
