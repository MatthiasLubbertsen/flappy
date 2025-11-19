import random

def handler(request):
    # 50/50 kans op up of down
    if random.choice([True, False]):
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": "Site is UP"
        }
    else:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "text/plain"},
            "body": "Site is DOWN"
        }
      
