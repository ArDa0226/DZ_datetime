
import datetime
class SuperDate(datetime.datetime):

    def __init__(self, year, month, day, hour):
        self.year : year
        self.month : month
        self.day : day
        self.hour : hour
    def get_season(self):
        seasons = {'Winter':(12, 1, 2), 'Spring':(3, 4, 5),
                   'Summer':(6, 7, 8), 'Autum':(9, 10, 11)}
        for k, v in seasons.items():
            if v.count(self.month):
                return k


    def get_time_of_day(self):
        time_of_day = {'Morning':(range(6, 12)), 'Day':(range(12, 18)),
                       'Evening':(range(18, 24)), 'Nigth':(range(0, 6))}
        for k, v in time_of_day.items():
            if v.count(self.hour):
                return k

a = SuperDate(2024, 6, 22, 19)
print(a.get_season())
print(a.get_time_of_day())
