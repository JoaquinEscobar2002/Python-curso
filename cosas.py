import pandas as pd
import random
import uuid
from faker import Faker

fake = Faker()
random.seed(42)

# Cantidad de registros
num_players = 10000
num_scores = 50000
num_reviews = 30000
 
# Juegos basados en títulos reales (75 únicos)
game_titles = [
    "The Legend of Zelda", "Super Mario Bros.", "Minecraft", "Fortnite", "Call of Duty",
    "League of Legends", "Counter-Strike", "Dota 2", "Grand Theft Auto V", "Red Dead Redemption 2",
    "Among Us", "Cyberpunk 2077", "Hollow Knight", "Dark Souls", "Elden Ring",
    "The Witcher 3", "Overwatch", "Valorant", "Rocket League", "Stardew Valley",
    "Animal Crossing", "Resident Evil", "Silent Hill", "Metal Gear Solid", "God of War",
    "Final Fantasy", "Pokemon", "World of Warcraft", "Hearthstone", "Diablo",
    "Battlefield", "FIFA", "NBA 2K", "Madden NFL", "Apex Legends",
    "Genshin Impact", "Tetris", "Dead by Daylight", "Horizon Zero Dawn", "Persona 5",
    "Half-Life", "Mass Effect", "Fallout", "Skyrim", "DOOM",
    "Celeste", "Cuphead", "Undertale", "Spelunky", "Portal",
    "Terraria", "The Sims", "Left 4 Dead", "Titanfall", "Death Stranding",
    "Sekiro", "Ghost of Tsushima", "Star Wars Jedi", "No Man's Sky", "Destiny",
    "Hitman", "Assassin's Creed", "Far Cry", "Borderlands", "Dragon Age",
    "Bloodborne", "Splatoon", "Fire Emblem", "Bayonetta", "Kirby",
    "Yakuza", "Nioh", "Xenoblade Chronicles", "Monster Hunter", "Crash Bandicoot"
]

# Géneros de juegos
game_genres = ["Acción", "Aventura", "RPG", "Shooter", "Estrategia", "Deportes", "Pelea", "Terror", "Simulación", "Carreras"]

# Equipos utilizados para jugar
equipment_types = ["PC", "Consola", "Móvil", "VR", "Arcade"]

# Tabla de jugadores
players = []
for _ in range(num_players):
    player_id = f"JUG-{uuid.uuid4().hex[:8]}"
    id_pc = f"PC-{uuid.uuid4().hex[:8]}"
    players.append([player_id, fake.name(), fake.email(), fake.phone_number(), id_pc, random.randint(10, 50), fake.country()])

df_players = pd.DataFrame(players, columns=["id_jugador", "nombre", "email", "telefono", "id_pc", "edad", "pais"])
df_players.to_csv("jugadores.csv", index=False)

# Tabla de hardware de PC
hardware_specs = ["Intel i7 + RTX 3070", "AMD Ryzen 5 + RX 6700", "Intel i9 + RTX 4090", 
                  "Apple M2 Max", "AMD Ryzen 7 + RTX 3080", "Intel i5 + GTX 1660", "Steam Deck", "Alienware R12"]
pcs = []
for id_pc in df_players["id_pc"].unique():
    pcs.append([id_pc, random.choice(hardware_specs), fake.date_this_decade()])

df_pcs = pd.DataFrame(pcs, columns=["id_pc", "especificaciones", "fecha_adquisicion"])
df_pcs.to_csv("hardware_pcs.csv", index=False)

# Tabla de juegos
games = []
for i in range(75):
    game_id = f"JUEGO-{i+1:03}"
    games.append([game_id, game_titles[i], random.choice(game_genres), random.randint(2000, 2025)])

df_games = pd.DataFrame(games, columns=["id_juego", "titulo", "genero", "anio_lanzamiento"])
df_games.to_csv("juegos.csv", index=False)

# Tabla de equipos requeridos por juegos
game_equipment = []
for game_id in df_games["id_juego"]:
    game_equipment.append([game_id, random.choice(equipment_types)])

df_game_equipment = pd.DataFrame(game_equipment, columns=["id_juego", "equipo_requerido"])
df_game_equipment.to_csv("equipos_juegos.csv", index=False)

# Tabla de niveles y puntajes
scores = []
for _ in range(num_scores):
    score_max = random.randint(5000, 100000)
    score_min = random.randint(0, score_max - 5000)
    scores.append([f"PUNT-{uuid.uuid4().hex[:8]}", random.choice(df_players["id_jugador"]), random.choice(df_games["id_juego"]),
                   random.randint(1, 100), random.randint(1, 200), random.randint(0, 100000), score_max, score_min, fake.date_this_decade()])

df_scores = pd.DataFrame(scores, columns=["id_puntaje", "id_jugador", "id_juego", "nivel", "horas_jugadas", "puntaje", "puntaje_maximo", "puntaje_minimo", "fecha"])
df_scores.to_csv("puntajes.csv", index=False)

# Tabla de comentarios y ratings
reviews = []
for _ in range(num_reviews):
    reviews.append([f"REV-{uuid.uuid4().hex[:8]}", random.choice(df_players["id_jugador"]), random.choice(df_games["id_juego"]),
                    random.randint(1, 5), fake.sentence(nb_words=10)])

df_reviews = pd.DataFrame(reviews, columns=["id_resena", "id_jugador", "id_juego", "calificacion", "comentario"])
df_reviews.to_csv("resenas.csv", index=False)

# Tabla de ventas y ganancias
sales = []
for game_id in df_games["id_juego"]:
    units_sold = random.randint(100000, 50000000)  # De 100k a 50M unidades vendidas
    revenue = units_sold * random.uniform(10, 70)  # Precio entre 10 y 70 dólares por unidad
    sales.append([game_id, units_sold, round(revenue, 2)])

df_sales = pd.DataFrame(sales, columns=["id_juego", "unidades_vendidas", "ganancias"])
df_sales.to_csv("ventas.csv", index=False)

print("✅ ¡Archivos generados con éxito!")
