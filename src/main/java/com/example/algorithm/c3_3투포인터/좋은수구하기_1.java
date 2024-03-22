package com.example.algorithm.c3_3투포인터;

import java.util.Arrays;
import java.util.Scanner;

//1253번
public class 좋은수구하기_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);

        int count=0;
        int i = 0;
        int j = n-1;
        while(i<j){
            int goodnum = a[j];
            if(a[i]+a[j-1]==goodnum){
                count++;
                j--;
                i++;
            }else if(a[i]+a[j-1]>goodnum){
                i--;
            }else if(a[i]+a[j-1]<goodnum){
                j++;
            }
        }

        System.out.println(count);
    }
}
