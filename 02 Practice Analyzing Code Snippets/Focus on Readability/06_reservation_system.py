class create_reservation:
    """Sistema básico de reservas para un restaurante."""
    def __init__(self, name, guests, time):
        self.name = name
        self.guests = guests
        self.time = time

    def display_reservation(self):
        """Muestra los detalles de la reserva."""
        print(f"Reserva a nombre de {self.name} para {self.guests} personas a las {self.time}.")

reservations = [
    Reservation("Carlos", 2, "7:00 PM"),
    Reservation("Ana", 4, "8:00 PM"),
    Reservation("Luis", 3, "9:00 PM")
]

# Mostrar reservas
for reservation in reservations:
    reservation.display_reservation()
