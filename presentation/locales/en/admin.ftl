#### English Translation ####

# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = 👥 Teams
ADMIN-MCC = 🏦 MCC
ADMIN-MESSAGING = ✉️ Messaging
ADMIN-PROFILE = 👤 Profile

SKIP = ⏭️ Skip

# TEAMS ################################################################################
TEAMS-CREATE = ➕ Create a new team
TEAMS-CREATE-NAME = 🏛️ Team name:
TEAMS-CREATE-SUCCESS = ✅ Team <b>{$team}</b> successfully created
TEAMS-CREATE-FAIL = ❌ Failed to create team (<b>{$error}</b>)
#################
TEAMS-CREATE-NAME_ERROR = ⚠️ Name too long (<b>{$symballs}</b> characters), must be within 50
################################################################################
TEAMS-DETAIL = ℹ️ ID: {$team_id}
    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>
    Users: 👥 <b>{$count_users}</b>
    Created: 🗓️ <b>{$created}</b>

    💵 Total amount of all transactions: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = 🔑 Team Access
TEAMS-ACCESS-CREATE = ➕ Create Access
TEAMS-ACCESS-CREATE-CONFIRMANTION = ❓ Do you want to create one-time access for the team <b>{$team}</b>?
TEAMS-ACCESS-CREATE-SUCCESS = ✅ Access for (<b>{$team}</b>) successfully created

    🔗 <code>{$deeplink}</code>
TEAMS-ACCESS-CREATE-FAIL = ❌ Failed to create access for (<b>{$team}</b>)
################################################################################
TEAMS-ACCESS-DETAIL = 🔑 Team: <b>{$team}</b>

    🔗 DeepLink: <code>{$deeplink}</code>

    👤 User ID: <code>{$user_id}</code>
    Username: @{$username}
    First name: {$firstname}
    Last name: {$lastname}

    🕒 Access created: <b>{$created}</b>
    🕒 Access activated: <b>{$activated}</b>
##################################################################################
TEAMS-ACCESS-DELETE = 🗑️ Delete Access
TEAMS-ACCESS-DELETE-WARNING = ⚠️ Deleting access will revoke all associated functionalities.

    ❗ <b>Are you sure to delete access?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = ✅ Confirm deletion
TEAMS-ACCESS-DELETE-SUCCESS = ✅ Access deleted
TEAMS-ACCESS-DELETE-FAIL = ❌ Failed to delete access
#################################################################################
TEAMS-DELETE = 🗑️ Delete Team
TEAMS-DELETE-WARNING = ⚠️ Are you sure you want to delete the team (<b>{$team}</b>)?

    🖙 This action cannot be undone!
TEAMS-DELETE-CONFIRMATION = ✅ Confirm team deletion
TEAMS-DELETE-SUCCESS = ✅ Team successfully deleted
TEAMS-DELETE-FAIL = ❌ Failed to delete team
###############################################
TEAMS-MCC-ACCESS = 🏦 Shared MCCs for team <b>{$team_name}</b>
TEAMS-MCC-ACCESS-DETAIL = ℹ️ <b>{$name}</b>
    👥 Available accounts: <b>{$account_available}</b>
    💰 Team balance: {$balance_team}$
    💰 Balance: {$balance}$
