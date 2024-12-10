# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = 👥 Teams
ADMIN-MCC = 🏦 MCC
ADMIN-MESSAGING = ✉️ Messaging
ADMIN-PROFILE = 👤 Profile

SKIP = ⏭️ Skip

# TEAMS ################################################################################
TEAMS-CREATE = ➕ Create new team
TEAMS-CREATE-NAME = 🏷️ Team name:
TEAMS-CREATE-SUCCESS = ✅ Team <b>{$team}</b> successfully created
TEAMS-CREATE-FAIL = ❌ Error creating team (<b>{$error}</b>)
#################
TEAMS-CREATE-NAME_ERROR = ⚠️ Name too long (<b>{$symballs}</b> characters), keep it under 50
################################################################################
TEAMS-DETAIL = ℹ️ ID: {$team_id}
    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>
    Users: 👥 <b>{$count_users}</b>
    Created: 🗓️ <b>{$created}</b>

    💵 Total transaction sum: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = 🔑 Team access
TEAMS-ACCESS-CREATE = ➕ Create access
TEAMS-ACCESS-CREATE-CONFIRMANTION = ❓ Do you want to create one-time access to the team <b>{$team}</b>?
TEAMS-ACCESS-CREATE-SUCCESS = ✅ Access for (<b>{$team}</b>) successfully created

    🔗 <code>{$deeplink}</code>
TEAMS-ACCESS-CREATE-FAIL = ❌ Error creating access for (<b>{$team}</b>)
################################################################################
TEAMS-ACCESS-DETAIL = 🔑 Team: <b>{$team}</b>

    🔗 DeepLink: <code>{$deeplink}</code>

    👤 User ID: <code>{$user_id}</code>
    UserName: @{$username}
    First Name: {$firstname}
    Last Name: {$lastname}

    🕒 Access created: <b>{$created}</b>
    🕒 Access activated: <b>{$activated}</b>
##################################################################################
TEAMS-ACCESS-DELETE = 🗑️ Delete access
TEAMS-ACCESS-DELETE-WARNING = ⚠️ Deleting access will remove the user's functionality

    ❗ <b>Are you sure you want to delete access?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = ✅ Confirm deletion
TEAMS-ACCESS-DELETE-SUCCESS = ✅ Access deleted
TEAMS-ACCESS-DELETE-FAIL = ❌ Failed to delete access
#################################################################################
TEAMS-DELETE = 🗑️ Delete team
TEAMS-DELETE-WARNING = ⚠️ Are you sure you want to delete the team (<b>{$team}</b>)?

    🔙 This action is irreversible!
TEAMS-DELETE-CONFIRMATION = ✅ Confirm team deletion
TEAMS-DELETE-SUCCESS = ✅ Team successfully deleted
TEAMS-DELETE-FAIL = ❌ Failed to delete team
###############################################
TEAMS-MCC-ACCESS = 🏦 MCCs shared with the team <b>{$team_name}</b>
TEAMS-MCC-ACCESS-DETAIL = ℹ️ <b>{$name}</b>
    👥 Accounts available: <b>{$account_available}</b>
    💰 Team balance: {$balance_team}$
    💰 Balance: {$balance}$
TEAMS-MCC-ACCOUNTS-LIMIT = 🔢 Account limit
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE = 🔢 Enter the number of accounts:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_ERROR = ⚠️ Enter a number between 0 and 999:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_DUBL = ℹ️ Current limit is <b>{$limit}</b>, enter a new value or cancel the operation:
TEAMS-MCC-ACCOUNTS-LIMIT-SUCCESS = ✅ Limit successfully changed to <b>{$limit}</b>
TEAMS-MCC-ACCOUNTS-LIMIT-FAIL = ❌ Failed to change the limit
TEAMS-MCC-SHARE = 🔗 Share
TEAMS-MCC-SHARE-CHOICE = 🏦 Select which MCC to share with the team <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = ❌ Failed to share MCC <b>{$error}</b>
TEAMS-MCC-SHARE-SUCCESS = ✅ MCC (<b>{$mcc_name}</b>) successfully shared with <b>{$team_name}</b>
TEAMS-MCC-RESHARE = 🔒 Remove access
TEAMS-MCC-RESHARE-CONFIRMATION = ❓ Are you sure you want to remove access to MCC (<b>{$mcc_name}</b>) from the team <b>{$team_name}</b>?
TEAMS-MCC-RESHARE-SUCCESS = ✅ Access removed
TEAMS-MCC-RESHARE-FAIL = ❌ Failed to remove access
########## MCC ############################################################################
MCC-AUTH-FAIL = ❌ Error authorizing MCC <b>{$mcc_name}</b>
###############################################################
MCC-ADD = ➕ Add new MCC
MCC-ADD-NAME = 🏷️ Enter name for new MCC:
MCC-ADD-WALLET = 👛 Enter crypto wallet address for MCC:
MCC-ADD-ID = 🆔 Enter ID for new MCC:
MCC-ADD-SECRET_TOKEN = 🔑 Enter Secret Token for new MCC:
##########################################################
MCC-ADD-NAME_ERROR = ⚠️ Name too long (<b>{$symballs}</b> characters), keep it under 50
MCC-ADD-SUCCESS = ✅ MCC <b>{$mcc_name}</b> successfully added
MCC-ADD-FAIL = ❌ Error adding MCC (<b>{$error}</b>)
###########################
MCC-DETAIL = ℹ️ <b>{$name}</b>
    💰 Balance: {$balance}$
    🔓 Available for new teams: <b>{$general}</b>
