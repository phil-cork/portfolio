import java.util.Collections;
import java.util.Arrays;
import java.io.*;

public class Deck {
    public static final int MAXSIZE = 52;

    private Card[] deck;
    private int top;

    public Deck() {
        deck = new Card[MAXSIZE];
        initialize();
    }

    public void shuffle() {
        top = 0;
        Collections.shuffle(Arrays.asList(deck));
    }

    public Card deal() {
        if (top == MAXSIZE) {
            System.out.println("Error trying to deal from empty deck");
            System.exit(1);
        }
        return deck[top++];
    }

    public int size() {
        return MAXSIZE - top;
    }

    public void initialize() {
        final char[] suits = {'c', 'd', 'h', 's'};
        top = 0;
        for (int i = 0; i < MAXSIZE; i++) {
            deck[i] = new Card(i % 13, suits[i/13]);
        }
    }

    public void initializeRev() {
        final char[] suits = {'c', 'd', 'h', 's'};
        top = 0;
        for (int i = MAXSIZE-1; i >= 0; i--) {
            deck[i] = new Card(i % 13, suits[i/13]);
        }
    }

    public void writeOut(String filename) throws IOException {
        PrintWriter outstream = new PrintWriter(filename);
        outstream.println(this.toString());
        outstream.close();
    }


    public String toString() {
        String res = "";
        for (int i = top; i < Deck.MAXSIZE; i++)
        {
            res += deck[i].toString() + "\n";
        }
        return res;
    }
}
