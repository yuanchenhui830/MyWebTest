#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, aiomysql, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    return web.Response(body='<h1>I love you</h1>',content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

def test_example():
    aiomysql.create_pool
    conn = yield from aiomysql.connect(host='10.10.10.130', port=3306,
                                       user='root', password='telek001',
                                       db='PD', loop=loop)
    cursor = yield from conn.cursor()
    yield from cursor.execute("SELECT usercode FROM user")
    r = yield from cursor.fetchall()
    print(r)
    yield from cursor.close()
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))

loop.run_forever()