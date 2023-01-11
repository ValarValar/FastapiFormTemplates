import asyncio
from typing import Union

from motor.motor_asyncio import AsyncIOMotorClient

from core.config import get_settings

settings = get_settings()


class MongoDbService:
    def __init__(self, mongo_url: str):
        self.mongodb_client = AsyncIOMotorClient(settings.MONGODB_DOCKER_URL)
        # self.mongodb_client.get_io_loop = asyncio.get_running_loop
        self.mongodb = self.mongodb_client[settings.MONGODB_DATABASE]
        self.form_template_collection = self.mongodb[settings.MONGODB_COLLECTION]

    async def __insert_templates_task(self, templates: list[dict]):
        await self.form_template_collection.insert_many(templates)

    def insert_templates(self, templates: list[dict]):
        asyncio.get_event_loop().run_until_complete(self.__insert_templates_task(templates))

    async def find_suitable_form_template_task(self, input_fields: dict) -> Union[None, str]:
        """
        :param input_fields:
        :return:
        """
        cursor = self.form_template_collection.aggregate([
            {
                "$addFields": {
                    "rawInput": {
                        "$objectToArray": input_fields
                    }
                }
            },
            {
                "$match": {
                    "$expr": {
                        "$eq": [
                            {
                                "$size": {
                                    "$filter": {
                                        "input": {
                                            "$objectToArray": "$template"
                                        },
                                        "as": "elem",
                                        "cond": {
                                            "$not": {
                                                "$in": [
                                                    "$$elem",
                                                    "$rawInput"
                                                ]
                                            }
                                        }
                                    }
                                }
                            },
                            0
                        ]
                    }
                }
            },
            {
                "$project": {
                    "Form template name": 1,
                    "template": 1
                }
            }
        ])
        mongo_result = await cursor.to_list(length=1)
        try:
            return mongo_result[0]['Form template name']
        except IndexError:
            return None


def get_mongodb_service(mongo_url: str = settings.MONGODB_DOCKER_URL) -> MongoDbService:
    return MongoDbService(mongo_url)
