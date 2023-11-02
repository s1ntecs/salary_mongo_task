from typing import Dict
from motor.motor_asyncio import AsyncIOMotorClient
from mongo_query import MongoQueries
from const import DATABASE_URL, ERROR_MSG


async def aggregate_payments(dt_from: str,
                             dt_upto: str,
                             group_type: str) -> Dict:
    """
    Функция считает сумму всех выплат за период
    c dt_from по dt_upto и группирует по group_type
    """

    client = AsyncIOMotorClient(DATABASE_URL)
    db = client["mongo"]
    collection = db["sample_collection"]
    try:
        aggregation_pipeline = MongoQueries(group_type=group_type,
                                            dt_from=dt_from,
                                            dt_upto=dt_upto)
    except Exception:
        return ERROR_MSG
    while aggregation_pipeline.cur_start_dt <= aggregation_pipeline.end_date:
        aggregation_pipeline.add_date()
        cursor = collection.aggregate(aggregation_pipeline.pipeline)
        await aggregation_pipeline.parse_data(cursor)
    return aggregation_pipeline.results
