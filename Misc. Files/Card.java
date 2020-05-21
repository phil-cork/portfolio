public class Card {

    private int rank;
    private char suit;

    public Card(int rank, char suit) {
        this.rank = rank;
        this.suit = suit;
    }

    public int getRank() {
        return rank;
    }

    public char getSuit() {
        return suit;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public void setSuit(char suit) {
        this.suit = suit;
    }

    public int compareTo(Card otherCard) {
        if (this.getRank() == otherCard.getRank()) return 0;
        else if (this.getRank() > otherCard.getRank()) return 1;
        else return -1;
    }

    public String toString() {
        final String[] rank_string = {"ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "jack","queen","king"};

        String result = rank_string[rank];

        if (suit == 'h')
            result += " of hearts";
        else if (suit == 'd')
            result += " of diamonds";
        else if (suit == 'c')
            result += " of clubs";
        else if (suit == 's')
            result += " of spades";

        return result;
    }
}
