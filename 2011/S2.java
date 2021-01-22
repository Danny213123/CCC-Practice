
public class MyProgram
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner (System.in);
        
        int Inputs = in.nextInt();
        Inputs *= 2;
        
        String[] Answers = new String[Inputs + 1];
        
        for (int y = 0; y <= Inputs; y++){
            Answers[y] = in.nextLine();
        }
        
        int correct = 0;
        
        for (int x = 0; x <= Inputs/2; x++){
            if (Answers[x].equals(Answers[x + (Inputs / 2)])){
                correct += 1;
            }
        }
        System.out.println(correct);
    }
}
