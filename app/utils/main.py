from app.databases import postgre_repo


def get_show_reviews(title):
    reviews = postgre_repo.get_show_reviews(title)
    show_avg_reviews_rating = sum(map(lambda x: x.rating, reviews)) / len(reviews) if len(reviews) else 0
    show_reviews_count = len(reviews)
    reviews = reviews[:5]
    show_reviews = {
        'avg_rating': float(show_avg_reviews_rating),
        'count': int(show_reviews_count),
        'reviews': reviews
    }

    return show_reviews
