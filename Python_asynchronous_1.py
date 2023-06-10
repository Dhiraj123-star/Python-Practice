import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://www.yahoo.com',
        'https://www.google.com',
        'https://www.openai.com'
    ]
    tasks = []

    for url in urls:
        tasks.append(fetch_url(url))

    results = await asyncio.gather(*tasks)
    for url, result in zip(urls, results):
        print(f"Response from {url}: {result[:100]}")

if __name__=="__main__":
    asyncio.run(main())