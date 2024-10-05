from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
import json
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

def load_links():
    with open('links.json', 'r') as f:
        return json.load(f)

# Save LINKS to JSON file
def save_links(links):
    with open('links.json', 'w') as f:
        json.dump(links, f)


LINKS = load_links()

@app.get("/go/{rest:path}")
async def golink(request: Request, rest: str):
    path_list = rest.split("/")

    if path_list[0] == "links":
        return JSONResponse(LINKS)
    elif path_list[0] == "cp":
        with open("static/cp.html", "r") as f:
            return HTMLResponse(f.read())
    else:
        link_dict = LINKS
        for path in path_list[:-1]:
            link_dict = link_dict.get(path, {})

        link = link_dict.get(path_list[-1])
        logging.info(f"Redirecting to {link}.")

        return RedirectResponse(link, status_code=302)

@app.post("/go/cp/add")
async def add_link(request: Request):
    data = await request.json()
    key, value = data['key'], data['value']
    LINKS[key] = value
    save_links(LINKS)
    return JSONResponse({"message": f"Added link: {key} -> {value}"})

@app.put("/go/cp/update")
async def update_link(request: Request):
    data = await request.json()
    key, value = data['key'], data['value']
    if key not in LINKS:
        raise HTTPException(status_code=404, detail="Link not found")
    LINKS[key] = value
    save_links(LINKS)
    return JSONResponse({"message": f"Updated link: {key} -> {value}"})

@app.delete("/go/cp/delete/{key}")
async def delete_link(key: str):
    if key not in LINKS:
        raise HTTPException(status_code=404, detail="Link not found")
    del LINKS[key]
    save_links(LINKS)
    return JSONResponse({"message": f"Deleted link: {key}"})

