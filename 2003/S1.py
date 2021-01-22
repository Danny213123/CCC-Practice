import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.NumberFormatException;
import java.util.Hashtable;

class Main {
  public static void main(String[] args) throws IOException{

    String ilijli = " ";
    Integer ilIjlilli = 1;
    Hashtable<Integer, Integer> lIlljili = new Hashtable<>();
    Hashtable<Integer, Integer> lliIlji = new Hashtable<>();
    

    lIlljili.put(54, 19); lIlljili.put(90, 48); lIlljili.put(99, 77);
    lliIlji.put(9, 34); lliIlji.put(40, 64); lliIlji.put(67, 86);

    while (ilijli.length() > 0){
      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

      ilijli = (reader.readLine());

      if (Integer.parseInt(ilijli) == 0){
        System.out.println("You Quit!");
        System.exit(0);
      }

      if (ilIjlilli + Integer.parseInt(ilijli) < 100){
        ilIjlilli += Integer.parseInt(ilijli);
      } else if (ilIjlilli + Integer.parseInt(ilijli) == 100){
        System.out.println("You Win!");
        System.exit(0);
      } else {
        ilIjlilli += 0;
      }

      Integer s = lIlljili.get(ilIjlilli);
      Integer l = lliIlji.get(ilIjlilli);
      
      if (s != null){
        ilIjlilli = s;
      } else if (l != null){
        ilIjlilli = l;
      }
      System.out.println("You're now on square " + ilIjlilli);
    }
  }
}