TEAMS-MCC-ACCOUNTS-LIMIT = 🔢 Account Limit
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE = 🔢 Enter the number of accounts:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_ERROR = ⚠️ You need to enter a number between 0 and 999:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_DUBL = ℹ️ The current limit <b>{$limit}</b> is already set, write a new one or cancel the operation:
TEAMS-MCC-ACCOUNTS-LIMIT-SUCCESS = ✅ Limit successfully updated to <b>{$limit}</b>
TEAMS-MCC-ACCOUNTS-LIMIT-FAIL = ❌ Failed to update the limit
TEAMS-MCC-SHARE = 🔗 Share
TEAMS-MCC-SHARE-CHOICE = 🏦 Select which MCC you want to share with the team <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = ❌ Failed to share MCC <b>{$error}</b>
TEAMS-MCC-SHARE-SUCCESS = ✅ MCC (<b>{$mcc_name}</b>) successfully shared with <b>{$team_name}</b>
TEAMS-MCC-RESHARE = 🔒 Remove Access
TEAMS-MCC-RESHARE-CONFIRMATION = ❓ Are you sure to remove access to MCC (<b>{$mcc_name}</b>) for team <b>{$team_name}</b>?
TEAMS-MCC-RESHARE-SUCCESS = ✅ Access removed
TEAMS-MCC-RESHARE-FAIL = ❌ Failed to remove access
########## MCC ############################################################################
MCC-AUTH-FAIL = ❌ MCC Authorization Failed <b>{$mcc_name}</b>
###############################################################
MCC-ADD = ➕ Add New MCC
MCC-ADD-NAME = 🏛️ Enter a name for the new MCC:
MCC-ADD-WALLET = 💼 Enter the wallet address for this MCC:
MCC-ADD-ID = 🖔 Enter the ID for the new MCC:
MCC-ADD-SECRET_TOKEN = 🔑 Enter the Secret Token for the new MCC:
##########################################################
MCC-ADD-NAME_ERROR = ⚠️ Name too long (<b>{$symballs}</b> characters), must be within 50
MCC-ADD-SUCCESS = ✅ MCC <b>{$mcc_name}</b> successfully added
MCC-ADD-FAIL = ❌ Failed to add MCC (<b>{$error}</b>)
###########################
MCC-DETAIL = ℹ️ <b>{$name}</b>
    💰 Balance: {$balance}$
    🔒 Available for new teams: <b>{$general}</b>
##############################################################
ACCOUNTS-DETAIL = ℹ️ <b>{$name}</b>
    =============================================
    🏦 MCC: <b>{$mcc_name}</b>
    Status: <b>{$status}</b>

    ✉️ Email: <code>{$email}</code>
    🌐 Time zone: <b>{$timezone}</b>
    🖔 Client ID: <code>{$customer_id}</code>

    💰 Balance: <b>{$balance}$</b>
    💸 Spend: <b>{$spend}$</b>
    🚷 Limit: <b>{$limit}$</b>

    👥 Team: <b>{$team_name}</b>
################## Messaging #################################################
MESSAGING-INPUT-MESSAGE = ✏️ Enter the message for the mailing:
MESSAGING-INPUT-IMAGE = 🖼️ Send a compressed image or skip
MESSAGING-SEND = ✉️ Send message
MESSAGING-RESULT = 📊 <b>-Mailing result-</b>

    📨 Messages received: {$send}\{$users}
    ⛔ Bot blocked: {$block}
    ⚙️ Other: {$other}
###################################################################################
TEAMS-TRANSACTIONS = 💸 Transactions
TEAMS-TRANSACTIONS-MCC = 💵 MCC Top-ups
TEAMS-TRANSACTIONS-SUB = 💰 Internal Transfers
TEAMS-TRANSACTIONS-TAX = 🚓 Commissions
TEAMS-TRANSACTIONS-MCC-DETAIL = ℹ️ <b>MCC Transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>

    💵 Top-up amount: <b>{$value}$</b>
    🗓️ Application date: <b>{$date}</b>

    🖔 Transaction ID: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-SUB-DETAIL = ℹ️ <b>Internal Transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>
    ✉️ Account: <code>{$account_email}</code>

    💵 Transfer amount: <b>{$value}$</b>
    🗓️ Transfer date: <b>{$date}</b>

    🖔 Transaction ID: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-TAX-DETAIL = ℹ️ <b>Commission Transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━
    🏢 Team: <b>{$team_name}</b>
    🏦 MCC: <b>{$mcc_name}</b> ({$client_link})

    💼 Transaction type: <b>{$kind}</b>
    💵 Commission amount: <b>{$amount} {$currency}</b>
    📄 Status: <b>{$status}</b>
    🔢 Date: <b>{$date}</b>

    ✉️ Email: <code>{$email}</code>

    🗋 <b>{$desc}</b>

    🖔 Transaction ID: <code>{$uuid_transaction}</code>
