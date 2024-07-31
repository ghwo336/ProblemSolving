import java.util.Scanner;
import java.math.BigInteger;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String a=scanner.nextLine();
        String  b=scanner.nextLine();
        BigInteger big1= new BigInteger(a);
        BigInteger big2= new BigInteger(b);
        BigInteger two = new BigInteger("2");
        System.out.println((big1.add(big2)).divide(two));
        System.out.println((big1.subtract(big2)).divide(two));
        
    }
}