from pylibdmtx.pylibdmtx import decode
from PIL import Image

def get_gtin_from_decode(image: str) -> str:
    try:
        result = decode(Image.open(image))
        decoded_data = str(result[0].data)
        gtin = decoded_data[5:18]
    except:
        return None

    return gtin