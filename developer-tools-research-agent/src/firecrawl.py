import os
from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()

class FirecrawlService():
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables")
        self.app = FirecrawlApp(api_key=api_key)
    
    # searching like searching on the web
    def search_companies(self, query:str, num_results:int=5):
        try:
            result = self.app.search(
                query = f"{query} company pricing",
                limit=num_results,
                scrape_options = ScrapeOptions(
                    formats = ["markdown"]
                )
            )
            return result
        except Exception as e:
            print(e)
            return []
    
    # When if you want to scrape a single page, you already know the website that you want to get the content from.
    # Scraping the website, you give it the URL and it goes and extracts all of the content for you.
    def scrape_company_pages(self, url:str):
        try:
            result = self.app.scrape_url(
                url,
                formats = ["markdown"]
            )
            return result
        except Exception as e:
            print(e)
            return None
        
        