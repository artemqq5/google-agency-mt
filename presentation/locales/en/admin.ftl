# MAIN ADMIN MENU #########################################################################
ADMIN-TEAMS = 👥 Teams
ADMIN-MCC = 🏦 MCC
ADMIN-MESSAGING = ✉️ Messaging
ADMIN-PROFILE = 👤 Profile

SKIP = ⏭️ Skip

# TEAMS ################################################################################
TEAMS-CREATE = ➕ Create a new team
TEAMS-CREATE-NAME = 🏷️ Team name:
TEAMS-CREATE-SUCCESS = ✅ Team <b>{$team}</b> created successfully
TEAMS-CREATE-FAIL = ❌ Error creating team (<b>{$error}</b>)
#################
TEAMS-CREATE-NAME_ERROR = ⚠️ Name is too long (<b>{$symballs}</b> characters), should be within 50
################################################################################
TEAMS-DETAIL = ℹ️ ID: {$team_id}
    Team: <b>{$team_name}</b>
    Team UUID: <code>{$team_uuid}</code>
    Users: 👥 <b>{$count_users}</b>
    Created: 🗓️ <b>{$created}</b>

    💵 Total sum of all transactions: <b>{$transactions_all}$</b>
################################################################################
TEAMS-ACCESS = 🔑 Team access
TEAMS-ACCESS-CREATE = ➕ Create access
TEAMS-ACCESS-CREATE-CONFIRMANTION = ❓ Do you want to create one-time access for team <b>{$team}</b>?
TEAMS-ACCESS-CREATE-SUCCESS = ✅ Access for (<b>{$team}</b>) created successfully

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
TEAMS-ACCESS-DELETE-WARNING = ⚠️ Deleting access will remove the user’s functionality

    ❗ <b>Are you sure you want to delete access?</b>
TEAMS-ACCESS-DELETE-CONFIRMATION = ✅ Confirm deletion
TEAMS-ACCESS-DELETE-SUCCESS = ✅ Access deleted
TEAMS-ACCESS-DELETE-FAIL = ❌ Failed to delete access
#################################################################################
TEAMS-DELETE = 🗑️ Delete team
TEAMS-DELETE-WARNING = ⚠️ Are you sure you want to delete the team (<b>{$team}</b>)?

    🔙 This action cannot be undone!
TEAMS-DELETE-CONFIRMATION = ✅ Confirm team deletion
TEAMS-DELETE-SUCCESS = ✅ Team deleted successfully
TEAMS-DELETE-FAIL = ❌ Failed to delete team
###############################################
TEAMS-MCC-ACCESS = 🏦 MCC shared for team <b>{$team_name}</b>
TEAMS-MCC-ACCESS-DETAIL = ℹ️ <b>{$name}</b>
    👥 Accounts available: <b>{$account_available}</b>
    💰 Team balance: {$balance_team}$
    💰 Balance: {$balance}$
TEAMS-MCC-ACCOUNTS-LIMIT = 🔢 Account limit
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE = 🔢 Enter the number of accounts:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_ERROR = ⚠️ Enter a number from 0 to 999:
TEAMS-MCC-ACCOUNTS-LIMIT-VALUE_DUBL = ℹ️ The current limit is already <b>{$limit}</b>, enter a new one or cancel the operation:
TEAMS-MCC-ACCOUNTS-LIMIT-SUCCESS = ✅ Limit successfully changed to <b>{$limit}</b>
TEAMS-MCC-ACCOUNTS-LIMIT-FAIL = ❌ Failed to change the limit
TEAMS-MCC-SHARE = 🔗 Share access
TEAMS-MCC-SHARE-CHOICE = 🏦 Choose which MCC to share for team <b>{$team_name}</b>
TEAMS-MCC-SHARE-FAIL = ❌ Failed to share MCC <b>{$error}</b>
TEAMS-MCC-SHARE-SUCCESS = ✅ MCC (<b>{$mcc_name}</b>) successfully shared with team <b>{$team_name}</b>
TEAMS-MCC-RESHARE = 🔒 Remove access
TEAMS-MCC-RESHARE-CONFIRMATION = ❓ Are you sure you want to remove MCC access (<b>{$mcc_name}</b>) for team <b>{$team_name}</b>?
TEAMS-MCC-RESHARE-SUCCESS = ✅ Access removed
TEAMS-MCC-RESHARE-FAIL = ❌ Failed to remove access
########## MCC ############################################################################
MCC-AUTH-FAIL = ❌ MCC authorization failed for <b>{$mcc_name}</b>
###############################################################
MCC-ADD = ➕ Add new MCC
MCC-ADD-NAME = 🏷️ Enter a name for the new MCC:
MCC-ADD-ID = 🆔 Enter the ID for the new MCC:
MCC-ADD-SECRET_TOKEN = 🔑 Enter the Secret Token for the new MCC:
##########################################################
MCC-ADD-NAME_ERROR = ⚠️ Name is too long (<b>{$symballs}</b> characters), should be within 50
MCC-ADD-SUCCESS = ✅ MCC <b>{$mcc_name}</b> added successfully
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
    🌐 Time zone: <b>{$timezone}</b>
    🆔 Customer ID: <code>{$customer_id}</code>

    💰 Balance: <b>{$balance}$</b>
    💸 Spend: <b>{$spend}$</b>
    🛑 Limit: <b>{$limit}$</b>

    👥 Team: <b>{$team_name}</b>
