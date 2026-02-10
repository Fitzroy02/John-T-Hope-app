def calculate_points_and_saplings(spend, point_value=500, points_per_sapling=20):
    points = spend / point_value
    saplings = points / points_per_sapling
    return int(points), saplings