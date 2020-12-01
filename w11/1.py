import asyncio
import aiohttp


async def get_response(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            return html


async def main(n = 100): 
    responses = [await get_response('http://127.0.0.1:8000') for i in range(n)]
    print(*responses)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(100))
loop.close()
