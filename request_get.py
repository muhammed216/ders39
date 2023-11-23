import requests
bolgeler_URL = 'https://data.police.uk/api/forces'
response = requests.get(bolgeler_URL)
#help(response)

print(response.status_code)
print(response.url)
print(response.text)
print(response.json())


#https://data.police.uk/api/crime-categories?date=2011-08
suc_kategorileri_URL = 'https://data.police.uk/api/crime-categories'
payload = {'date': '2023-01'}
response = requests.get(suc_kategorileri_URL, params=payload)
print(response.json())

suc_URL = 'https://data.police.uk/api/crimes-no-location'

payload = {
   'category': 'all crime',
   'force': 'city-of-london',
   'date': '2023-1'}
response = requests.get(suc_URL, params=payload)


print(response.json())


class SucRaporu():
   def __init__(self, bolge, tarih, suc_tipi='all crime'):
      self.bolge = bolge
      self.tarih = tarih
      self.suc_tipi = suc_tipi
      self.suclar = self.suclari_bul

   def suclari_bul(self):
      suc_URL = 'https://data.police.uk/api/crimes-no-location'

      payload = {
         'category': self.suc_tipi,
         'force': self.bolge,
         'date': self.tarih}
      response = requests.get(suc_URL, params=payload)


      if response.status_code == 200:
         return response.json()
      else:
         return None

   def suclari_raporla(self):
      suclar_listesi = []
      if self.suclar is not None:
         for suc in self.suclar:
            suclar_listesi.append(suc['category'])

         return suclar_listesi

      sr = SucRaporu('city-of-london', '2023-01')

      sr.suclar





      





