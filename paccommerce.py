from tabulate import tabulate
from math import sqrt

class Membership:
  database_user = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
  }

  table_membership = {
      'Platinum': ['Platinum', '15%', 'Voucher makanan + Voucher Ojek Online + Voucher Liburan + Cashback Max 30persen'],
      'Gold': ['Gold', '10%', 'Voucher Makanan + Voucher Ojek  Online'],
      'Silver':['Silver', '8%', 'Voucher Makanan']
                   }
  table_requirement = {
      'Platinum' : ['Platinum', 8, 15, ],
      'Gold' : ['Gold', 6, 10],
      'Silver' : ['Silver', 5, 7]
  }

  def __init__(self, username):
    self.username = username
    self.database_user[username] = ""
  
  def check_all_membership(self):
    table = [value for membership, value in self.table_membership.items()]
    header = ['Membership', 'Discount', 'Detail']
    print(tabulate(table, headers = header))

  def check_requirement(self):
    table = [value for membership, value in self.table_requirement.items()]
    header = ['Membership', 'Discount', 'Detail']
    print(tabulate(table, headers = header))  

  def predict_membership(self, username, monthly_expense, monthly_income):
    if username in self.database_user.keys(): #supaya data user yg tidak terdaftar menggeser yg ada pada database
      distance = {}

      for key, value in self.table_requirement.items():
        euclidean_distance = round(sqrt((monthly_expense - value[1])**2 + (monthly_income - value[2])**2),2)
        distance[key] = euclidean_distance

      print(f'Hasil perhitungan Euclidean Distance dari user {self.username} adalah {distance}')

      for key, value in distance.items():
        if value == min(distance.values()):
          self.database_user[username] = key #untuk menyimpan username pada database user
          return key
    else:
      return "Username tidak terdaftar"

  def show_membership(self, username):
    if isinstance(username, str): #and isinstance(usia, int) jika ingin menambahkan parameter usia
      if username in self.database_user.keys(): #jika username yg dicari ada di dalam database
        return self.database_user[username]
      else:
        return 'Username tidak terdaftar'

  def __check_username(self, username):
    if isinstance(username, str):
      return True
    else:
      return 'Inputan tidak sama'

  def calculate_bill(self, username, list_harga):
    try:
      if username in self.database_user.keys(): #mengecek apakah username ada atau tidak
        membership_type = self.database_user[username] #cari membershipnya
        if membership_type != '': #jika membership tidak kosong, bisa dihitung diskonnya
          diskon = int(self.table_membership[membership_type][1].split('%')[0])/100
          total_bill = (1 - diskon) * sum(list_harga)
          return total_bill
        else:
          raise Exception('Membership kosong, silakan lakukan predict')
      else:
        raise Exception('Username tidak terdaftar')
    except Exception as e:
      print(e)
