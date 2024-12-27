from notion_client import Client

from private_config import NOTION_SECRET, NOTION_DATABASE_ID


class NotionAPI:
    def __init__(self):
        self.notion = Client(auth=NOTION_SECRET)

    async def is_unique(self, identifier: str):
        query = self.notion.databases.query(
            database_id=NOTION_DATABASE_ID,
            filter={
                "property": "Unique ID",
                "rich_text": {
                    "equals": identifier
                }
            }
        )
        return len(query['results']) == 0

    async def add_to_notion(self, data: dict):
        try:
            self.notion.pages.create(
                parent={"database_id": NOTION_DATABASE_ID},
                properties={
                    "Name": {"title": [{"text": {"content": data['name']}}]},
                    "Email": {"email": data['email']},
                    "Amount": {"number": data['amount']},
                    "Date": {"date": {"start": data['date']}},
                }
            )
            return True
        except Exception as e:
            print(f"add to notion with error: {e}")
            return False