#####################
TEAMS-MCC-BALANCE-ADD = 💰 Add balance
TEAMS-MCC-BALANCE-VALUE = 💵 Top-up amount:
TEAMS-MCC-BALANCE-VALUE-ERROR = ⚠️ You need to enter a number:
TEAMS-MCC-BALANCE-CONFIRMATION = 💵 Is the top-up amount <b>{$value}</b> correct?
TEAMS-MCC-BALANCE-CREATE-TRANSACTION = 🏦 Create transaction
TEAMS-MCC-BALANCE-TOPUP-SUCCESS = ✅ MCC successfully topped up for the team
TEAMS-MCC-BALANCE-TOPUP-TRANSACTION-FAIL = ❌ Failed to top up MCC for the team (<b>{$error}</b>)
#################
MCC-GENERAL-SWITCH = 🔄 General On\Off
################### CREATE ACCOUNT #########
ADMIN-ACCOUNT-CREATE = 🔧 Create account
ADMIN-ACCOUNT-CREATE-NAME = 🏛️ Specify a name:
ADMIN-ACCOUNT-CREATE-NAME-ERROR = ⚠️ The name must be up to 255 characters, currently <b>{$len}</b>
ADMIN-ACCOUNT-CREATE-TEAM = 🖔 Specify the team UUID:
ADMIN-ACCOUNT-CREATE-TEAM-ERROR = ❌ No teams exist with this UUID
ADMIN-ACCOUNT-CREATE-TEAM-SKIP = ⏭️ Continue without a team
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_SKIP = ⏭️ Team skipped.
    ✉️ Specify an email:
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_CHOiCED = ✅ Selected team (<b>{$team_name}</b>).
    ✉️ Specify an email:
ADMIN-ACCOUNT-CREATE-AMOUNT = 💵 Top-up amount (min $50):
ADMIN-ACCOUNT-CREATE-TIMEZONE = 🌐 Specify a time zone, UTC(from -12 to +14), enter a number, e.g., +12 or -3:
ADMIN-ACCOUNT-CREATE-TIMEZONE-ERROR = ⚠️ Invalid format. UTC(from -12 to +14), enter a number, e.g., +12 or -3:
ADMIN-ACCOUNT-CREATE-FAIL = ❌ Error while creating account
    Error: <b>{$error}</b>
ADMIN-ACCOUNT-CREATE-SUCCESS = ✅ Account successfully created! Wait until it appears in your accounts under the specified MCC (<b>{$mcc_name}</b>)
##########
ADMIN-ACCOUNT-NO_VERIFY_YET = ⏳ Account not yet verified, check back later
##################### CHANGE TEAM #################
ADMIN-ACCOUNT-CHANGE_TEAM = 🔄 Change team
ADMIN-ACCOUNT-CHANGE_TEAM-UUID = 🖔 Specify the team ID:
ADMIN-ACCOUNT-CHANGE_TEAM-EXIST = ℹ️ This team already has this account
ADMIN-ACCOUNT-CHANGE_TEAM-ERROR = ❌ No team found with this ID
ADMIN-ACCOUNT-CHANGE_TEAM-SUCCESS = ✅ Successfully transferred to team <b>{$team_name}</b>
ADMIN-ACCOUNT-CHANGE_TEAM-FAIL = ❌ Failed to change the team for the account

#######################################
# Account (change email, refund, topup)
Change Email ###
ADMIN-ACCOUNT-CHANGE_EMAIL = ✉️ Change email
ADMIN-ACCOUNT-CHANGE_EMAIL-INPUT = ✉️ Specify a new email
ADMIN-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Failed to change email
ADMIN-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Invalid email format
ADMIN-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email successfully changed to <b>{$email}</b>
# Refund ###
ADMIN-ACCOUNT-REFUND = 💸 Refund
ADMIN-ACCOUNT-REFUND-CONFIRMATION-WARNING = ❓ Are you sure you want to refund the account <b>{$account_name}</b>?

    💵 Account balance (<b>{$balance}$</b>) will be returned to the main MCC
