# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/24 
# Desc:

import arrow
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient # mongodb 的异步实现
MONGO_URI = 'mongodb://mongouser:597a1f38d863c780@140.143.58.134:1234/admin'
client = AsyncIOMotorClient(MONGO_URI)
rank_db = client.rank_data # 数据库


async def fetch_huobi_price(start, end=None, db=rank_db): # # 从mongodb取数
    coll = db.huobi_spot_otc_price # 表
    query = {
        "created": {"$gte": start},
        "coin_name": {"$in": ['BTC', 'ETH', 'USDT']}
    }
    if end:
        assert isinstance(end, datetime), 'end must be instance of datetime'
        query['created']['$lte'] = end
    async for item in coll.find(query).sort('created', 1):
        yield item
