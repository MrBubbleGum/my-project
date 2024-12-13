from abc import ABC, abstractmethod
from colorama import Fore, init

# Инициализация colorama для работы с цветами в консоли
init(autoreset=True)

# Абстрактный базовый класс для транспорта
class Transport(ABC):
    def __init__(self, transport_type, flight_number, departure, destination, ticket_prices):
        self.transport_type = transport_type
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.ticket_prices = ticket_prices

    @property
    @abstractmethod
    def available_seats(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    def is_full(self):
        """Проверка, есть ли свободные места."""
        return self.available_seats == 0


# Класс для автобусов
class Bus(Transport):
    def __init__(self, transport_type, flight_number, departure, destination, ticket_prices, soft_seats, hard_seats):
        super().__init__(transport_type, flight_number, departure, destination, ticket_prices)
        self.soft_seats = soft_seats
        self.hard_seats = hard_seats

    @property
    def available_seats(self):
        """Возвращаем количество свободных мест в автобусе."""
        return self.soft_seats + self.hard_seats

    def display_info(self):
        """Отображение информации об автобусе."""
        color = Fore.RED if self.is_full() else ''  # Красный цвет, если мест нет
        print(f"{color}Transport Type: {self.transport_type}")
        print(f"{color}Flight Number: {self.flight_number}")
        print(f"{color}Departure: {self.departure}")
        print(f"{color}Destination: {self.destination}")
        print(f"{color}Available Seats: {self.available_seats}")
        print(f"{color}Ticket Prices: {self.ticket_prices}")


# Класс для самолетов
class Airplane(Transport):
    def __init__(self, transport_type, flight_number, departure, destination, ticket_prices, economy_seats, business_seats, first_class_seats):
        super().__init__(transport_type, flight_number, departure, destination, ticket_prices)
        self.economy_seats = economy_seats
        self.business_seats = business_seats
        self.first_class_seats = first_class_seats

    @property
    def available_seats(self):
        """Возвращаем минимальное количество свободных мест среди всех классов."""
        return min(self.economy_seats, self.business_seats, self.first_class_seats)

    def display_info(self):
        """Отображение информации о самолете."""
        color = Fore.RED if self.is_full() else ''  # Красный цвет, если мест нет
        print(f"{color}Transport Type: {self.transport_type}")
        print(f"{color}Flight Number: {self.flight_number}")
        print(f"{color}Departure: {self.departure}")
        print(f"{color}Destination: {self.destination}")
        print(f"{color}Available Seats: {self.available_seats}")
        print(f"{color}Ticket Prices: {self.ticket_prices}")


# Класс для поездов
class Train(Transport):
    def __init__(self, transport_type, flight_number, departure, destination, ticket_prices, luxury_seats, compartment_seats, platzkart_seats, general_seats):
        super().__init__(transport_type, flight_number, departure, destination, ticket_prices)
        self.luxury_seats = luxury_seats
        self.compartment_seats = compartment_seats
        self.platzkart_seats = platzkart_seats
        self.general_seats = general_seats

    @property
    def available_seats(self):
        """Возвращаем минимальное количество свободных мест среди всех типов вагонов."""
        return min(self.luxury_seats, self.compartment_seats, self.platzkart_seats, self.general_seats)

    def display_info(self):
        """Отображение информации о поезде."""
        color = Fore.RED if self.is_full() else ''  # Красный цвет, если мест нет
        print(f"{color}Transport Type: {self.transport_type}")
        print(f"{color}Flight Number: {self.flight_number}")
        print(f"{color}Departure: {self.departure}")
        print(f"{color}Destination: {self.destination}")
        print(f"{color}Available Seats: {self.available_seats}")
        print(f"{color}Ticket Prices: {self.ticket_prices}")


# Класс для объектов с нулевыми местами
class TransportWithZeroSeats(Transport):
    def __init__(self, transport_type, flight_number, departure, destination, ticket_prices):
        super().__init__(transport_type, flight_number, departure, destination, ticket_prices)
    
    @property
    def available_seats(self):
        return 0  # Количество мест всегда 0
    
    def display_info(self):
        """Отображение информации для случая с нулевыми местами."""
        print(f"{Fore.RED}Transport Type: {self.transport_type}")
        print(f"{Fore.RED}Flight Number: {self.flight_number}")
        print(f"{Fore.RED}Departure: {self.departure}")
        print(f"{Fore.RED}Destination: {self.destination}")
        print(f"{Fore.RED}Available Seats: 0")
        print(f"{Fore.RED}Ticket Prices: {self.ticket_prices}")


# Функция для чтения данных из файла
def read_transport_data(file_path):
    transports = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()

            if len(parts) < 4:
                print(f"Error: Not enough data in the line: {line.strip()}")
                transport = TransportWithZeroSeats('', '', '', '', [])
                transports.append(transport)
                continue

            transport_type = parts[0]  
            flight_number = parts[1]  
            departure = parts[2]  
            destination = parts[3]  

            ticket_prices = []
            try:
                ticket_prices = list(map(int, parts[4:]))  
            except ValueError:
                print(f"Error: Invalid ticket prices in line: {line.strip()}")

            soft_seats = hard_seats = 0
            economy_seats = business_seats = first_class_seats = 0
            luxury_seats = compartment_seats = platzkart_seats = general_seats = 0

            if ticket_prices:
                if transport_type == "airplane":
                    economy_seats = 100
                    business_seats = 50
                    first_class_seats = 20
                    transport = Airplane(transport_type, flight_number, departure, destination, ticket_prices, economy_seats, business_seats, first_class_seats)

                elif transport_type == "bus":
                    soft_seats = 30
                    hard_seats = 20
                    transport = Bus(transport_type, flight_number, departure, destination, ticket_prices, soft_seats, hard_seats)

                elif transport_type == "train":
                    luxury_seats = 10
                    compartment_seats = 30
                    platzkart_seats = 50
                    general_seats = 100
                    transport = Train(transport_type, flight_number, departure, destination, ticket_prices, luxury_seats, compartment_seats, platzkart_seats, general_seats)

                else:
                    print(f"Unknown transport type: {transport_type}")
                    transport = TransportWithZeroSeats(transport_type, flight_number, departure, destination, ticket_prices)

            else:
                transport = TransportWithZeroSeats(transport_type, flight_number, departure, destination, ticket_prices)

            transports.append(transport)

    return transports


# Функция для отображения всех данных о транспорте
def display_all_transport_info(transports):
    print(f"{'Transport Type':<15}{'Flight Number':<15}{'Departure':<15}{'Destination':<15}{'Available Seats':<20}")
    print("="*80)
    
    for transport in transports:
        transport.display_info()
        print("-" * 40)

# Функция для вывода цен на билеты для конкретного типа транспорта
def display_ticket_prices(transports, transport_type, seat_type=None):
    seat_types = {"1": "Economy", "2": "Business", "3": "First Class"}
    
    print(f"Ticket Prices for {transport_type.capitalize()}:\n")
    print(f"{'Flight Number':<15}{'Seat Type':<15}{'Price':<10}")
    print("="*50)
    
    for transport in transports:
        if transport.transport_type == transport_type:
            # Фильтруем по типу места
            for index, price in enumerate(transport.ticket_prices):
                seat_type_label = seat_types.get(str(index + 1), "Other")  # Для других типов мест
                if seat_type and seat_type != seat_type_label:
                    continue

                print(f"{transport.flight_number:<15}{seat_type_label:<15}{price}")

# Основная функция
def main():
    file_path = "1.txt"  # Путь к вашему файлу
    transports = read_transport_data(file_path)
    
    # Запрос у пользователя для выбора транспорта (цифры)
    print("Choose transport type:")
    print("1 - Bus")
    print("2 - Airplane")
    print("3 - Train")
    transport_choice = input("Enter number: ").strip()

    # Проверка на корректность ввода
    transport_types = {"1": "bus", "2": "airplane", "3": "train"}
    transport_type = transport_types.get(transport_choice, None)

    if not transport_type:
        print("Invalid transport type selected!")
        return

    # Запрос у пользователя для выбора места (цифры)
    print("Choose seat type:")
    print("1 - Economy")
    print("2 - Business")
    print("3 - First Class")
    seat_choice = input("Enter number: ").strip()

    # Проверка на корректность ввода
    seat_types = {"1": "Economy", "2": "Business", "3": "First Class"}
    seat_type = seat_types.get(seat_choice, None)

    if not seat_type:
        print("Invalid seat type selected!")
        return

    # Отображаем цены для выбранного транспорта и места
    display_ticket_prices(transports, transport_type, seat_type)

# Запуск программы
if __name__ == "__main__":
    main()
