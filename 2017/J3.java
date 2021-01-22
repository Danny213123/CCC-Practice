import java.util.Scanner;

public class Sample {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        String InitialPosition = in.nextLine();
        String EndPosition = in.nextLine();
        int Battery = in.nextInt();

        String[] list1 = InitialPosition.split(" ");
        String[] list2 = EndPosition.split(" ");

        int distanceAvenue = Math.abs(Integer.parseInt(list1[0]) - Integer.parseInt(list2[0]));
        int distanceStreet = Math.abs(Integer.parseInt(list1[1]) - Integer.parseInt(list2[1]));

        int totalDistance = distanceAvenue + distanceStreet;

        if (totalDistance > Battery) {
            System.out.println("N");
        } else if (Battery % 2 == 1 && totalDistance % 2 == 1) {
            System.out.println("Y");
        } else if (Battery % 2 == 0 && totalDistance % 2 == 0) {
            System.out.println("Y");
        } else if (Battery % 2 == 1 && totalDistance % 2 == 0) {
            System.out.println("N");
        } else if (Battery % 2 == 0 && totalDistance % 2 == 1) {
            System.out.println("N");
        }
    }
}
