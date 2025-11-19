import random

def main(request):
    if random.choice([True, False]):
        return {
            "status": 200,
            "body": "Site is UP"
        }
    else:
        return {
            "status": 500,
            "body": "Site is DOWN"
        }

# Vercel kijkt naar een exported 'handler' of 'app' — wijs die hier naar onze main functie.
handler = main
app = main
