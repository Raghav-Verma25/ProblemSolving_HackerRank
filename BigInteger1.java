
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
           Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        BigInteger num1 = new BigInteger(a);
        BigInteger num2 = new BigInteger(b);
        BigInteger c = num1.add(num2);
        BigInteger d = num1.multiply(num2);
        System.out.println(c);
        System.out.println(d);
    }
}
