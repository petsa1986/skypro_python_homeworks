from address import Address
from mailing import Mailing

to_address = Address('344091', 'Ростов-на-Дону', 'Коммунистический ', '43', '24')
from_address = Address('352330', 'Усть-Лабинск', 'Ленина', '70', '6')
mailing = Mailing(to_address, from_address, 123456, 'ABC123')

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.home} - {mailing.from_address.room} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.home} - {mailing.to_address.room}. Стоимость {mailing.cost} рублей.")