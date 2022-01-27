import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int x=0;
        for(int i =0 ; i<str.length()-1 ; i++){ 
            if(str.charAt(i)==str.charAt(i+1)){
                x=x+1;
            }
        }
        System.out.println(x);
    }
}
