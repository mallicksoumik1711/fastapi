from fastapi import FastAPI, Query, HTTPException
from models import MenuList, MenuResponse
from inMemoryData import lists

app = FastAPI(
    title="API Menus Lists",
    description="Just an basic api collection for finding menus"
)

@app.get("/")
def root():
    return lists


@app.get("/list-category", response_model=MenuResponse)
def get_list_catogory(category: str | None = Query(default=None)):
    if category:
        filtered = [list for list in lists if list["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No list found for category {category}")
        return MenuResponse(count=len(filtered), lists=filtered)

    return MenuResponse(count=len(lists), lists=lists)
                                        # from MenuResponse, and inMemoryData


@app.get("/dynamic-routing/{id}", response_model=MenuList)
def get_list_dynamic_routing(id: int):
    for list in lists:
        if list["id"] == id:
            return list

    raise HTTPException(status_code=404, detail=f"menu list not found for id {id}")