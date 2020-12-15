import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.NumberFormatException;
import java.util.Hashtable;

class Main {
  public static void main(String[] args) throws IOException{

    String line = " ";
    Integer current_square = 1;
    Hashtable<Integer, Integer> Snake = new Hashtable<>();
    Hashtable<Integer, Integer> Ladder = new Hashtable<>();
    

    Snake.put(54, 19); Snake.put(90, 48); Snake.put(99, 77);
    Ladder.put(9, 34); Ladder.put(40, 64); Ladder.put(67, 86);

    while (line.length() > 0){
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

      line = (reader.readLine());

      if (Integer.parseInt(line) == 0){
        System.out.println("You Quit!");
        System.exit(0);
      }

      if (current_square + Integer.parseInt(line) < 100){
        current_square += Integer.parseInt(line);
      } else if (current_square + Integer.parseInt(line) == 100){
        System.out.println("You Win!");
        System.exit(0);
      } else {
        current_square += 0;
      }

      Integer s = Snake.get(current_square);
      Integer l = Ladder.get(current_square);
      
      if (s != null){
        current_square = s;
      } else if (l != null){
        current_square = l;
      }
      System.out.println("You're now on square " + current_square);
    }
  }
}