################## Messaging #################################################
MESSAGING-INPUT-MESSAGE = ✏️ Enter a message for messaging:
MESSAGING-INPUT-IMAGE = 🖼️ Send a compressed photo or skip
MESSAGING-SEND = ✉️ Send message
MESSAGING-RESULT = 📊 <b>-Messaging Result-</b>

    📬 Message received: {$send}\{$users}
    🚫 Blocked bot: {$block}
    ⚙️ Other: {$other}
###################################################################################
TEAMS-TRANSACTIONS = 💸 Transactions
TEAMS-TRANSACTIONS-MCC = 💵 MCC Top-up
TEAMS-TRANSACTIONS-SUB = 💰 Internal transfers
TEAMS-TRANSACTIONS-MCC-DETAIL = ℹ️ <b>MCC transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>

    💵 Top-up amount: <b>{$value}$</b>
    🗓️ Date of request: <b>{$date}</b>

    🆔 Transaction ID: <code>{$uuid_transaction}</code>
TEAMS-TRANSACTIONS-SUB-DETAIL = ℹ️ <b>Internal transaction #{$id_transaction}</b>
    ━━━━━━━━━━━━━━━━
    🏦 MCC: <b>{$mcc_name}</b>
    📧 Account: <code>{$account_email}</code>

    💵 Top-up amount: <b>{$value}$</b>
    🗓️ Transfer date: <b>{$date}</b>

    🆔 Transaction ID: <code>{$uuid_transaction}</code>
#####################
TEAMS-MCC-BALANCE-ADD = 💰 Add balance
TEAMS-MCC-BALANCE-VALUE = 💵 Top-up amount:
TEAMS-MCC-BALANCE-VALUE-ERROR = ⚠️ Enter a number:
TEAMS-MCC-BALANCE-CONFIRMATION = 💵 Is the top-up amount <b>{$value}</b> correct?
TEAMS-MCC-BALANCE-CREATE-TRANSACTION = 🏦 Create transaction
TEAMS-MCC-BALANCE-TOPUP-SUCCESS = ✅ MCC successfully topped up for the team
TEAMS-MCC-BALANCE-TOPUP-TRANSACTION-FAIL = ❌ Failed to top up MCC for the team (<b>{$error}</b>)
#################
MCC-GENERAL-SWITCH = 🔄 General On/Off
################### CREATE ACCOUNT #########
ADMIN-ACCOUNT-CREATE = 🆕 Create account
ADMIN-ACCOUNT-CREATE-NAME = 🏷️ Enter the name:
ADMIN-ACCOUNT-CREATE-NAME-ERROR = ⚠️ The name must be up to 255 characters, currently <b>{$len}</b>
ADMIN-ACCOUNT-CREATE-TEAM = 🆔 Enter the team UUID:
ADMIN-ACCOUNT-CREATE-TEAM-ERROR = ❌ No team exists with this UUID
ADMIN-ACCOUNT-CREATE-TEAM-SKIP = ⏭️ Continue without a team
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_SKIP = ⏭️ Team skipped.
    ✉️ Enter email:
ADMIN-ACCOUNT-CREATE-EMAIL-TEAM_CHOiCED = ✅ Selected team (<b>{$team_name}</b>).
    ✉️ Enter email:
ADMIN-ACCOUNT-CREATE-AMOUNT = 💵 Top-up amount (min 50$):
ADMIN-ACCOUNT-CREATE-TIMEZONE = 🌐 Enter the time zone, UTC (from -12 to +14), enter a number, e.g., +12 or -3:
ADMIN-ACCOUNT-CREATE-TIMEZONE-ERROR = ⚠️ Invalid format. UTC (from -12 to +14), enter a number, e.g., +12 or -3:
ADMIN-ACCOUNT-CREATE-FAIL = ❌ Error creating account
    Error: <b>{$error}</b>
