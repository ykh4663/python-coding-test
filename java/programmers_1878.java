import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(int[][] v) {
        int [] answer = new int[2];
        Map<Integer,Integer>rows = new HashMap<>();
        Map<Integer,Integer>cols = new HashMap<>();
        for(int i = 0; i < 3; i++)
        {
            rows.put(v[i][0], rows.getOrDefault(v[i][0], 0)+1);//put
            cols.put(v[i][1], cols.getOrDefault(v[i][1], 0)+1);
        }
        
        for(Map.Entry<Integer, Integer> r : rows.entrySet()){//Map.Etry<> 꺼낼때는 entrySet()
            int x = r.getKey();//key value값 각각 getKey, getValue로
            int cnt = r.getValue();
            if(cnt == 1){
                answer[0] = x;
            }
        }
        
        for(Map.Entry<Integer, Integer> c : cols.entrySet()){
            int y = c.getKey();
            int cnt = c.getValue();
            if(cnt == 1){
                answer[1] = y;
            }
        }
        

        

        return answer;
    }
}