class Cafe:
    def __init__(
        self,
        cafe_name,
        location_url,
        open_time,
        closing_time,
        coffee_rating,
        wifi_rating,
        power_outlet_rating,
    ) -> None:
        self.cafe_name = cafe_name
        self.location_url = location_url
        self.open_time = open_time
        self.closing_time = closing_time
        self.coffee_rating = coffee_rating
        self.wifi_rating = wifi_rating
        self.power_outlet_rating = power_outlet_rating
