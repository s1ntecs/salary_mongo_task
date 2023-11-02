from datetime import datetime, timedelta
from typing import Dict, List

from motor.core import AgnosticLatentCommandCursor


class MongoQueries():

    def __init__(self,
                 group_type: str,
                 dt_from: str,
                 dt_upto: str) -> None:
        self.group_type: str = group_type
        self.end_date: datetime = datetime.fromisoformat(dt_upto)
        self.cur_start_dt: datetime = datetime.fromisoformat(dt_from)
        self.cur_end_dt: datetime = datetime.fromisoformat(dt_upto)
        self.pipeline: List = []
        self.results: Dict[str, List] = {"dataset": [], "labels": []}

    def add_date(self) -> List:
        self.pipeline = []
        match self.group_type:
            case "hour":
                self.cur_end_dt = (
                    self.cur_start_dt if self.cur_start_dt == self.end_date
                    else self.cur_start_dt + timedelta(hours=1)
                )

                self.pipeline.extend([
                    {
                        "$match": {
                            "dt": {
                                "$gte": self.cur_start_dt,
                                "$lt": self.cur_end_dt
                                }
                        }
                    }
                ])
            case "day":
                self.next_day()
                self.pipeline.extend([
                    {
                        "$match": {
                            "dt": {
                                "$gte": self.cur_start_dt,
                                "$lt": self.cur_end_dt
                            }
                        }
                    }
                ])
            case "month":
                self.next_month()
                self.pipeline.extend([
                    {
                        "$match": {
                            "dt": {
                                "$gte": self.cur_start_dt,
                                "$lt": self.cur_end_dt
                            }
                        }
                    }
                ])
        self.pipeline.extend([
            {
                "$group": {
                    "_id": None,
                    "totalValue": {"$sum": "$value"}
                }
            }
        ])

    async def parse_data(self,
                         cursor: AgnosticLatentCommandCursor):
        date = self.cur_start_dt.strftime("%Y-%m-%dT%H:00:00")
        data_exists = False
        async for result in cursor:
            data_exists = True
            total_value = result["totalValue"]
            self.results["dataset"].append(total_value)
            self.results["labels"].append(date)
        if not data_exists:
            self.results["dataset"].append(0)
            self.results["labels"].append(date)
        self.next_period()

    def next_period(self):
        match self.group_type:
            case "hour":
                self.cur_start_dt = self.cur_start_dt + timedelta(hours=1)
            case "day":
                self.cur_start_dt = self.cur_start_dt + timedelta(days=1)
            case "month":
                self.cur_start_dt = self.cur_end_dt

    def next_month(self):
        if self.cur_start_dt.month == 12:
            self.cur_end_dt = self.cur_start_dt.replace(
                day=1, month=1, year=self.cur_start_dt.year + 1)
        else:
            self.cur_end_dt = self.cur_start_dt.replace(
                day=1, month=self.cur_start_dt.month + 1)

    def next_day(self):
        if (self.cur_start_dt + timedelta(days=1)) > self.end_date:
            self.cur_end_dt = self.end_date
        else:
            self.cur_end_dt = self.cur_start_dt + timedelta(days=1)
