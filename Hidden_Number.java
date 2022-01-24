import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();
        int sum =0;
        int arr[] =  new int [t];
        for(int i =0 ; i<t ; i++){ 
                arr[i] = sc.nextInt();
            sum = sum+arr[i];
        }
        if(sum%t==0){ 
        System.out.println(sum/t);
        }
        else{ 
        System.out.println("-1");
        }
        
    }
}
