# media_engine.py

def even_square_generator(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2

def run_analytics(limit):
    counts = list(even_square_generator(limit))
    total_plays = sum(counts)
    num_records = len(counts)
    return total_plays, num_records, counts

def play_media(artist):
    print(f"Now playing tracks from {artist}")