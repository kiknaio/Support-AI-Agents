from crewai.tools import BaseTool
from crewai_tools import ScrapeWebsiteTool
from typing import Type
from pydantic import BaseModel, Field


class ReactDocsScraperInput(BaseModel):
    """Input schema for ReactDocsScraper."""
    argument: str = Field(..., description="Description of the argument.")

class ReactDocsScraper(BaseTool):
    name: str = "React Documentation Scraper"
    description: str = (
        "Scrape the React docs website for the latest information and updates."
    )
    args_schema: Type[BaseModel] = ReactDocsScraperInput

    def _run(self, argument: str) -> str:
        scraper = ScrapeWebsiteTool(website_url="https://react.dev/learn")
        result = scraper.run()
        return result
