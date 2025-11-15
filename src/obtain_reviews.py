import requests

class ObtainReviews:
    ENDPOINT = "https://store.steampowered.com/appreviews/"
    def __init__(self):
        self.game_id = None

    def fetch_reviews(self):
        url = f"{self.ENDPOINT}{self.game_id}?json=1&language=english&review_type=all&num_per_page=100"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            reviews = data.get('reviews', [])
            for review in reviews:
                print(review['review'])
        else:
            raise Exception(f"Failed to fetch reviews: {response.status_code}")