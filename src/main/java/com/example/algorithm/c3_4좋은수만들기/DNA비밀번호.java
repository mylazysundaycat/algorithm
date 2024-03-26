package com.example.algorithm.c3_4좋은수만들기;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//12891
public class DNA비밀번호 {

    static int[] myArr = new int[4];
    static int[] checkArr = new int[4];
    static int result = 0;
    static char[] A;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        A = bf.readLine().toCharArray();

        //부분 문자열에 포함돼야할 A,C,G,T 갯수
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 4; i++) {
            checkArr[i] = Integer.parseInt(st.nextToken());
        }
        //초기 배열 P 처리부분
        for (int i = 0; i < P; i++) {
            add(A[i]);
        }
        if (validate()) {
            result++;
        }

        //슬라이딩 윈도우
        for(int i=P; i<S; i++){
            int j = i-P;
            //더하기
            add(A[i]);
            //빼기
            remove(A[j]);
            if(validate()) result++;
        }
        System.out.println(result);
        bf.close();
    }




    private static void add(char c) {
        switch(c){
            case 'A':
                myArr[0]++;
                break;
            case 'C':
                myArr[1]++;
                break;
            case 'G':
                myArr[2]++;
                break;
            case 'T':
                myArr[3]++;
                break;
        }
    }
    private static void remove(char c) {
        switch(c){
            case 'A':
                myArr[0]--;
                break;
            case 'C':
                myArr[1]--;
                break;
            case 'G':
                myArr[2]--;
                break;
            case 'T':
                myArr[3]--;
                break;
        }
    }

    private static boolean validate(){
        for (int i = 0; i < 4; i++) {
            if (myArr[i] < checkArr[i])
                return false;
        }
        return true;
    }
}
