
from google.adk import Agent
from google.adk.tools import google_search
from firecrawl import AsyncFirecrawlApp
from dotenv import load_dotenv
from google.genai import types
import os
import unicodedata
import re

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

def slugify(value: str) -> str:
    value = value.lower()
    # Normaliza y elimina acentos (ñ queda como ñ)
    value = unicodedata.normalize('NFD', value)
    value = ''.join(c for c in value if unicodedata.category(c) != 'Mn')
    # Reemplaza cualquier cosa que no sea alfanumérica por guiones
    value = re.sub(r'[^a-z0-9]+', '-', value)

    value = value.strip('-')

    return value

def limpiar_texto(texto):
    palabras = texto.split()
    resultado = []

    for i in range(len(palabras)):
        palabra = palabras[i]
        # Remueve caracteres especiales
        palabra_limpia = re.sub(r"[^\w\s]", "", palabra)
        # Descarta palabras de un solo caracter (excepto si es una letra mayúscula como "I")
        if (i != 0 or i != len(palabras) - 1) and len(palabra_limpia) == 1 and not palabra_limpia.isupper():
            continue

        resultado.append(palabra_limpia)

    return ' '.join(resultado)

async def get_guitar_tabs_and_chords(artist: str = '', song:str = '') -> str:
    """
    Get guitar tabs and chord progressions.
    Parameters:
        artist (str): The artist name
        song (str): The song name
    Returns:
        str: The guitar tab and chord progression for the given artist and song
    """
    print(f"artist: {artist}")
    print(f"song: {song}")
    song_to_slugify = limpiar_texto(song)
    artist_to_slugify = limpiar_texto(artist)

    print(f"artist_to_slugify: {artist_to_slugify}")
    print(f"song_to_slugify: {song_to_slugify}")

    artist_slugify = slugify(artist_to_slugify)
    song_slugify = slugify(song_to_slugify)

    print(f"artist_slugify: {artist_slugify}")
    print(f"song_slugify: {song_slugify}")
    url = f"https://www.cifraclub.com/{artist_slugify}/{song_slugify}/"

    print(f"url: {url}")

    app = AsyncFirecrawlApp(api_key=FIRECRAWL_API_KEY)
    response = await app.scrape_url(
        url=url,		
        formats= [ 'markdown' ],
        only_main_content= True,
        include_tags= [ '.cifra-column--left' ]
    )

    return response.markdown

