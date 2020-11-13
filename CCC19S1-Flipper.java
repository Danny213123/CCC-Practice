import java.util.Scanner;

public class MyProgram
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        
        int[][] NumberGrid = new int[2][2];
        
        NumberGrid[0][0] = 1;
        NumberGrid[0][1] = 2;
        NumberGrid[1][0] = 3;
        NumberGrid[1][1] = 4;
        
        String Sequence = in.nextLine();
        
        for (int x = 0; x < Sequence.length(); x++){
            if (Sequence.substring(x, x+1).equals("H")){
                int tempGrid1 = NumberGrid[0][0];
                int tempGrid2 = NumberGrid[0][1];
                NumberGrid[0][0] = NumberGrid[1][0];
                NumberGrid[0][1] = NumberGrid[1][1];
                NumberGrid[1][0] = tempGrid1;
                NumberGrid[1][1] = tempGrid2;
            } else {
                int tempGrid1 = NumberGrid[0][1];
                int tempGrid2 = NumberGrid[1][1];
                NumberGrid[0][1] = NumberGrid[0][0];
                NumberGrid[1][1] = NumberGrid[1][0];
                NumberGrid[0][0] = tempGrid1;
                NumberGrid[1][0] = tempGrid2;
            }
        }
        
        System.out.println(NumberGrid[0][0] + " " + NumberGrid[0][1]);
        System.out.println(NumberGrid[1][0] + " " + NumberGrid[1][1]);
    }
