from datetime import datetime

FILMS = [
    {
        "id": "silent-path",
        "title": "The Silent Path",
        "artist": "Aiko Tanaka",
        "genre": "Drama",
        "release_date": datetime(2026, 3, 1),
        "country": "Japan",
        "runtime": "1h 42m",
        "synopsis": "A minimalist exploration of grief, memory, and quiet spaces.",
        "event": "Tokyo Release Party – 28 February 2026",
    },
    {
        "id": "night-train-oslo",
        "title": "Night Train to Oslo",
        "artist": "Jonas Ravn",
        "genre": "Drama",
        "release_date": datetime(2026, 3, 12),
        "country": "Norway",
        "runtime": "1h 55m",
        "synopsis": "A contemplative journey through isolation and landscape.",
        "event": "Oslo Premiere – 10 March 2026",
    },
]

MUSIC = [
    {
        "id": "dust-honey",
        "title": "Dust & Honey",
        "artist": "Marisol Vega",
        "release_date": datetime(2026, 4, 5),
        "genre": "Folk/Electronic",
    },
]

ARTISTS = {
    "Aiko Tanaka": {
        "bio": "Japanese filmmaker known for minimalist emotional storytelling.",
        "works": ["silent-path"]
    },
    "Jonas Ravn": {
        "bio": "Norwegian director exploring isolation and landscape.",
        "works": ["night-train-oslo"]
    },
    "Marisol Vega": {
        "bio": "Latin American singer blending folk and electronic textures.",
        "works": ["dust-honey"]
    },
}
