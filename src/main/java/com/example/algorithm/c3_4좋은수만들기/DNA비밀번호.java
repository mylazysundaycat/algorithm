package com.example.algorithm.c3_4좋은수만들기;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//12891
public class DNA비밀번호 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        //DNA 문자열
        char[] DNA = new char[S];
        DNA = bf.readLine().toCharArray();

        //부분 문자열에 포함돼야할 A,C,G,T 갯수
        int[] dnaNum = new int[4];
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 4; i++) {
            dnaNum[i] = Integer.parseInt(st.nextToken());
        }
        int start=0;
        int end =P;
        int result=0;

        while(start<=S-P){
            int[] checkNum = new int[4];
            for(int i=start; i<end; i++){
                if(DNA[i] == 'A'){
                    checkNum[0]++;
                } else if(DNA[i] == 'C') {
                    checkNum[1]++;
                } else if(DNA[i] == 'G') {
                    checkNum[2]++;
                } else if(DNA[i] == 'T') {
                    checkNum[3]++;
                }
            }
            //검증
            if(checkNum[0]==dnaNum[0] && checkNum[1]==dnaNum[1] &&
            checkNum[2]==dnaNum[2] && checkNum[3]==dnaNum[3]){
                result++;
            }
            start++;
            end++;
        }

        System.out.println(result);

    }
}
