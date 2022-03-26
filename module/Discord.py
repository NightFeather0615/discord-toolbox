import requests
import random
import typing

class Discord(object):
  def __init__(self):
    pass

  def fetch_user(token: str) -> dict:
    user_data = requests.get("https://discord.com/api/users/@me", headers = {"Authorization": token}).json()
    if user_data.get('code') == 0:
      print("\n[Login Failed]\nHTTP Error: 401 Unauthorized, invalid token")
      return None
    else:
      user_info = f"\n[Login Success]\nUser: {user_data['username']}#{user_data['discriminator']}\nID: {user_data['id']}\nEmail: {user_data['email']}\nLocale: {user_data['locale']}\nMFA: {user_data['mfa_enabled']}\n"
      print(user_info)
      return user_data

  def change_hypesquad_house(token: str, house: typing.Union[str, int] = None) -> None:
    url = "https://discord.com/api/hypesquad/online"
    house = int(house)
    if house == None:
      house = random.randint(1, 3)
    id_to_name = {
      1: "Bravery",
      2: "Brilliance",
      3: "Balance"
    }
    payload = {'house_id': house}
    respond = requests.post(url, headers = {"Authorization": token, "Content-Type": "application/json"}, json = payload)
    if respond.status_code == 204:
      print(f"Hypesquad house changed to {id_to_name[house]}")
    else:
      print(f"Hypesquad house change failed, HTTP Error: {respond.status_code}")