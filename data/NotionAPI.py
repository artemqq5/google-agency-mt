# from notion_client import Client
#
# # from private_config import NOTION_SECRET, NOTION_DATABASE_ID
#
#
# class NotionAPI:
#     def __init__(self):
#         self.notion = Client(auth=NOTION_SECRET)
#
#     async def __is_unique(self, identifier: str):
#         query = self.notion.databases.query(
#             database_id=NOTION_DATABASE_ID,
#             filter={
#                 "property": "transaction_uuid",
#                 "rich_text": {
#                     "equals": identifier
#                 }
#             }
#         )
#         return len(query['results']) == 0
#
#     async def add_to_notion(self, data: dict):
#         try:
#             if not await self.__is_unique(data['transaction_uuid']):
#                 return False
#
#             self.notion.pages.create(
#                 parent={"database_id": NOTION_DATABASE_ID},
#
#                 properties={
#                     "email": {"title": [{"text": {"content": data['team_name']}}]},
#                     "mcc name": {"rich_text": [{"text": {"content": data['mcc_name']}}]},
#                     "mcc uuid": {"rich_text": [{"text": {"content": data['mcc_uuid']}}]},
#                     "team uuid": {"rich_text": [{"text": {"content": data['team_uuid']}}]},
#                     "transaction uuid": {"rich_text": [{"text": {"content": data['transaction_uuid']}}]},
#                     "kind": {"rich_text": [{"text": {"content": data['kind']}}]},
#                     "amount": {"number": data['amount']},
#                     "currency": {"rich_text": [{"text": {"content": data['currency']}}]},
#                     "status": {"rich_text": [{"text": {"content": data['status']}}]},
#                     "client link": [{"text": {"content":  data['client_link']}}],
#                     "desc": {"rich_text": [{"text": {"content": data['desc']}}]},
#                     "date": {"date": {"start": data['date']}},
#                 }
#             )
#             return True
#         except Exception as e:
#             print(f"add to notion with error: {e}")
#             return False
