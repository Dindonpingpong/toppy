from http.client import HTTPException
from fastapi import FastAPI, File, UploadFile
import uuid

from app.matrix_decoder import get_gtin_from_decode

app = FastAPI()

@app.post("/gtin/")
async def create_upload_file(file: UploadFile = File(...)):

    path = f"tmp_images/{str(uuid.uuid4())}"

    with open(path, "wb+") as file_object:
        file_object.write(file.file.read())

    gtin = get_gtin_from_decode(path)

    if gtin is None:
        raise HTTPException(status=404, message="not found gtin in this photo")

    return {
        "gtin": gtin,
    }
