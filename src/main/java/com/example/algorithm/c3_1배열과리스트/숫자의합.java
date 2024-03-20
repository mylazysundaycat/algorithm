package com.example.algorithm.c3_1배열과리스트;

import java.util.Scanner;

//백준 11720
public class 숫자의합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //숫자의 개수 입력
        int N = sc.nextInt();
        //공백없이 주어진 N개의 숫자
        String sNum = sc.next();
        char[] cNum = sNum.toCharArray();

        int sum = 0;
        for(int i=0; i<cNum.length; i++){
            sum += cNum[i]-'0';
        }
        System.out.println(sum);
    }
}
