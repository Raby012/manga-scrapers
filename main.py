import requests
from fastapi import FastAPI, Response

from src.asurascans import Asurascans
from src.mangapill import Mangapill

app = FastAPI()


@app.get("/")
def homepage():
    return {
        "message": "Welcome to the manga scrapers API",
        "available_providers": ["mangapill", "asurascans"],
    }


@app.head("/")
async def read_root_head():
    return Response(headers={"Custom-Header": "Value"})


# Mangapill
@app.get("/mangapill/{category}/{path:path}")
def mangapill(category: str, path: str):
    if category == "search":
        return Mangapill().search(query=path)
    elif category == "info":
        return Mangapill().info(id=path)
    elif category == "pages":
        return Mangapill().pages(id=path)
    elif category == "newest":
        return Mangapill().new()
    elif category == "recent":
        return Mangapill().recent()
    elif category == "images":
        if path:
            headers = {"Referer": "https://mangapill.com/"}
            content = requests.get(url=path, headers=headers).content
            return Response(content=content, media_type="image/jpg")
        else:
            return {"detail": "image url is required"}
    else:
        return {"detail": "Invalid parameter"}


# Asurascans
@app.get("/asurascans/{category}/{path:path}")
def asurascans(category: str, path: str):
    if category == "search":
        if path:
            newQuery = path.replace(" ", "+")
            return Asurascans().search(query=newQuery)
    elif category == "info":
        return Asurascans().info(id=path)
    elif category == "pages":
        return Asurascans().pages(id=path)
    elif category == "popular":
        return Asurascans().popular()
    elif category == "latest":
        return Asurascans().latest(page=path)
    elif category == "genres":
        return Asurascans().genres(type=path)
    elif category == "genre-list":
        return {
            "endpoint": "asurascans",
            "genres": "action, adventure, comedy, romance",
        }
    else:
        return {"detail": "Invalid parameter"}