ADMIN-ACCOUNT-REFUND-CONFIRMATION = ✅ Confirm refund
ADMIN-ACCOUNT-REFUND-FAIL = ❌ An error occurred. Refund failed
ADMIN-ACCOUNT-REFUND-SUCCESS = ✅ Refund request sent successfully
# TopUp ###
ADMIN-ACCOUNT-TOPUP = 💳 Top up
ADMIN-ACCOUNT-TOPUP-VALUE = 💵 Enter top-up amount from <b>$50</b>:
ADMIN-ACCOUNT-TOPUP-VALUE-ERROR = ⚠️ Enter a number between <b>$50</b> and <b>$10,000</b>:
ADMIN-ACCOUNT-TOPUP-WARNING = ❓ Top up the account balance by <b>{$value}$</b>?
ADMIN-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Insufficient account balance.
    Your balance: <b>{$balance}$</b>
    Top-up request: <b>{$value}$</b>
ADMIN-ACCOUNT-TOPUP-CONFIRMATION = ✅ Confirm top-up
ADMIN-ACCOUNT-TOPUP-FAIL = ❌ Failed to top up
ADMIN-ACCOUNT-TOPUP-SUCCESS = ✅ Successfully topped up
################################## Specific API Functions #################################
ADMIN-SPECIFIC = ⚙️ Additional
#LOAD ACCOUNTS#
ADMIN-SPECIFIC-LOAD = 🔄 Load accounts
ADMIN-SPECIFIC-LOAD-CHOICE_MCC = Select MCC
ADMIN-SPECIFIC-LOAD-WARNING = ⚠️ Starting the process of loading new accounts from all MCCs added to the bot! During this process, accounts not yet in the bot's database will be assigned to the corresponding MCC.

    ❗ <b>Click only once, this process is resource-intensive</b>
ADMIN-SPECIFIC-LOAD-CONFIRMATION = ✅ Confirm loading
ADMIN-SPECIFIC-LOAD-PROCESSING = ⏳ Loading started, this may take some time
ADMIN-SPECIFIC-LOAD-PART = MCC <b>{$mcc_name}</b> Loaded <b>{$new_accounts}</b> new accounts. ({$current_accounts}/{$all_accounts})
ADMIN-SPECIFIC-LOAD-RESULT = ✅ Successfully loaded new accounts: <b>{$new_accounts}</b> 📊

    {$statistic}
ADMIN-SPECIFIC-LOAD-FAIL = ❌ Error adding account <b>{$email}</b> to MCC <b>{$mcc_name}</b>


#TAX PAYMENT#
ADMIN-SPECIFIC-TAX = 🔎 Load commission transactions
ADMIN-SPECIFIC-TAX-DOCUMENT = Send a <b>.csv</b> document for analysis
ADMIN-SPECIFIC-TAX-NO_DOCUMENT = Invalid file format ❌ Send a <b>.csv</b> document
ADMIN-SPECIFIC-TAX-ERROR = An error occurred ❌
    <code>{$error}</code>
ADMIN-SPECIFIC-TAX-FAIL = An error occurred ❌ <b>{$email}</b>
    <code>{$error}</code>
ADMIN-SPECIFIC-TAX-SUCCESS = Transaction added ✅ | <b>{$amount} {$currency}</b>
    {$client_link}➡️{$mcc_name} | {$team} | {$date}
    {$status} | {$email}
    {$desc}
ADMIN-SPECIFIC-TAX-SUMMARY = File analysis completed

    Transactions found in the file: {$taxes_count}
    Successfully processed: {$taxes_success} ✅
    Errors or duplicates: {$taxes_fail} ❌

    Processed transactions can be viewed in the transaction history or in Google Sheets using the link below.
    (Analytics in Google Sheets is updated every morning, but instantly in the bot)
ADMIN-SPECIFIC-TAX-GOOGLE_SHEET = Analytics in Google Sheets

MESSAGING-TAX-RESULT = <b>{$team_name}</b>
    -------
    📨 Received: {$send}\{$users}
    ⛔ Blocked bot: {$block}
    ⚙️ Other: {$other}
    ====================================


###########################################
ADMIN-SEARCH-ACCOUNT = 🔎 Search account
ADMIN-SEARCH-ACCOUNT-EMAIL = ✉️ Enter the email to search for an account:
ADMIN-SEARCH-ACCOUNT-NOTHING = ❌ No account found with this email
