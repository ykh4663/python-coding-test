import java.io.*;
import java.util.*;

class Solution {
    public int solution(String s) {
        int s_len = s.length();
        int result = s_len;
        for(int i = 1; i <= s_len / 2; i++){
            int cnt = 1;
            String elem = s.substring(0,i);
            StringBuilder sb = new StringBuilder();
            String new_elem = "";
            int idx = 0;
            for(int j = i; j < s_len; j+=i){
                if(j+i > s_len){
                    new_elem = s.substring(j,s_len);//stringbuilder 자를 때는 ,로 자름 파이썬 : 와 헷갈리는 거 주의
                }
                else{
                    new_elem = s.substring(j,j+i);
                }
                
                if(!elem.equals(new_elem)){//문자열은 equals함수로 요소 값 비교 가능
                    if(cnt == 1){
                        sb.append(elem);
                    }
                    else{
                        sb.append(cnt).append(elem);
                    }
                    elem = new_elem;
                    cnt = 1;
                    idx+= (elem.length() * cnt);//idx를 매번 최신화해주고 있는데 그러기보다 마지막에 그냥 남은 값에 대해서 따로 처리해주면됨 cnt 값이 1인지 1초과인지에 따라서
                }
                else{
                    cnt+=1;
                }
            }
            if(idx != s_len){
                if(cnt != 1){
                    sb.append(cnt).append(new_elem);
                }
                else{
                    sb.append(new_elem);
                }
            }
            int local_result = sb.length();
            result = Math.min(result, local_result);//min 비교 시 Math.min
        }
        return result;
    }
}