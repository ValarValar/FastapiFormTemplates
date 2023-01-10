import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from core.config import Settings


def get_settings():
    return Settings()


settings = get_settings()

template = {
    "form_name": "Form template name",
    "template": {
        "username": "text",
        "user_email": "email",
        "user_phone": "phone",
        "user_registration_date": "date",
        "user_phone2": "phone",
    }
}

mongodb_client = AsyncIOMotorClient('mongodb://localhost:27017')
mongodb = mongodb_client[settings.MONGODB_DATABASE]
mongodb_collection = mongodb[settings.MONGODB_COLLECTION]
print(mongodb_collection)


async def insert_template(template: dict):
    new_task = await mongodb[settings.MONGODB_COLLECTION].insert_one(template)
    created_task = await mongodb[settings.MONGODB_COLLECTION].find_one(
        {"_id": new_task.inserted_id}
    )
    return created_task


input_obj = {
    "username": "text",
    "user_email": "email",
    "user_phone": "phone",
    "user_registration_date": "date",
    'user_phone2': 'phone',

}


async def find_suitable_form_template(input_fields: dict):
    """
    :param input_fields:
    :return:
    """
    cursor = mongodb_collection.aggregate([
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
                "Name": 1,
                "template": 1
            }
        }
    ])
    results = await cursor.to_list(length=1)
    return results


async def main():
    task1 = asyncio.create_task(insert_template(template))
    await task1


asyncio.run(main())
