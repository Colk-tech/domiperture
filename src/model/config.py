import random


TEMPERATURE_RANGE = (36.1, 36.6)


class UserObject:
    def __init__(self, url_template, building, room_number, name):
        self.url_template = url_template
        self.temperature_range = TEMPERATURE_RANGE
        self.building = building
        self.room_number = room_number
        self.name = name

    def generate_url(self):
        body_temperature: float = round(random.uniform(self.temperature_range[0], self.temperature_range[1]), 1)

        result = self.url_template.format(
            building=self.building,
            room_number=self.room_number,
            name=self.name,
            body_temperature=body_temperature)

        return result
