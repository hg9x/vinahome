#!/usr/bin/python3
#
# Copyright (c) 2017-2018, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the ASL 2.0 license. See LICENSE.md file for details.
#
import asyncio
import json

import asyncws

ACCESS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjZWZiM2MyNTdlMDg0ODgxODFlZTFiMTE1NzM5ZmFmNyIsImlhdCI6MTU1ODM2Nzc0OCwiZXhwIjoxODczNzI3NzQ4fQ.3onRJpJSczNXHRVTgSJchV6CfW08TIvBJ2JM_ktvYtc'

async def main():
    print("""Simple WebSocket client for Home Assistant.""")
    websocket = await asyncws.connect('ws://192.168.9.138:8123/api/websocket')
    print('asdasdas')
    await websocket.send(json.dumps(
        {'type': 'auth',
         'access_token': ACCESS_TOKEN}
    ))

    await websocket.send(json.dumps(
        {'id': 18, 'type': 'subscribe_events', 'event_type': 'state_changed'}
    ))

    while True:
        message = await websocket.recv()
        if message is None:
            print('dm')
            break
        print (message)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()