import random
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
stats = {
  "dealer": {
    "cards": [],
    "money": 0,
  },
  "player": {
    "cards": [], 
    "money": 1000,
  }
}
def blackjack():
  def calculate_total(who):
    return sum(stats[who]['cards'])
    
  def deal_cards():
    for _ in range(2):
      for player in stats:
        stats[player]["cards"].append(random.choice(cards))
    print(f"Dealer's hand: {stats['dealer']['cards'][1]}")
    print(f"Your hand: {stats['player']['cards']}. Score: {calculate_total('player')}")
  deal_cards()

  def less_than_17(dealer_total):
    stats["dealer"]["cards"].append(random.choice(cards))
    dealer_total = calculate_total("dealer")
    if dealer_total < 17:
      less_than_17(dealer_total)
  
  def handle_ace(who):
    for card in range(len(stats[who]['cards'])):
      if stats[who]['cards'][card] == 11:
        print(f"{who.title()} hand: {stats[who]['cards']}")
        ace = input("Type 'y' for 1 or type 'n' for 11? ")
        if ace == 'y':
          stats[who]['cards'][card] = 1
  
  active_round = True
  while active_round:
    p_total = calculate_total("player")
    if p_total == 21:
      print("You win!")
      active_round = False
    else:
      hit = str(input("Type 'y' to hit or 'n' to stand: ")).lower().strip()
      if hit == 'n':
        d_total = calculate_total("dealer")
        p_total = calculate_total("player")
        if d_total == 21:
          print("You lose.")
        handle_ace("dealer")
        if d_total < 17:
          less_than_17(d_total)
          d_total = calculate_total("dealer")
        if p_total == d_total:
          print("Draw.")
        if d_total < p_total and p_total <= 21:
          print("You win!")
        if d_total > p_total and d_total <= 21:
          print("You lose.")
        print(f"Dealer's hand: {stats['dealer']['cards']}. Score: {d_total}")
        print(f"Your hand: {stats['player']['cards']}. Score: {p_total}")
        active_round = False
      if hit == 'y':
        stats["player"]["cards"].append(random.choice(cards))
        handle_ace("player")
        p_total = calculate_total("player")
        print(f"Your hand: {stats['player']['cards']}. Score: {p_total}")
        if p_total > 21:
          print("You lose.")
          active_round = False
    if not active_round:
      continue_game = input("Type 'y' to play another round. ")
      if continue_game == 'y':
        for n in range(2):
          for player in stats:
            stats[player]["cards"] = []
        blackjack()
      else:
        active_round = False
blackjack()