class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "int | Distance") -> "Distance":
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        return Distance(self.km + other_km)

    def __iadd__(self, other: "int | Distance") -> "Distance":
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        self.km += other_km
        return self

    def __mul__(self, other: "int | Distance") -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: "int | Distance") -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "int | Distance") -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        return self.km < other_km

    def __gt__(self, other: "int | Distance") -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        return self.km > other_km

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        return self.km == other_km

    def __le__(self, other: "int | Distance") -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        return self.km <= other_km

    def __ge__(self, other: "int | Distance") -> bool:
        if isinstance(other, Distance):
            other_km = other.km
        else:
            other_km = other
        return self.km >= other_km
