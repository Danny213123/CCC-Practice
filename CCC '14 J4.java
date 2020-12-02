import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class MyProgram {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        ArrayList<Integer> choresMinutes = new ArrayList<>();

        int availableMinutes = in.nextInt();
        int amountChores = in.nextInt();

        int counter = 0;
        
        for (int i = 0; i<amountChores; i++){
            choresMinutes.add(in.nextInt());
        }
        
        Collections.sort(choresMinutes);
        
        for (int k = 0; k<amountChores; k++){
            if(availableMinutes - choresMinutes.get(k) >= 0){
                counter++;
                availableMinutes -= choresMinutes.get(k);
            }
        }
    
        System.out.println(counter);

    }
}
