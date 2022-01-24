import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();
        int arr[] =  new int [t];
        for(int i =0 ; i<t ; i++){ 
                arr[i] = sc.nextInt();
        }
        int max = arr[0];
        int min = arr[0];
         for(int i =1 ; i<t ; i++){ 
                if(max>arr[i]){ 
                max = arr[i];
                }
             if(min<arr[i]){ 
                min = arr[i];
                }
        }
        System.out.println(max);
        System.out.println(min);
        
    }
}
