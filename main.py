############### Blackjack Project #####################

import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
stats = {
  "dealer": {
    "cards": [],
  },
  "player": {
    "cards": [], 
    "money": 1000,
    "bet": 0
  },
}

def blackjack():
  def bet(game, outcome):
    b_total = stats['player']['money']
    if game == "pregame":
      print(f"Your bank total: {b_total}")
      wager = int(input("How much did you want to bet?\n"))
      if wager > b_total:
        print("Insufficent amount. Try again.")
        bet('pregame','none')
      stats['player']['bet'] = wager
      return wager
    if game == "postgame":
      betted = stats['player']['bet']
      if outcome == "win":
        b_total += betted
      elif outcome == "lose":
        b_total -= betted
      stats['player']['money'] = b_total
      print(f"Your balance: {b_total}")
  
  def calculate_total(who):
    return sum(stats[who]['cards'])
    
  def deal_cards():
    for _ in range(2):
      for player in stats:
        stats[player]['cards'].append(random.choice(cards))
    print(f"Dealer's hand: {stats['dealer']['cards'][0]}")
    print(f"Your hand: {stats['player']['cards']}. Score: {calculate_total('player')}")

  def handle_ace(who):
    for card in range(len(stats[who]['cards'])):
      if stats[who]['cards'][card] == 11:
        if calculate_total(who) > 21:
          stats[who]['cards'][card] = 1
          
  def less_than_17(dealer_total):
    if dealer_total < 17:
      stats['dealer']['cards'].append(random.choice(cards))
      handle_ace('dealer')
      d_total = calculate_total("dealer")
      less_than_17(d_total)
    return calculate_total('dealer')

  def game_status(player, dealer):
    if d_total == 21:
      print("You lose.")
      bet("postgame", "lose")
    elif p_total == d_total:
      print("Draw.")
    elif d_total > 21 or d_total < p_total and p_total <= 21:
      print("You win!")
      bet("postgame", "win")
    elif d_total > p_total and d_total <= 21:
      print("You lose.")
      bet("postgame", "lose")
    print(f"Dealer's hand: {stats['dealer']['cards']}. Score: {d_total}")
    print(f"Your hand: {stats['player']['cards']}. Score: {p_total}")
    
  print(logo)
  print(f"Bet: {bet('pregame','none')}")
  deal_cards()
  active_round = True
  while active_round:
    p_total = calculate_total("player")
    if p_total == 21:
      if len(stats['player']['cards']) == 2:
        print("Blackjack!")
      else:
        print("You win!")
      bet("postgame", "win")
      active_round = False
    else:
      hit = str(input("Type 'y' to hit or 'n' to stand: \n")).lower().strip()
      if hit == 'n':
        p_total = calculate_total("player")
        d_total = calculate_total("dealer")
        d_total = less_than_17(d_total)
        game_status(p_total, d_total)
        active_round = False
      elif hit == 'y':
        stats['player']['cards'].append(random.choice(cards))
        handle_ace("player")
        p_total = calculate_total("player")
        print(f"Your hand: {stats['player']['cards']}. Score: {p_total}")
        if p_total > 21:
          print("You lose.")
          bet("postgame", "lose")
          active_round = False
    if not active_round:
      if stats['player']['money'] == 0:
        print("You have no more funds to play. Goodbye.")
      else:
        continue_game = input("Type 'y' to play another round. \n")
        if continue_game == 'y':
          stats['dealer']['cards'].clear()
          stats['player']['cards'].clear()
          clear()
          blackjack()
        else:
          active_round = False
blackjack()
