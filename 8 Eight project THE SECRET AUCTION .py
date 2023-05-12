from replit import clear
from my_pic import logo

should_end = False
users_list = []
print(logo)
while not should_end:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))

  #add people
  def add_people(name_dict, bid_dict):
    users_dict = {}
    users_dict[name_dict] = bid_dict
    users_list.append(users_dict)

  add_people(name_dict=name, bid_dict=bid)

  #defines the largest value in the list of dictionaries and its key
  def winner(users_list):
    winner_key = ""
    max_value = 0
    for users in users_list:
      for key, value in users.items():
        if value > max_value:
          winner_key = key
          max_value = value
    print(f"The winer is {winner_key} with a bid of {max_value}")

  #should end?
  any_others = input(
    "Are there any other bidders? Type 'yes' or 'no'. ").lower()
  clear()
  if any_others == 'no':
    should_end = True
    winner(users_list)
