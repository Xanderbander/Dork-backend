
from fastapi import FastAPI, HTTPException
from dork_generation import generate_dork
from web_scraping import Scraper
from config import api_key

app = FastAPI()
scraper = Scraper(api_key)

@app.get("/generate_dork")
def get_dork(pattern: str):
    return {"dork": generate_dork(pattern)}

@app.get("/search")
def search_dork(dork: str):
    response = scraper.search(dork)
    if not response:
        raise HTTPException(status_code=404, detail="No results found")
    return {"results": response}

@app.get("/documents")
def get_documents():
    # This function will return stored document data
    return {"documents": "List of stored documents"}
