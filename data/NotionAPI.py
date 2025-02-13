import asyncio

from notion_client import Client

from data.repositories.sub_accounts_mcc import SubAccountRepository
from data.repositories.taxes import TaxRepository
from private_config import NOTION_SECRET, NOTION_DATABASE_ID_ACCOUTNS


class NotionAPI:
    def __init__(self):
        self.notion = Client(auth=NOTION_SECRET)

    async def __is_unique(self, identifier: str):
        query = self.notion.databases.query(
            database_id=NOTION_DATABASE_ID_ACCOUTNS,
            filter={
                "property": "account uid",
                "rich_text": {
                    "equals": identifier
                }
            }
        )
        return len(query['results']) == 0

    async def add_to_notion(self, data: dict):
        try:
            if not await self.__is_unique(data['account_uid']):
                return False

            self.notion.pages.create(
                parent={"database_id": NOTION_DATABASE_ID_ACCOUTNS},

                properties={
                    "account email": {"title": [{"text": {"content": data['account_email']}}]},
                    "account name": {"rich_text": [{"text": {"content": data['account_name']}}]},
                    "account uid": {"rich_text": [{"text": {"content": data['account_uid']}}]},
                    "mcc uuid": {"rich_text": [{"text": {"content": data['mcc_uuid']}}]},
                    "account timezone": {"rich_text": [{"text": {"content": data['account_timezone']}}]},
                    "team uuid": {"rich_text": [{"text": {"content": data['team_uuid']}}]},
                    "team name": {"rich_text": [{"text": {"content": data['team_name']}}]},
                    "created": {"date": {"start": data['created'].isoformat()}},
                }
            )
            return True
        except Exception as e:
            print(f"add to notion with error: {e}")
            return False


async def start():
    notion = NotionAPI()
    for tax in SubAccountRepository().all_accounts():
        await notion.add_to_notion(tax)


asyncio.run(start())
