package p6Coding;

import java.util.ArrayList;

public class Deck {

	//YOU NEED TO USE THIS ARRAYLIST<CARD> TO HOLD THE DECK
	//  YOU CANNOT USE REGULAR ARRAYS IN THIS CLASS OTHER THAN
	//  IN THE DEAL METHOD, WHICH NEEDS TO RETURN AN ARRAY
	
	private ArrayList<Card> cards;

	public Deck() {
		cards = new ArrayList<Card>();
		for(int i = 0; i < 5; i++){
			for (int j = 1; j < 10; j++){
				cards.add(new Card(j, i));
			}
		}
	}

	public Deck(Deck other) {
		cards = new ArrayList<Card>(other.cards);
	}

	public Card getCardAt(int position) {
		Card specifiedCard = cards.get(position);
		return specifiedCard;
	}

	public int getNumCards() {
		int numberCards = cards.size();
		return numberCards;
	}


	public Card[] deal(int numCards) {
		Card[] deal = new Card[numCards];
		for(int i = 0; i < numCards; i++){
			deal[i] = cards.get(0);
			cards.remove(0);
		}
		return deal;
	}


	public void cut(int position) {
		
	}
	
	public void shuffle() {
		
	}
	

}
