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

def get_contact_info():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    return name, email, phone

def get_vogn_type():
    vogn_type = input("Enter type of vogn ('sittevogn' or 'sovevogn'): ")
    while vogn_type not in ['sittevogn', 'sovevogn']:
        print("Invalid vogn type. Please enter 'sittevogn' or 'sovevogn'")
        vogn_type = input("Enter type of vogn ('sittevogn' or 'sovevogn'): ")
    return vogn_type

def get_phone_number():
    phone_number=input("Enter your phone number: ")
    return phone_number

def get_yes_or_no():
    answer= input("Enter your answer y or n: ")
    return answer

def get_number(): 
    number=input("Enter your number: ")
    return number