from smartphone import Smartphone
catalog = []
phone1 = Smartphone ('Samsung', 'Galaxy A54', '+79512653748')
phone2 = Smartphone ('Huawei', 'nova 11 Pro', '+79183627490')
phone3 = Smartphone ('Xiaomi', '13 Pro', '+79183549283')
phone4 = Smartphone ('ASUS', 'Zenfone 10', '+79883420175')
phone5 = Smartphone ('POCO', 'F5 Pro', '+79284360267')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print (f"{phone.marka_sm} - {phone.model_sm}, {phone.number_phone_sm}")