#################################### General ################################################
NONAME-NO_ACCESS = 🛑 You do not have access, please contact administrators

REGISTER-SUCCESS = Welcome! 👋 You have entered MT Agency — a service created by the Masons Traffic team specifically for working with Google agency accounts
REGISTER-FAIL = ❌ Registration failed

MENU = 📋 Menu
BACK = 🔙 Back

HELLO_TEXT =

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = ❗ Key does not exist!
JOIN_KEY-ACTIVATED_BEFORE = 🔑 The key was activated before you!
JOIN_KEY-FAIL_UPDATE = ⚠️ Something went wrong. Team key not set
JOIN_KEY-SUCCESS_UPDATE = 🔓 Team key successfully set!

#################################### Accounts #################################################
CLIENT-ACCOUNTS = 👥 Accounts
CLIENT-ACCOUNTS-DETAIL = Account: <b>{$name}</b>
    =============================================
    MCC: <b>{$mcc_name}</b>
    Status: <b>{$status}</b>

    Email: <code>{$email}</code>
    Time zone: <b>{$timezone}</b>
    Client ID: <code>{$customer_id}</code>

    Balance: <b>{$balance}$</b>
    Spend: <b>{$spend}$</b>
    Limit: <b>{$limit}$</b>

########################## MCC ###################################################
CLIENT-MCC = 🏦 Select MCC for account management
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Available accounts: <b>{$account_available}</b>
    Balance: {$balance}$

CLIENT-MCC-BALANCE-ADD = 💰 Top-up balance
CLIENT-MCC-BALANCE-VALUE = Top-up amount from <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = ❗ Please enter an amount between <b>100$</b> and <b>10,000$</b>:
CLIENT-MCC-BALANCE-HASH = 📄 Top up the balance with the specified amount and <b>send the transaction hash</b>:

    <b>Wallets for top-up</b>

    📌 <code>TR5zws4EYZtrExwLc6EDGgdMfZ958EhVSm</code>
      USDT TRC20

    📌 <code>0x5129f986ef3751480aecaa9ddade59fbc48230fe</code>
      USDT ERC20

CLIENT-MCC-BALANCE-SUCCESS = ✅ Top-up request sent successfully
CLIENT-MCC-BALANCE-FAIL = ❌ Failed to send top-up request

########################## Account (change email, refund, topup) ###########################
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = ✉️ Change email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Enter new email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Failed to change email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Invalid email format
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email successfully changed to <b>{$email}</b>

# Refund ###
CLIENT-ACCOUNT-REFUND = 💸 Refund
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Are you sure you want to refund the account <b>{$account_name}</b>?

    The account balance (<b>{$balance}$</b>) will be returned to the main MCC
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Confirm refund
CLIENT-ACCOUNT-REFUND-FAIL = ❌ An error occurred. Refund failed
CLIENT-ACCOUNT-REFUND-SUCCESS = ✅ Refund request sent successfully

# TopUp ###
CLIENT-ACCOUNT-TOPUP = 💰 Top-up
CLIENT-ACCOUNT-TOPUP-VALUE = Enter top-up amount from <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = ❗ Please enter an amount between <b>100$</b> and <b>10,000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Top-up account balance with <b>{$value}$</b>?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Insufficient balance on the account.
    Your balance: <b>{$balance}$</b>
    Requested top-up: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Confirm top-up
CLIENT-ACCOUNT-TOPUP-FAIL = ❌ Top-up error
CLIENT-ACCOUNT-TOPUP-SUCCESS = ✅ Successfully topped up

CLIENT-ACCOUNT-CREATE = 🆕 Create account
CLIENT-ACCOUNT-CREATE-LIMIT = ❗ You have reached the account creation limit for this MCC
CLIENT-ACCOUNT-CREATE-NAME = Enter account name:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = ❗ Name must be up to 255 characters, currently <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Enter email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Top-up amount (min 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = ❗ The balance is insufficient to top up the account (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Enter time zone, UTC (from -12 to +14), enter a number like +12 or -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = ❗ Invalid format. UTC (from -12 to +14), enter a number like +12 or -3:
CLIENT-ACCOUNT-CREATE-FAIL = ❌ Error creating account
CLIENT-ACCOUNT-CREATE-SUCCESS = ✅ Account successfully created! Wait for it to appear in your MCC accounts (<b>{$mcc_name}</b>)

CLIENT-ACCOUNT-NO_VERIFY_YET = ⏱️ Account not yet verified, try again later ⏱️
