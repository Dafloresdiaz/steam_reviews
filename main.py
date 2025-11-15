from src.obtain_reviews import ObtainReviews as review

if __name__ == "__main__":
    obtain_review = review()
    obtain_review.game_id = 2592160
    obtain_review.fetch_reviews()