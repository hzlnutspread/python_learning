from bs4 import BeautifulSoup
import aiohttp
import pandas as pd
import requests
import asyncio


class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        self.all_data = []
        self.master_dict = {}
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.main())

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                text = await response.text
                return text, url
        except Exception as e:
            print(str(e))

    # async def extract_title_tag(self, text):
    #     try:
    #         soup = BeautifulSoup(text, 'html.parser')
    #         return soup.title
    #     except Exception as e:
    #         print(str(e))

    async def main(self):
        tasks = []
        headers = {
            "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            for html in htmls:
                if html is not None:
                    url = html[1]
                    self.master_dict[url] = {'Raw HTML': html[0]}
                else:
                    continue


urls = ['https://twitter.com/flufworld', 'https://twitter.com/seekers_xyz']
scraper = WebScraper(urls=urls)