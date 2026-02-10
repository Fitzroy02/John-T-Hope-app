from datetime import datetime, timedelta

def get_music_status(release_date):
    """
    Music:
    - 4 week promotion period BEFORE release
    - 2 week availability AFTER release
    - 12 week blackout after availability
    """
    now = datetime.now()
    promo_start = release_date - timedelta(weeks=4)
    available_end = release_date + timedelta(weeks=2)
    blackout_end = available_end + timedelta(weeks=12)

    if now < promo_start:
        return "Not yet in promotion", (promo_start - now).days
    elif promo_start <= now < release_date:
        return "In promotion", (release_date - now).days
    elif release_date <= now < available_end:
        return "Available", (available_end - now).days
    elif available_end <= now < blackout_end:
        return "Blackout", (blackout_end - now).days
    else:
        return "Returns soon", None

def get_film_status(release_date):
    """
    Films:
    - 4 week promotion period BEFORE release
    - Available for release week (you can extend)
    - 6 month blackout
    """
    now = datetime.now()
    promo_start = release_date - timedelta(weeks=4)
    available_end = release_date + timedelta(weeks=1)
    blackout_end = release_date + timedelta(weeks=26)

    if now < promo_start:
        return "Not yet in promotion", (promo_start - now).days
    elif promo_start <= now < release_date:
        return "In promotion", (release_date - now).days
    elif release_date <= now < available_end:
        return "Available", (available_end - now).days
    elif available_end <= now < blackout_end:
        return "Blackout", (blackout_end - now).days
    else:
        return "Returns soon", None

def get_early_access_status(release_date, days_before=7):
    now = datetime.now()
    early_start = release_date - timedelta(days=days_before)

    if early_start <= now < release_date:
        return "Early access", (release_date - now).days
    elif now < early_start:
        return "No early access yet", (early_start - now).days
    else:
        return "Early access ended", None
