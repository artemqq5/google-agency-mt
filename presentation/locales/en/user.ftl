#################################### General ################################################
NONAME-NO_ACCESS = 🛑 You do not have access, please ask the administrators

REGISTER-SUCCESS = Welcome! 👋 You have joined MT Agency - a service created by the Masons Traffic team specifically for working with Google agency accounts
REGISTER-FAIL = ❌ Registration error

MENU = 📋 Menu
BACK = 🔙 Back

CLIENT-ACCOUNT-NOT_EXIST = The account does not exist

FAQ = ℹ️ FAQ
OPEN = Open
FAQ_MESSAGE = Instructions for working with MT Agency Google accounts

################################### NONAME ###############################################
JOIN_KEY-NOT_EXIST = ❗ Key does not exist!
JOIN_KEY-ACTIVATED_BEFORE = 🔑 The key was previously activated by someone else!
JOIN_KEY-FAIL_UPDATE = ⚠️ An error occurred. The team key was not set
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
CLIENT-MCC = 🏦 Choose an MCC to manage accounts
CLIENT-MCC-DETAIL = MCC (<b>{$name}</b>)
    Accounts available: <b>{$account_available}</b>
    Balance: {$balance}$

CLIENT-MCC-BALANCE-ADD = 💰 Add funds
CLIENT-MCC-BALANCE-VALUE = Top-up amount from <b>100$</b>:
CLIENT-MCC-BALANCE-VALUE-ERROR = ❗ You must enter a number between <b>100$</b> and <b>10,000$</b>:
CLIENT-MCC-BALANCE-HASH-SEND = 📄❗ <b>Send the transaction hash</b>:
CLIENT-MCC-BALANCE-HASH =  📄 Top up your balance by <b>{$sum}$</b>:

    ❗For amounts less than the specified value, payment will not be processed automatically❗

    <b>Wallets for top-up</b>

    📌 <code>TR5zws4EYZtrExwLc6EDGgdMfZ958EhVSm</code>
      USDT TRC20

    📌 <code>0x5129f986ef3751480aecaa9ddade59fbc48230fe</code>
      USDT ERC20

CLIENT-MCC-BALANCE-SUCCESS = ✅ Top-up request sent successfully
CLIENT-MCC-BALANCE-FAIL = ❌ Failed to send top-up request

########################## Account (change email, refund, top-up) ###########################
# Change Email ###
CLIENT-ACCOUNT-CHANGE_EMAIL = ✉️ Change email
CLIENT-ACCOUNT-CHANGE_EMAIL-INPUT = Enter new email
CLIENT-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Failed to change email
CLIENT-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Invalid email format
CLIENT-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email successfully changed to <b>{$email}</b>

# Refund ###
CLIENT-ACCOUNT-REFUND = 💸 Refund
CLIENT-ACCOUNT-REFUND-CONFIRMATION-WARNING = Are you sure you want to refund the account <b>{$account_name}</b>?

    Account balance <b>{$balance}$</b> will be returned to the main MCC
    WARNING! Fee 4% = <b>{$commission}$</b>
CLIENT-ACCOUNT-REFUND-CONFIRMATION = Confirm refund
CLIENT-ACCOUNT-REFUND-FAIL = ❌ An error occurred. Refund failed
CLIENT-ACCOUNT-REFUND-SUCCESS = ✅ Refund request sent successfully

# TopUp ###
CLIENT-ACCOUNT-TOPUP = 💰 Top up
CLIENT-ACCOUNT-TOPUP-VALUE = Enter top-up amount from <b>100$</b>:
CLIENT-ACCOUNT-TOPUP-VALUE-ERROR = ❗ You must enter a number between <b>100$</b> and <b>10,000$</b>:
CLIENT-ACCOUNT-TOPUP-WARNING = Top up account balance by <b>{$value}$</b>?
CLIENT-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Insufficient account balance.
    Your balance: <b>{$balance}$</b>
    Top-up request: <b>{$value}$</b>
CLIENT-ACCOUNT-TOPUP-CONFIRMATION = Confirm top-up
CLIENT-ACCOUNT-TOPUP-FAIL = ❌ Top-up failed
CLIENT-ACCOUNT-TOPUP-SUCCESS = ✅ Successfully topped up

CLIENT-ACCOUNT-CREATE = 🆕 Create account
CLIENT-ACCOUNT-CREATE-LIMIT = ❗ You have reached the account creation limit for this MCC
CLIENT-ACCOUNT-CREATE-NAME = Enter name:
CLIENT-ACCOUNT-CREATE-NAME-ERROR = ❗ The name must be up to 255 characters, currently <b>{$len}</b>
CLIENT-ACCOUNT-CREATE-EMAIL = Enter email:
CLIENT-ACCOUNT-CREATE-AMOUNT = Top-up amount (min 100$):
CLIENT-ACCOUNT-CREATE-AMOUNT-NOMONEY = ❗ Not enough funds to top up the account (<b>{$balance}$</b>)
CLIENT-ACCOUNT-CREATE-TIMEZONE = Enter timezone, UTC(from -12 to +14), enter a number, e.g., +12 or -3:
CLIENT-ACCOUNT-CREATE-TIMEZONE-ERROR = ❗ Invalid format. UTC(from -12 to +14), enter a number, e.g., +12 or -3:
CLIENT-ACCOUNT-CREATE-FAIL = ❌ Account creation failed
CLIENT-ACCOUNT-CREATE-SUCCESS = ✅ Account successfully created! Wait until it appears in your accounts under the specified MCC (<b>{$mcc_name}</b>)

CLIENT-ACCOUNT-NO_VERIFY_YET = ⏱️ Account not verified yet, please check back later ⏱️
########################## TAX
CLIENT-TAXES = 🚕 Taxes
CLIENT-TRANSACTIONS-TAX-DETAIL = ℹ️ <b>Commission transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b> ({$client_link})

    💵 Commission amount: <b>{$amount} {$currency}</b>
    📅 Date: <b>{$date}</b>

    📧 Email: <code>{$email}</code>

    📝 <b>{$desc}</b>

    🆔 Transaction ID: <code>{$uuid_transaction}</code>

CLIENT-WAIT_FOR_REQUEST = Wait a few seconds before asking again!