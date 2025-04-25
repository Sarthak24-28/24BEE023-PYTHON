class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes %= 60

    def __add__(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def __sub__(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total_seconds)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)


time1 = Time(2, 45, 30)
time2 = Time(1, 30, 45)

result_add = time1 + time2

result_sub = time1 - time2

print(f"Time 1:",time1)
print(f"Time 2:",time2)
print(f"Addition Result:",result_add)
print(f"Subtraction Result:",result_sub)
