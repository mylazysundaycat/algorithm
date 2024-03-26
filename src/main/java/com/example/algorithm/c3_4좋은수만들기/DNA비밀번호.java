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

        int result = 0;

        char[] A = bf.readLine().toCharArray();
        int[] checkarr = new int[4];
        int[] myArr = new int[4];
        int checkSecret=0;

        //부분 문자열에 포함돼야할 A,C,G,T 갯수
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 4; i++) {
            checkarr[i] = Integer.parseInt(st.nextToken());
            if(checkarr[i]==0) checkSecret++;
        }


        //초기 배열 P 처리부분
        for (int i = 0; i < P; i++) {
            switch(A[i]){
                case 'A':
                    myArr[0]++;
                    if(myArr[0]==checkarr[0]) checkSecret++;
                    break;
                case 'C':
                    myArr[1]++;
                    if(myArr[1]==checkarr[1]) checkSecret++;
                    break;
                case 'G':
                    myArr[2]++;
                    if(myArr[2]==checkarr[2]) checkSecret++;
                    break;
                case 'T':
                    myArr[3]++;
                    if(myArr[3]==checkarr[3]) checkSecret++;
                    break;
            }
        }

        //슬라이딩 윈도우
        for(int i=P; i<S; i++){
            int j = i-P;
            //더하기
            switch(A[i]){
                case 'A':
                    myArr[0]++;
                    if(myArr[0]==checkarr[0]) checkSecret++;
                    break;
                case 'C':
                    myArr[1]++;
                    if(myArr[1]==checkarr[1]) checkSecret++;
                    break;
                case 'G':
                    myArr[2]++;
                    if(myArr[2]==checkarr[2]) checkSecret++;
                    break;
                case 'T':
                    myArr[3]++;
                    if(myArr[3]==checkarr[3]) checkSecret++;
                    break;
            }
            //빼기
            switch(A[j]){
                case 'A':
                    if(myArr[0]==checkarr[0]) checkSecret--;
                    myArr[0]--;
                    break;
                case 'C':
                    if(myArr[1]==checkarr[1]) checkSecret--;
                    myArr[1]--;
                    break;
                case 'G':
                    if(myArr[2]==checkarr[2]) checkSecret--;
                    myArr[2]--;
                    break;
                case 'T':
                    if(myArr[3]==checkarr[3]) checkSecret--;
                    myArr[3]--;
                    break;
            }
            if(checkSecret==4) result++;
        }
        System.out.println(result);
        bf.close();


    }
}
