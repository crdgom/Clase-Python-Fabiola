class Reservation: #Le cambiaria el nombre de create_reservation a Reservation 
    """Sistema básico de reservas para un restaurante."""
    def __init__(self, name, guests, time):#le agregaria el apellido como un argumento mas "last_name"
        self.name = name
        self.guests = guests #le cambiaria el combre a la variable a guests_number 
        self.time = time #Le cambiaria el nombre a "ckeckin_date_hr
       #self.last_name= last_name
       #Le agregaria un atributo llamado dia y hora de checkout_date_hr
   
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
