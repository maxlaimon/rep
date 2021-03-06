import aiohttp
import asyncio
import aiofile

async def fetch(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            return html


async def find_line(text):
    lines = text.split(r'\n')
    async with aiofile.AIOFile("found.txt", 'w') as found:
        for line in lines:
            if line.startswith("<a >"):
                await found.write(line)


async def seeker(file):
    async with aiofile.AIOFile(file, 'r') as urls:
        texts = []
        async for url in aiofile.LineReader(urls):
            texts.append(fetch(url))
        await asyncio.gather(*texts)


loop = asyncio.get_event_loop()
loop.run_until_complete(seeker("urls.txt"))

