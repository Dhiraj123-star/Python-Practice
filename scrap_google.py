import httpx
import asyncio
from bs4 import BeautifulSoup

async def get_organic_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4703.0 Safari/537.36"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.google.com/search?q=python+tutorial&gl=us&hl=en", headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        organic_results =[]

        i = 0

        for el in soup.select(".g"):
            organic_results.append({
                "title": el.select_one("h3").text,
                "link": el.select_one(".yuRUbf > a")["href"],
                "description": el.select_one(".VwiC3b").text,
                "rank": i+1
            })

            i+=1    

        print(organic_results)


asyncio.run(get_organic_data())
