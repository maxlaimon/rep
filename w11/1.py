import asyncio
import aiohttp


async def get_resp(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            return html



loop = asyncio.get_event_loop()
resps = [get_resp('http://127.0.0.1:8000') for _ in range(100)]
done = loop.run_until_complete(asyncio.gather(*resps))
loop.close()
print(*done)
