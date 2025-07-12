from colorthief import ColorThief
import requests
import io

img_url = "https://i.scdn.co/image/ab67616d0000b273d9194aa18fa4c9362b47464f"  # PlaceHolder
img_data = requests.get(img_url).content

color_thief = ColorThief(io.BytesIO(img_data))
dominant_color = color_thief.get_color(quality=1)

print(f"Dominant color: {dominant_color}")