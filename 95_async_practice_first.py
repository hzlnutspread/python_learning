import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            return text, url
    except Exception as e:
        print(str(e))


async def main():
    tasks = []
    html_array = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))

        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            html_array.append(html)
            print("_"*50)
            print("_"*50)
            print("_"*50)

        for i in range(len(html)):
            soup = BeautifulSoup(html[i], 'lxml')
            # soup.find('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
            # date = soup.find('div', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0').text
            print(soup)



asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
urls = ['https://twitter.com/flufworld', 'https://twitter.com/seekers_xyz']
asyncio.run(main())
