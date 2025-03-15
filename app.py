from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from processing import movies, cv, cosine_sim, get_movie_index, get_movie_title

app = FastAPI()
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Define the model for the input data
class MovieRequest(BaseModel):
    title: str

# Path to your HTML file
HTML_FILE_PATH = "C:/Users/asrah/Desktop/mrs_proj/index.html"

@app.get("/", response_class=HTMLResponse)
async def get_html():
    """Serve the HTML file"""
    # Read the HTML file from disk
    with open(HTML_FILE_PATH, "r") as file:
        html_content = file.read()
    
    return HTMLResponse(content=html_content, status_code=200)
@app.post("/recommend")
async def recommend(request: MovieRequest):
    title = request.title
    movie_index = get_movie_index(title)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    recommendations = []
    for i, movie in enumerate(sorted_similar_movies):
        if i >= 15:
            break
        recommendations.append(get_movie_title(movie[0]))
    return JSONResponse(content={"recommendations": recommendations})

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="localhost",
        port=8000,
        reload=True
    )