##############################################################
ACCOUNTS-DETAIL = ℹ️ <b>{$name}</b>
    =============================================
    🏦 MCC: <b>{$mcc_name}</b>
    Status: <b>{$status}</b>

    ✉️ Email: <code>{$email}</code>
    🌐 Timezone: <b>{$timezone}</b>
    🆔 Client ID: <code>{$customer_id}</code>

    💰 Balance: <b>{$balance}$</b>
    💸 Spend: <b>{$spend}$</b>
    🛑 Limit: <b>{$limit}$</b>

    👥 Team: <b>{$team_name}</b>
################## Messaging #################################################
MESSAGING-INPUT-MESSAGE = ✏️ Enter a message for the broadcast:
MESSAGING-INPUT-IMAGE = 🖼️ Send a compressed image or skip
MESSAGING-SEND = ✉️ Send message
MESSAGING-RESULT = 📊 <b>-Broadcast Results-</b>

    📬 Delivered to: {$send}\{$users}
    🚫 Bot blocked: {$block}
    ⚙️ Other: {$other}
###################################################################################
TEAMS-TRANSACTIONS = 💸 Transactions
TEAMS-TRANSACTIONS-MCC = 💵 MCC Top-Up
TEAMS-TRANSACTIONS-SUB = 💰 Internal Transfers
TEAMS-TRANSACTIONS-MCC-DETAIL = ℹ️ <b>MCC Transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>

    💵 Top-Up amount: <b>{$value}$</b>
    🗓️ Date of request: <b>{$date}</b>

    🆔 Transaction ID: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-SUB-DETAIL = ℹ️ <b>Internal Transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>
    📧 Account: <code>{$account_email}</code>

    💵 Transfer amount: <b>{$value}$</b>
    🗓️ Transfer date: <b>{$date}</b>

    🆔 Transaction ID: <code>{$uuid_transaction}</code>
#####################
TEAMS-MCC-BALANCE-ADD = 💰 Top-up balance
TEAMS-MCC-BALANCE-VALUE = 💵 Top-up amount:
TEAMS-MCC-BALANCE-VALUE-ERROR = ⚠️ Please enter a number:
TEAMS-MCC-BALANCE-CONFIRMATION = 💵 Is the amount <b>{$value}</b> correct?
TEAMS-MCC-BALANCE-CREATE-TRANSACTION = 🏦 Create transaction
TEAMS-MCC-BALANCE-TOPUP-SUCCESS = ✅ MCC successfully topped up for the team
TEAMS-MCC-BALANCE-TOPUP-TRANSACTION-FAIL = ❌ Failed to top-up MCC for the team (<b>{$error}</b>)
#################
MCC-GENERAL-SWITCH = 🔄 General On\Off
################### CREATE ACCOUNT #########
ADMIN-ACCOUNT-CREATE = 🆕 Create account
ADMIN-ACCOUNT-CREATE-NAME = 🏷️ Enter name:
ADMIN-ACCOUNT-CREATE-NAME-ERROR = ⚠️ Name must be under 255 characters, currently <b>{$len}</b>
ADMIN-ACCOUNT-CREATE-TEAM = 🆔 Enter team UUID:
ADMIN-ACCOUNT-CREATE-TEAM-ERROR = ❌ No team exists with this UUID
ADMIN-ACCOUNT-CREATE-TEAM-SKIP = ⏭️ Continue without team
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_SKIP = ⏭️ Team skipped.
    ✉️ Enter email:
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_CHOiCED = ✅ Selected team (<b>{$team_name}</b>).
    ✉️ Enter email:
ADMIN-ACCOUNT-CREATE-AMOUNT = 💵 Top-up amount (min 50$):
ADMIN-ACCOUNT-CREATE-TIMEZONE = 🌐 Enter timezone, UTC (from -12 to +14), enter a number like +12 or -3:
ADMIN-ACCOUNT-CREATE-TIMEZONE-ERROR = ⚠️ Incorrect format. UTC (from -12 to +14), enter a number like +12 or -3:
ADMIN-ACCOUNT-CREATE-FAIL = ❌ Error creating account
    Error: <b>{$error}</b>
