package com.example.algorithm.c3_3투포인터;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 좋은수구하기_2 {
    public static void main(String[] args) throws IOException {
        //BufferdReader: 문자 입력 스트림을 버퍼링하여 텍스트 한 줄씩 읽을 수 있는 클래스
        //InputStreamReader: 바이트 스트림을 문자 스트림으로 변환하는 브릿지입니다.
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] A = new int[N];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        int count=0;
        int i = 0;
        int j = N-1;
        while(i<j){
            int goodnum = A[j];
            if(A[i]+A[j-1]==goodnum){
                count++;
                j--;
                i++;
            }else if(A[i]+A[j-1]>goodnum){
                i--;
            }else if(A[i]+A[j-1]<goodnum){
                j++;
            }
        }

        System.out.println(count);

    }
}
