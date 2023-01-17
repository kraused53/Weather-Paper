import geocoder


def get_location():
    location_data = geocoder.ip('me')
    return [
        str(location_data.city),
        str(location_data.state),
        str(location_data.lat),
        str(location_data.lng)
    ]