package com.example.algorithm.c3_3투포인터;

import java.util.Scanner;

public class 연속된자연수의합구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int count = 1;
        int start_index = 1;
        int end_index = 1;
        int sum = 1;
        while(end_index != N) {
            if (sum == N) {
                count++;
                end_index++;
                sum = sum+end_index;
            }else if(sum>N) {
                sum = sum-start_index;
                start_index++;
            } else if (sum < N) {
                end_index++;
                sum=sum+end_index;
            }
        }
        System.out.println(count);
    }
}
