import random

class Cards(object):
    
	'''
    initialize without __init__ because all cards have the same rank
	there are no suits, but 4 decks. so every deck has 4 copies of each rank due to the 4 suits and there are 4 decks
	hence the 16 number
	also initializes the rank dictionary, as it will take the key which is the rank of the card, and allocates it 
	accordingly with the correct value
	'''
	deck = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']*16  
	rank = {'A1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10, 'A2':11}

	def shuffle(self):
		
		''' 
	Uses the fisher yates shuffle algorithm
	First we need the size of the deck
	Then we use a for loop to iterate through each card of the deck from the bottom of the deck to the top of the deck
	Hence why start begins with decksize-1, ends at 0 and increments by -1
	We then have a variable rand that gets a random number between the top of the deck and the iteration
	The card that has finished shuffling will in take the random value, while the card needing to be shuffled again
	in takes the iteration value num
		'''
		
		deck_size = len(Cards.deck)
		for num in range(deck_size-1, 0, -1):
			rand = random.randint(0,num)
			Cards.deck[num], Cards.deck[rand] = Cards.deck[rand], Cards.deck[num]
		
		return Cards.deck   

	def getTopDeck(self):
		
		return Cards.deck[0]

	def removeTopDeck(self):
		
		del Cards.deck[0]

	def checkDeckSize(self):
		
		return len(Cards.deck)        

	def resetDeck(self):

	## when the deck only has a certain amount of cards left, we get a new batch of 4 decks
		
		Cards.deck = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']*16  
    
class Dealer(object):
    
	hand = []
	dealer_total = 0
	face_up_total = 0

	'''
	when the dealer deals a card, it first adds a card to the list, which is to hand variable from the top of the deck.
	then the dealer will remove that card at the top of the deck from the cards object
	'''

	def selfDeal(self,deck):

		self.hand.append(deck.getTopDeck())
		deck.removeTopDeck()

	def playerDeal(self,player,num,deck):

		player[num].hand.append(deck.getTopDeck())
		deck.removeTopDeck()

	def dealerTurn(self,deck):

		'''
	when it's the dealer's turn to deal cards to himself after every player has either bust, doubled or stood pat,
	if the dealer's hand is not at 17 or above, he will deal cards to himself the same way as he would in 
	methods selfDeal and playerDeal. 
	the dealer will also let you know what the count is at with the print statement
		'''

		while Dealer.dealer_total < 17:
			self.hand.append(deck.getTopDeck())
			deck.removeTopDeck()
			self.produceDealerTotal()
			print "Dealer's hand: %s Count: %s" %(self.hand, self.getDealerTotal())                   

	def removeHand(self):

		'''
	when the hand is finished, the dealer needs to restart fresh without a hand. 
	in order to do this, he needs to remove all the elements in the hand index to start fresh.
	so he will need to get the size of his hand, then call a while loop to slowly rid the elements 
	in his hand list. to not get the error of outofindex, within the while loop the hand size has to be 
	reset to the current amount 
		'''

		hand_size = len(self.hand)
		while hand_size > 0:
			del self.hand[hand_size-1]
			hand_size = len(self.hand)

	def produceDealerTotal(self):	

		Dealer.dealer_total = total(self.hand)
		
	def getDealerTotal(self):

		return Dealer.dealer_total

	def resetDealerTotal(self):

		Dealer.dealer_total = 0

	def produceFaceUpTotal(self):

		Dealer.face_up_total = total(self.hand[1])

	def getFaceUpTotal(self):

		return Dealer.face_up_total

	def resetFaceUpTotal(self):

		Dealer.face_up_total = 0

	def getHand(self):

		return self.hand

	def getHiddenHand(self):

	## gives a new list that prints '' to print 1 card face down and then print the other card face up 
		return ['',self.hand[1]]
			
class Player(object):
    
	'''
	this class will be the parent of all the human and bot players. 
	it will initialize with the name, the bankroll, an empty hand which is a list, the amount he will bet
	which will be looked at in a method for other child classes, whether he has blackjack or not, 
	the current total for his hand and whether or not he busts. 
	
	an added note is there are getters and resetters for CardTotal, which involves a function total. 
	this will be elaborated on in the comments in the total function
	'''
	
	## universal total that will not change as it depends on what face card the dealer has.
	## this variable is used on more complex bots like GoodJoeBot who will use good basic blackjack strategy to play
	dealer_face_card = 0

	def __init__(self, name, bankroll):

		self.name = name
		self.bankroll = bankroll
		self.hand = []
		self.bet_amount = 0
		self.black_jack = False
		self.card_total = 0
		self.has_bust = False
		
	def receiveCard(self, deck):
	
		'''
	this method here reduces line of code for receiving a single card from the dealer when the bot hits or doubles.
	this is especially the case for every other child bot class not named Beginner Joe Bot.
	it works the same way as selfDeal and playerDeal in Dealer class except it will also keep track of the card count
	in the final 2 lines. one being it actually calls the function and returns the value for the variable card_total,
	the other being it just prints the output.
		'''
	
		self.hand.append(deck.getTopDeck())
		deck.removeTopDeck()            
		self.card_total = total(self.hand)
		print "%s's hand: %s Count: %s " %(self.name,self.getHand(),self.getCardTotal())	

	def addBankroll(self, amount):

		self.bankroll += amount

	def subtractBankroll(self, amount):

		self.bankroll -= amount

	def getBetAmount(self):

		return self.bet_amount
			
	def hasBusted(self):

		self.has_bust = True

	def resetBusted(self):

		self.has_bust = False

	def getBust(self):

		return self.has_bust
			
	def getDecision(self):

		return self.decision.lower()

	def isBlackJack(self):

		return self.black_jack

	def resetBlackJack(self):

		self.black_jack = False

	def getBankroll(self):

		return self.bankroll      

	def removeHand(self):

	##same as removeHand method for the Dealer class 
		hand_size = len(self.hand)
		while hand_size > 0:
			del self.hand[hand_size-1]
			hand_size = len(self.hand)

	def getCardTotal(self):

		return self.card_total

	def resetCardTotal(self):

		self.card_total = 0

	def getHand(self):

		return self.hand    

	def obtainDealerFaceCard(self, dealer):

		Player.dealer_face_card = dealer.getFaceUpTotal()
		
	def getDealerFaceCard(self):
		
		return Player.dealer_face_card

	def __del__(self):

		print '%s has been eliminated' % (self.name)

class Bot(Player):

	'''
	the mother of all bot classes, who is also a child of the player class, who again is the mother of all players
	even human players
	'''

	def __init__(self, name, bankroll):
        
		self.name = name
		self.bankroll = bankroll
		self.hand = []
		self.bet_amount = 0
		self.black_jack = False
		self.card_total = 0
		self.decision = ''
		self.has_bust = False

class Human(Player):

	## the human class, where you play against the house. it now has a bet method and a decisionTree method.
	
    def __init__(self, name, bankroll):
        
        self.name = name
        self.bankroll = bankroll
        self.hand = []
        self.bet_amount = 0
        self.black_jack = False
        self.card_total = 0
        self.decision = ''
        self.has_bust = False

    def bet(self):
    
	##takes the input from human, subtracts from bankroll, prints the output
	
        self.bet_amount = input('How much are you betting')
        self.subtractBankroll(self.bet_amount)
        print '%s bet size: %s' %(self.name, self.bet_amount)
        print 'bankroll:', self.getBankroll()		
        
    def decisionTree(self, deck):
    
	'''
	the decision tree method. first it checks to see if you have a blackjack. in normal blackjack, if you get a blackjack,
	you win without needing to look up the dealer. so this is the case here too.
	otherwise (aka else), a while loop is incorporated and the game will ask for your input to hit, stand or double (only on the 1st draw). 
	if you stand or double, you're out of the while loop, otherwise you will keep hitting until you stand or hit 21
	which is good for you or you just bust. 
	'''
    
        self.card_total = total(self.hand)
        
        if self.getCardTotal() == 21:
            print 'BlackJack'
            self.black_jack = True
			
        else:     
            print "%s's hand: %s" %(self.name,self.getHand())
            self.decision = raw_input('S for stand, H for hit, D for double ')
            while self.decision.lower() != 's':
                while self.decision.lower() != 'h' and self.decision.lower() != 'd':
                    self.decision = raw_input('S for stand, H for hit, D for double ') 
                self.receiveCard(deck)
                if self.card_total > 21:
                    print 'Bust'     
                    self.hasBusted()
                    break                
                elif self.card_total == 21:
                    print 'Twenty one'
                    break                
                elif self.decision.lower() == 'd':
                    break
                self.decision = raw_input('S for stand, H for hit ')

class BeginnerJoeBot(Bot):

	'''
	the Beginner Joe Bot. the worst bot of the bunch. he may hit when he is given 2 face cards to start. 
	he may stand when he is given 2 low cards that doesn't add to at least 9. this is the bot that will 
	dumbfound you with his poor decision making. he is meant to make these poor decisions as the decisionTree
	method dictates that given a 3 to 2 odd, he will hit, regardless of the current count. given a 1 to 2 odd,
	he will stand, no matter what the current card count is. he is the Beginner Joe, and he is meant to be bad
	'''
				
	def __init__(self, name, bankroll):
        
		self.name = name
		self.bankroll = bankroll
		self.hand = []
		self.bet_amount = 0
		self.black_jack = False
		self.card_total = 0
		self.decision = ''
		self.has_bust = False

	def bet(self):

		'''
		the Beginner Joe Bot will bet a somewhat modest amount between 100 to 500, just because. 
		the import random at the top of the code will help us in getting the random number for bet_amount
		with the random.randint(low cap, high cap)
		'''
		self.bet_amount = random.randint(100,500)
		self.subtractBankroll(self.bet_amount)
		print '%s bet size: %s' %(self.name, self.bet_amount)
		print 'bankroll:', self.getBankroll()
	
	def decisionTree(self, deck):
	
		'''
		the decision tree of a Beginner Joe Bot is here. he will initialize a local variable rand_decision
		which will be at 0 for this given time. but when we get to the while loop when his hand isn't at 21 or above,
		rand_decision will generate a random number between 0 to 100. the Beginner Joe Bot will have a 60% chance
		he will hit on any card and 40% chance he will just stand. since he is a beginner, he doesn't understand
		the concept of doubling, so he will not double.
		'''
		rand_decision = 0
		self.card_total = total(self.hand)		
		if self.getCardTotal() == 21:
			print 'BlackJack'
			self.black_jack = True		
			
		else:
			print "%s's hand: %s" %(self.name,self.getHand())
			while self.getCardTotal() < 21:
				rand_decision = random.randint(0,100)
				print 'decision', rand_decision
				if rand_decision <= 60:
					self.decision = 'h'					
					self.receiveCard(deck)
					if self.getCardTotal() > 21:
						print 'Bust'     
						self.hasBusted()
						break                
					elif self.getCardTotal() == 21:
						print 'Twenty one'
						break   
				else:
					self.decision = 's'
					break
		
class SteadyJoeBot(Bot):

	'''
	Steady Joe Bot implies that this bot plays in a steady way, takes very small risks like betting small amounts instead
	and never hitting when his cards hits 12 or more, only hitting when his cards are 9 or less, and only doubling on 10 
	or 11. Steady Joe Bot plays it safe, and this is what the bot does.
	'''

	def __init__(self, name, bankroll):
        
		self.name = name
		self.bankroll = bankroll
		self.hand = []
		self.bet_amount = 0
		self.black_jack = False
		self.card_total = 0
		self.decision = ''
		self.has_bust = False
	
	def bet(self):

	## Steady Joe Bot only bets 50 to 100, very small amount given his 10,000 bankroll 
		self.bet_amount = random.randint(50,100)
		self.subtractBankroll(self.bet_amount)
		print '%s bet size: %s' %(self.name, self.bet_amount)
		print 'bankroll:', self.getBankroll()
		

	def decisionTree(self, deck):
	
		'''
		just like Beginner Joe Bot, this bot will have a decision tree. Except he doesn't take rand_decision because
		his decisions are not randomized. instead his decisions are rigid. if at any time his cards are 11 or under 
		after the 1st hit, he will hit. else if his card count is at 10 or 11 and he hasn't hit yet, checked by the length
		of the hand list, he will double. otherwise he will hit. else, this is when his card count is at 12, he will
		always stand.
		'''
		self.card_total = total(self.hand)		
		
		if self.getCardTotal() == 21:
			print 'BlackJack'
			self.black_jack = True	
		else:
			print "%s's hand: %s" %(self.name,self.getHand())
			while self.getCardTotal() < 21:
				if self.getCardTotal() < 17:
					if self.getCardTotal() <= 9:
						self.decision = 'h'		
						self.receiveCard(deck)
						if self.getCardTotal() > 21:
							print 'Bust'     
							self.hasBusted()
							break                
						elif self.getCardTotal() == 21:
							print 'Twenty one'
							break 
					elif self.getCardTotal() == 10 or self.getCardTotal() == 11:
						if len(self.getHand()) <= 2:
							self.decision = 'd'
							self.receiveCard(deck)
							break
						else:
							self.decision = 'h'
							self.receiveCard(deck)
							if self.getCardTotal() > 21:
								print 'Bust'     
								self.hasBusted()
								break                
							elif self.getCardTotal() == 21:
								print 'Twenty one'
								break 
					else:
						self.decision = 's'
						break					
				else:
					self.decision = 's'
					break
		
class WildJoeBot(Bot):

	'''
	Wild Joe Bot, as the name implies, is a wild bot. he is wild, he will bet outrageous amounts and double at outrageous 
	times, like when he has a face card and a 6, which counts to 16. there is also a chance he will gamble on 17 because,
	he is wild. he's Wild Joe Bot, so he plays recklessly and wildly.
	'''
	def __init__(self, name, bankroll):
        
		self.name = name
		self.bankroll = bankroll
		self.hand = []
		self.bet_amount = 0
		self.black_jack = False
		self.card_total = 0
		self.decision = ''
		self.has_bust = False

	def bet(self):

	## bets can range from 200 all the way to 2000
		self.bet_amount = random.randint(200,2000)
		self.subtractBankroll(self.bet_amount)
		print '%s bet size: %s' %(self.name, self.bet_amount)
		print 'bankroll:', self.getBankroll()
	
	def decisionTree(self, deck):
	
		'''
		his decision tree is more complex than Beginner Joe Bot, but they both share rand_decision. this bot will 
		have a 40% chance to double at any card below 17, just because he's wild. he will also have a 20% chance of hitting
		on a 17, just because he's wild and reckless.
		'''
		
		rand_decision = 0
		self.card_total = total(self.hand)		
		if self.getCardTotal() == 21:
			print 'BlackJack'
			self.black_jack = True		
			
		else:
			print "%s's hand: %s" %(self.name,self.getHand())
			while self.getCardTotal() < 21:
				rand_decision = random.randint(0,100)
				print 'decision', rand_decision
				if self.getCardTotal() < 17:	
					if len(self.getHand()) <= 2:
						if rand_decision <= 40:
							self.decision = 'd'
							self.receiveCard(deck)
							if self.getCardTotal() > 21:
								print 'Bust'     
								self.hasBusted()               
							elif self.getCardTotal() == 21:
								print 'Twenty one'
							break
						else:
							self.decision = 'h'
							self.receiveCard(deck)
					else:
						self.decision = 'h'
						self.receiveCard(deck)
				elif self.getCardTotal() == 17:
					if rand_decision <= 20:		
						self.decision = 'h'		
						self.receiveCard(deck)
					else:
						self.decision = 's'
						break						
				else:
					self.decision = 's'
					break
				
				if self.getCardTotal() > 21:
					print 'Bust'     
					self.hasBusted()
					break                
				elif self.getCardTotal() == 21:
					print 'Twenty one'
					break  

class GoodJoeBot(Bot):

	'''
	Good Joe Bot, this implies he's 'good' but just good. he will still end up a loser in the long run, because he plays
	almost perfect basic strategy. he won't split as this blackjack program does not have a split implementation. 
	there's too much to go over with basic blackjack strategy, but he plays almost perfect basic blackjack strategy
	according to the chart, except for when he has a 17 or an 18 with an ace in his starting hand. here he will 
	stand exclusively. 
	'''
	def __init__(self, name, bankroll):
        
		self.name = name
		self.bankroll = bankroll
		self.hand = []
		self.bet_amount = 0
		self.black_jack = False
		self.card_total = 0
		self.decision = ''
		self.has_bust = False

	def bet(self):

	## Good Joe Bot won't take huge gambles, because he knows he's a long term loser, so he bets slightly bigger 
	## than Steady Joe Bot at 100 to 200.
		self.bet_amount = random.randint(100,200)
		self.subtractBankroll(self.bet_amount)
		print '%s bet size: %s' %(self.name, self.bet_amount)
		print 'bankroll:', self.getBankroll()
	
	def decisionTree(self, deck):
	
	## too much to explain for perfect basic blackjack strategy, but his decision is based on this and it can be found
	## googling a basic blackjack strategy chart 
		self.card_total = total(self.hand)		
		if self.getCardTotal() == 21:
			print 'BlackJack'
			self.black_jack = True		

				
		else:
			print "%s's hand: %s" %(self.name,self.getHand())
			while self.getCardTotal() < 21:				
				if self.getCardTotal() < 17:
					if self.getCardTotal() < 9:
						self.decision = 'h'
						self.receiveCard(deck)
						
					elif self.getCardTotal() == 9:
						if self.getDealerFaceCard() < 7 and len(self.getHand()) <= 2:
							self.decision = 'd'
							self.receiveCard(deck)
							break
						else:
							self.decision = 'h'
							self.receiveCard(deck)
							
					elif self.getCardTotal() == 10:
						if self.getDealerFaceCard() < 10 and len(self.getHand()) <= 2:
							self.decision = 'd'
							self.receiveCard(deck)
							break
						else:
							self.decision = 'h'
							self.receiveCard(deck)
							
					elif self.getCardTotal() == 11:
						if len(self.getHand()) <= 2:
							self.decision = 'd'
							self.receiveCard(deck)
							break
						else:
							self.decision = 'h'
							self.receiveCard(deck)
					
					else:
						if 'A' in self.getHand() and len(self.getHand()) <= 2:
							if self.getCardTotal() <= 14:
								if self.getDealerFaceCard() == 5 or self.getDealerFaceCard() == 6:
									self.decision = 'd'
									self.receiveCard(deck)
									break
								else:
									self.decision = 'h'
									self.receiveCard(deck)
									
							if self.getCardTotal() > 14 and self.getCardTotal() <= 16:							
								if self.getDealerFaceCard() == 4 or self.getDealerFaceCard() == 5 or self.getDealerFaceCard() == 6:
									self.decision = 'd'
									self.receiveCard(deck)
									break
								else:
									self.decision = 'h'
									self.receiveCard(deck)
							
							else:
								self.decision = 's'
								break
						
						else:
							if self.getDealerFaceCard() > 6:
								self.decision = 'h'
								self.receiveCard(deck)
							else:
								self.decision = 's'
								break
				
				else:
					self.decision = 's'
					break
							
				if self.getCardTotal() > 21:
					print 'Bust'     
					self.hasBusted()
					break                
				elif self.getCardTotal() == 21:
					print 'Twenty one'
					break  
						
def total(hand):

	'''
	this function's whole function is to count the totals of a hand, dealer or player, via the method of having 
	a new list that takes the card's value. 
	it first initializes a local count variable as well as a local list that's named hand_so_far.
	then it runs a for loop, where it takes the actual player/dealer's hand as the argument.
	this for loop will iterate through every card in the player/dealer's hand list and then add it's value 
	to the hand_so_far list. for example, I get a hand of T and 6. the list will iterate through and get to 
	T as the 1st card it'll iterate through. it sees that it's not an ace and will add the value of the card
	that is extracted from the dictionary rank in the Card object. so T becomes 10 and hand_so_far will have [10].
	Then the next card is 6, and it will see that it's value is 6 and will be added to the hand_so_far list. now
	the list is complete at [10,6]. 
	'''
	count = 0
	hand_so_far = []
	for card in hand:
		if card != 'A':
			hand_so_far.append(Cards.rank[card])
		else:
			if count < 12:
				hand_so_far.append(Cards.rank['A2'])
			else:
				hand_so_far.append(Cards.rank['A1'])

	## runs a for loop to go through every value in the newly formed hand_so_far list and accumulate its total through
	## the count variable
	for num in hand_so_far:
		count += num
		
	'''
	special case for dealing with the ace here. previously in appending the value of the ace, if the count is less than 12
	then take the big ace that's worth 11. however, what if you get 2 aces, both valued at 11 so you get 22. here is where
	this while loop comes in. this corrects the problem of having 2 aces being busts. the while loop condition checks to see
	if the count is greater than 21, and most importantly, if the ace value of 11 is in the list hand_so_far. so both conditions 
	are met, we remove them 1 by 1 and subtract the value of the big ace from count, and add in a new small ace from the dictionary
	A1, this is worth 1 instead of 11. we accumulate the count total by 1 accordingly instead. 
	'''
	while count > 21 and 11 in hand_so_far:
		hand_so_far.remove(11)
		count -= 11
		hand_so_far.append(Cards.rank['A1'])
		count += 1          
			
	return count

def compare_total(dealer_total, player_total):

## this function simply compares the 2 arguments, with the dealer's total and the player's total. it returns who the winner is 
## 0 being push, 1 being dealer, 2 being player
    winner = 0
    if dealer_total > player_total:
        winner = 1
    elif dealer_total < player_total:
        winner = 2
        
    return winner
	
def deal(dealer, deck, player, num):

## deals in the order of dealer himself, then to the players, then to the dealer himself, then to the players
## hence the for loop because we need to make sure every player gets a card
    dealer.selfDeal(deck)
    for n in range(num): 
        dealer.playerDeal(player, n, deck)
    dealer.selfDeal(deck)
    for n in range(num): 
        dealer.playerDeal(player, n, deck)   
        
def betting_round(player):

## self explainatory, get the bets in, return the bet amount & print the output.
    player.bet()
    player.getBetAmount()
    
def determine_amount(player):

## strictly to determine if the player doubled or not after he won his hand against the dealer.
    if player.getDecision() == 'd':
        player.addBankroll(player.getBetAmount()*4)
    else:
        player.addBankroll(player.getBetAmount()*2)   
		
def determine_winner(player, num, dealer):

	'''
	this function does what the function name says, it determines who the winner is between the player and the dealer.
	this function first has its own local boolean hasBust. this checks to see whether all players have bust or not. 
	if all players bust, dealer doesn't need to deal. we then need to check every player vs the dealer 
	through using a for loop explained in further detail in the next section of comments.
	'''
	
	hasBust = True
	
	for n in range(num):
		if player[n].getBust() == False:
			hasBust = False
			break
			
	if hasBust == False:
		dealer.dealerTurn(c)

	'''
	first gotta check whether the player has BlackJack. if he does, pay him 3/2 odd bet. 
	then reset his BlackJack boolean to false again. otherwise, if he doesn't have BlackJack and the dealer card count
	is currently less than 21 after he finishes dealing, we need to compare the total of this particular player with the
	dealer. first check to see if the player busts, if not, then if player wins, give him money from determine amount 
	function. otherwise if it's a push, return his bet. otherwise, dealer wins, player goes home crying because of a lost bet. 
	otherwise (aka else), if player actually busts, dealer wins. now if the dealer busts for some reason, we need to 
	again make sure the players have not busted in order to not give the busted player sweet winnings. 
	'''
	for n in range(num):
		if player[n].isBlackJack() == True:
			player[n].addBankroll(player[n].getBetAmount() + (player[n].getBetAmount()*(float(3)/2)))
			print 'Player %s wins' %(player[n].name)
			player[n].resetBlackJack()
    
		elif dealer.getDealerTotal() <= 21:
			if player[n].getBust() == False:
				determine_winner = compare_total(dealer.getDealerTotal(),player[n].getCardTotal())
				if determine_winner == 2:
					determine_amount(player[n])						
					print 'Player %s wins' %(player[n].name)
				elif determine_winner == 0:
					if player[n].getDecision() == 'd':
						player[n].addBankroll(player[n].getBetAmount()*2)
					else:
						player[n].addBankroll(player[n].getBetAmount()) 
					print 'Push'
				else:
					print 'Dealer wins'

			else:
				print 'Dealer wins'  

		else:                
			if player[n].getBust() == False:
				print 'Player %s wins' %(player[n].name)
				determine_amount(player[n])
			else:
				print 'Dealer wins'  
						
## initialize the game by asking for player count, putting the players inside the list and then adding human/bot players
## to the list and also giving the players a 10 000 bank to worth with.

num_players = int(raw_input('Enter number of players'))
the_players_list = []
for num in range(num_players):
	is_AI = raw_input('Is he bot?: y for Yes n for No ')
	if is_AI.lower() == 'y':
		which_AI = raw_input('Who do you want to play against?: b for Beginner Joe, s for Steady Joe, w for Wild Joe and g for Good Joe')
		while which_AI.lower() != 's' and which_AI.lower() != 'b' and which_AI.lower() != 'w' and which_AI.lower() != 'g':
			which_AI = raw_input('Who do you want to play against?: b for Beginner Joe, s for Steady Joe, w for Wild Joe and g for Good Joe')
		if which_AI.lower() == 'b':
			the_players_list.append(BeginnerJoeBot('Beginner Joe', 10000))
		elif which_AI.lower() == 'w': 
			the_players_list.append(WildJoeBot('Wild Joe', 10000))		
		elif which_AI.lower() == 's':
			the_players_list.append(SteadyJoeBot('Steady Joe', 10000))
		else:
			the_players_list.append(GoodJoeBot('Good Joe', 10000))
	else:
		name = raw_input('Enter your name: ')
		the_players_list.append(Human(name, 10000))

## we need cards, so initialize the cards object with c, shuffle the cards and initialize the dealer object.	
c = Cards()
c.shuffle()
dealer = Dealer()

## while the game is going
while True:

## we start with the betting round
	for num in range(num_players):
		betting_round(the_players_list[num])

## if player 1 puts in no bets, game ends
	if the_players_list[0].getBetAmount() <= 0:
		break

## deal cards
	deal(dealer, c, the_players_list, num_players)

## print the output of the hidden card list
	print dealer.getHiddenHand()
	
## specifically for the GoodJoeBot, produce a face up card total
	dealer.produceFaceUpTotal()

## output the hands and who it belongs to
	for num in range(num_players):
		print 'name: %s, hand: %s' %(the_players_list[num].name, the_players_list[num].getHand())    

## player's turns, go through the for loop to make sure every player gets their turn. go through the decision tree
## of hitting, standing and doubling and output the player's current hand at the moment.
	for num in range(num_players):
		the_players_list[num].obtainDealerFaceCard(dealer)
		the_players_list[num].decisionTree(c)
		if the_players_list[num].getDecision() == 'd':
			print 'Doubled'
			print '%s Bet Amount: %s' %(the_players_list[num].name, the_players_list[num].getBetAmount()*2)
		the_players_list[num].subtractBankroll(the_players_list[num].getBetAmount())   
		print the_players_list[num].getHand()

## player's turns have ended, dealer's turn to play cards, first we need the dealer's current total, then 
## run determine winner function, which as the name implies determines who the winners are, this is also where 
## the dealer self deals the cards inside the function 
	dealer.produceDealerTotal()
	print "Dealer's hand: %s Count: %s" %(dealer.getHand(), dealer.getDealerTotal())
	determine_winner(the_players_list, num_players, dealer)

## getting ready for the next hand
## reset the hand, the card total and whether he busted or not for every player
	for num in range(num_players):
		print "%s's bank: %f" %(the_players_list[num].name, the_players_list[num].getBankroll())
		the_players_list[num].removeHand()
		the_players_list[num].resetCardTotal()
		the_players_list[num].resetBusted()

## reset the hand and card total for the dealer
	dealer.removeHand()    
	dealer.resetDealerTotal()

## determine deck penetration by decksize being 7 cards left times the number of players
## reset the deck to its full 4 deck play and shuffle it again.
	if c.checkDeckSize() < (7*num_players):
		c.resetDeck()
		c.shuffle()
