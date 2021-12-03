from random import sample

def game():
  blackjack: int = 21
  cards: list    = [
    'A', 'A', 'A', 'A', \
    2, 2, 2, 2,         \
    3, 3, 3, 3,         \
    4, 4, 4, 4,         \
    5, 5, 5, 5,         \
    6, 6, 6, 6,         \
    7, 7, 7, 7,         \
    8, 8, 8, 8,         \
    9, 9, 9, 9,         \
    10, 10, 10, 10,     \
    'J', 'J', 'J', 'J', \
    'Q', 'Q', 'Q', 'Q', \
    'K', 'K', 'K', 'K'  \
  ]
  shuffled: list  = sample(cards, len(cards))
  player: tuple   = (shuffled[0], shuffled[1])
  dealer: tuple   = (shuffled[2], shuffled[3])
  player_sum: int = \
    (10 if player[0] in { 'J', 'Q', 'K' } else (player[0], 11)[player[0] is 'A']) + \
    (10 if player[1] in { 'J', 'Q', 'K' } else (player[1], 11)[player[1] is 'A'])
  print(f'Player Hand: { player } (sum={ player_sum })')
  dealer_sum: int = \
    (10 if dealer[0] in { 'J', 'Q', 'K' } else (dealer[0], 11)[dealer[0] is 'A']) + \
    (10 if dealer[1] in { 'J', 'Q', 'K' } else (dealer[1], 11)[dealer[1] is 'A'])
  print(f'Dealer Hand: ({ dealer[0] }, #)')

  ### Checks for Blackjack ###
  if player_sum == blackjack and dealer_sum != blackjack:
    print('Blackjack! Player wins.')
    exit(0)
  elif dealer_sum == blackjack and player_sum != blackjack:
    print('Blackjack! Dealer wins.')
    exit(1)
  elif player_sum == blackjack and dealer_sum == blackjack:
    print('Blackjack! Both player and dealer tied for 21.')
    exit(1)

  ### Turns ###
  deck_index: int = 4
  while True:
    user_input: str = input('If you wish to hit, type \'y\': ')
    hit: bool       = user_input.strip().lower() == 'y'
    if hit and player_sum < blackjack:
      top_card    = shuffled[deck_index]
      player     += (top_card, )
      player_sum += (10 if top_card in { 'J', 'Q', 'K' } else (top_card, 11)[top_card is 'A']) 
      deck_index += 1
      print(f'Player Hand: { player } (sum={ player_sum })')
      if player_sum > blackjack:
        print('Bust!')
        break
    else: break
  if player_sum > blackjack or dealer_sum >= player_sum:
    print(f'Dealer wins. (cards={ dealer }, sum={ dealer_sum })')
    print(f'Player loses. (cards={ player }, sum={ player_sum })')
    exit(1)
  else:
    print(f'Player wins. (cards={ player }, sum={ player_sum })')
    print(f'Dealer loses. (cards={ dealer }, sum={ dealer_sum })')
    exit(0)

if __name__ == '__main__':
  game()
