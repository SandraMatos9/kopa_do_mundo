from exceptions import ImpossibleTitlesError, NegativeTitlesError, InvalidYearCupError
from datetime import datetime

data_dict = {
    "name": "França",
    "titles": -3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}


def data_processing(data):
    datetime_atual = datetime.now()
    date_object = datetime.strptime(data["first_cup"], "%Y-%m-%d")

    year_now = int(datetime_atual.strftime("%Y"))
    year = int(date_object.year)
    titles = int(data["titles"])
    print(year)
    list_cup_year = []
    for i in range(year, year_now, 4):
        list_cup_year.append(i)
    quant_titles = 0
    quant_titles = len(list_cup_year)

    variavel = (year - 1930) % 4 != 0
    print(variavel)
    if year < 1930 or variavel:
        raise InvalidYearCupError("there was no world cup this year")
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")
    if titles > quant_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