ADMIN-ACCOUNT-CREATE-SUCCESS = ✅ Account created successfully! Wait for it to appear in your accounts under the MCC (<b>{$mcc_name}</b>)
##########
ADMIN-ACCOUNT-NO_VERIFY_YET = ⏱️ The account is not yet verified, check back later
##################### CHANGE TEAM #################
ADMIN-ACCOUNT-CHANGE_TEAM = 🔄 Change team
ADMIN-ACCOUNT-CHANGE_TEAM-UUID = 🆔 Enter the team ID:
ADMIN-ACCOUNT-CHANGE_TEAM-EXIST = ℹ️ The team with this ID already has this account
ADMIN-ACCOUNT-CHANGE_TEAM-ERROR = ❌ No team exists with this ID
ADMIN-ACCOUNT-CHANGE_TEAM-SUCCESS = ✅ Successfully transferred to team <b>{$team_name}</b>
ADMIN-ACCOUNT-CHANGE_TEAM-FAIL = ❌ Failed to change the team for the account

#######################################
# Account (change email, refund, topup)
Change Email ###
ADMIN-ACCOUNT-CHANGE_EMAIL = ✉️ Change email
ADMIN-ACCOUNT-CHANGE_EMAIL-INPUT = ✉️ Enter the new email
ADMIN-ACCOUNT-CHANGE_EMAIL-FAIL = ❌ Failed to change email
ADMIN-ACCOUNT-CHANGE_EMAIL-ERROR = ⚠️ Invalid email format
ADMIN-ACCOUNT-CHANGE_EMAIL-SUCCESS = ✅ Email successfully changed to <b>{$email}</b>
# Refund ###
ADMIN-ACCOUNT-REFUND = 💸 Refund
ADMIN-ACCOUNT-REFUND-CONFIRMATION-WARNING = ❓ Are you sure you want to refund account <b>{$account_name}</b>?

    💵 The account balance (<b>{$balance}$</b>) will be refunded to the main MCC
ADMIN-ACCOUNT-REFUND-CONFIRMATION = ✅ Confirm refund
ADMIN-ACCOUNT-REFUND-FAIL = ❌ An error occurred. Failed to refund
ADMIN-ACCOUNT-REFUND-SUCCESS = ✅ Refund request successfully sent
# TopUp ###
ADMIN-ACCOUNT-TOPUP = 💳 Top up
ADMIN-ACCOUNT-TOPUP-VALUE = 💵 Enter the top-up amount from <b>50$</b>:
ADMIN-ACCOUNT-TOPUP-VALUE-ERROR = ⚠️ Enter a number between <b>50$</b> and <b>10,000$</b>:
ADMIN-ACCOUNT-TOPUP-WARNING = ❓ Top up the account balance by <b>{$value}$</b>?
ADMIN-ACCOUNT-TOPUP-BALANCE-ERROR = ⚠️ Insufficient balance on the account.
    Your balance: <b>{$balance}$</b>
    Top-up request: <b>{$value}$</b>
ADMIN-ACCOUNT-TOPUP-CONFIRMATION = ✅ Confirm top-up
ADMIN-ACCOUNT-TOPUP-FAIL = ❌ Error during top-up
ADMIN-ACCOUNT-TOPUP-SUCCESS = ✅ Successfully topped up
################################## Specific API Functions #################################
ADMIN-SPECIFIC = ⚙️ Additional
ADMIN-SPECIFIC-LOAD = 🔄 Load accounts
ADMIN-SPECIFIC-LOAD-WARNING = ⚠️ The process of loading new accounts from all added MCCs in the bot will now be initiated! Any accounts not already in the bot database will be added to the corresponding MCC.

    ❗ <b>Press only once, this is a resource-intensive process</b>
ADMIN-SPECIFIC-LOAD-CONFIRMATION = ✅ Confirm loading
ADMIN-SPECIFIC-LOAD-PROCESSING = ⏳ Loading started, it will take about 1-2 minutes
ADMIN-SPECIFIC-LOAD-RESULT = ✅ Successfully loaded new accounts: <b>{$new_accounts}</b>

    📊 {$statistic}
ADMIN-SPECIFIC-LOAD-FAIL = ❌ Error adding account <b>{$email}</b> to MCC <b>{$mcc_name}</b>
