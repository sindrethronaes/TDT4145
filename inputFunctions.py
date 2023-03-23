def get_station_name():
    station_name = input("Enter station name: ")
    return station_name
    
def get_weekday():
    weekday = int(input("Enter weekday number (e.g., Sunday = 0, Monday = 1, etc.): "))
    return weekday


def start_station():
    startstasjon = input("Enter starting station: ")
    return startstasjon

def end_station():
    end_station = input("Enter ending station: ")
    return end_station

def date():
    date = input("Enter date (YYYY-MM-DD): ")
    return date

def time():
    time = input("Enter time (HH:MM): ")
    return time

def get_name():
    name = input("Enter your name: ")
    return name

def get_e_mail():
    email = input("Enter your email: ")
    return email

def get_phone_number():
    phone = input("Enter your phone number: ")
    return phone

def get_vogn_type():
    vogn_type = input("Enter type of vogn ('sittevogn' or 'sovevogn'): ")
    while vogn_type not in ['sittevogn', 'sovevogn']:
        print("Invalid vogn type. Please enter 'sittevogn' or 'sovevogn'")
        vogn_type = input("Enter type of vogn ('sittevogn' or 'sovevogn'): ")
    return vogn_type
