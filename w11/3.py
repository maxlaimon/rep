import aiohttp
import asyncio
import aiofile

async def get_response(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            html = await response.text()
            lines = html.split('\n')
            async with aiofile.AIOFile("found.txt", 'w') as found:
                for line in lines:
                    if line.startswith("<>"):
                        found.write(line)

async def go_url(urls):
    