ADMIN-ACCOUNT-CREATE-SUCCESS = ✅ Account successfully created! Wait for it to appear in your MCC (<b>{$mcc_name}</b>)
##########
ADMIN-ACCOUNT-NO_VERIFY_YET = ⏱️ Account not yet verified, try later
##################### CHANGE TEAM #################
ADMIN-ACCOUNT-CHANGE_TEAM = 🔄 Change team
ADMIN-ACCOUNT-CHANGE_TEAM-UUID = 🆔 Enter team UUID:
ADMIN-ACCOUNT-CHANGE_TEAM-EXIST = ℹ️ Team with this UUID already has this account
ADMIN-ACCOUNT-CHANGE_TEAM-ERROR = ❌ No team exists with this UUID
ADMIN-ACCOUNT-CHANGE_TEAM-SUCCESS = ✅ Successfully transferred to team <b>{$team_name}</b>
ADMIN-ACCOUNT-CHANGE_TEAM-FAIL = ❌ Failed to change account team

#######################################
# Account (change email, refund, top-up)
Change Email ###
ADMIN-ACCOUNT-CHANGE_EMAIL = ✉️ Change email
ADMIN-ACCOUNT-CHANGE_EMAIL-INPUT = ✉️ Enter new email
ADMIN-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Failed to change email
ADMIN-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Invalid email format
ADMIN-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email successfully changed to <b>{$email}</b>
# Refund ###
ADMIN-ACCOUNT-REFUND = 💸 Refund
ADMIN-ACCOUNT-REFUND-CONFIRMATION-WARNING = ❓ Are you sure you want to refund the account <b>{$account_name}</b>?

    💵 Account balance (<b>{$balance}$</b>) will be returned to the main MCC
ADMIN-ACCOUNT-REFUND-CONFIRMATION = ✅ Confirm refund
ADMIN-ACCOUNT-REFUND-FAIL = ❌ Error occurred. Refund failed
ADMIN-ACCOUNT-REFUND-SUCCESS = ✅ Refund request successfully sent
# TopUp ###
ADMIN-ACCOUNT-TOPUP = 💳 Top-up
ADMIN-ACCOUNT-TOPUP-VALUE = 💵 Enter top-up amount from <b>50$</b>:
ADMIN-ACCOUNT-TOPUP-VALUE-ERROR = ⚠️ Enter an amount between <b>50$</b> and <b>10,000$</b>:
ADMIN-ACCOUNT-TOPUP-WARNING = ❓ Top-up account with <b>{$value}$</b>?
ADMIN-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Insufficient balance.
    Your balance: <b>{$balance}$</b>
    Requested top-up: <b>{$value}$</b>
ADMIN-ACCOUNT-TOPUP-CONFIRMATION = ✅ Confirm top-up
ADMIN-ACCOUNT-TOPUP-FAIL = ❌ Error during top-up
ADMIN-ACCOUNT-TOPUP-SUCCESS = ✅ Successfully topped up
################################## Specific API Functions #################################
ADMIN-SPECIFIC = ⚙️ Additional
ADMIN-SPECIFIC-LOAD = 🔄 Load accounts
ADMIN-SPECIFIC-LOAD-CHOICE_MCC = Choose MCC
ADMIN-SPECIFIC-LOAD-WARNING = ⚠️ This will start the process of loading new accounts from all MCCs added to the bot! During this process, any accounts not yet in the bot's database will be added to the corresponding MCC.

    ❗ <b>Press only once, this is a resource-intensive process</b>
ADMIN-SPECIFIC-LOAD-CONFIRMATION = ✅ Confirm loading
ADMIN-SPECIFIC-LOAD-PROCESSING = ⏳ Loading started, this will take some time
ADMIN-SPECIFIC-LOAD-PART = MCC <b>{$mcc_name}</b> Loaded <b>{$new_accounts}</b> new accounts. ({$current_accounts}/{$all_accounts})
ADMIN-SPECIFIC-LOAD-RESULT = ✅ Successfully loaded new accounts: <b>{$new_accounts}</b> 📊

    {$statistic}
ADMIN-SPECIFIC-LOAD-FAIL = ❌ Error adding account <b>{$email}</b> to MCC <b>{$mcc_name}</b>
###########################################
ADMIN-SEARCH-ACCOUNT = 🔎 Account search
ADMIN-SEARCH-ACCOUNT-EMAIL = 📨 Enter email to search for an account:
ADMIN-SEARCH-ACCOUNT-NOTHING = ❌ No account with this email was found
