package p6Coding;

public class HandEvaluatorBBXP {
	//ALL OF THESE ARE PASSED AN ARRAY OF LENGTH 5

	
	
	//Cluster 1: Think about how a helper might be useful for these...
	public static boolean hasPair(Card[] cards) {
		if(cards[0].getValue() == cards[1].getValue() || cards[0].getValue() == cards[2].getValue() || cards[0].getValue() == cards[3].getValue() || cards[0].getValue() == cards[4].getValue() || cards[1].getValue() == cards[2].getValue() || cards[1].getValue() == cards[3].getValue() || cards[1].getValue() == cards[4].getValue() || cards[2].getValue() == cards[3].getValue() || cards[2].getValue() == cards[4].getValue() || cards[3].getValue() == cards[4].getValue()){
			return true;
		}else{
			return false;
		}
	}

	public static boolean hasThreeOfAKind(Card[] cards) {
		for(int i = 0; i < 5; i++){	
				if(cards[i].getValue() == cards[].getValue()){
					return true; 
				}else{
					return false;
				}
		}
	}

	public static boolean hasFourOfAKind(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}

	public static boolean hasFiveOfAKind(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}



	//Cluster 2
	public static boolean hasRainbow(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}

	public static boolean hasStraight(Card [] cards) {
		throw new RuntimeException("You need to implement this...");
	}

	public static boolean hasFlush(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}




	//Cluster 3: Think about how to make use of existing methods to
	//           make the following ones easier to write...
	public static boolean hasStraightRainbow(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}

	public static boolean hasStraightFlush(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}

	public static boolean hasTwoPair(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}




	//Challenge
	public static boolean hasFullHouse(Card[] cards) {
		throw new RuntimeException("You need to implement this...");
	}




}

