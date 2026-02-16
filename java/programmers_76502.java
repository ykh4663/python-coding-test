import java.io.*;
import java.util.*;.//자바 코테 잘 모르니깐 그냥 이거 두개 일단 임포트하고 시작하기

class Solution {
    private boolean isPush(char elem){
        if(elem == '{' || elem == '(' || elem == '['){
            return true;
        }
        return false;
    }
    
    private boolean isPair(char c1, char c2){
        if(c1 == '{'){
            if(c2 == '}'){
                return true;
            }
        }
        else if(c1 == '('){
            if(c2 == ')'){
                return true;
            }
        }
        else{
            if(c2 == ']'){
                return true;
            }
        }
        return false;
    }
    public int solution(String s) {
        int result = 0;
        int s_len = s.length();
        
        for(int x = 0; x < s_len; x++){
            ArrayDeque<Character> deque = new ArrayDeque<>(); //주의점1: Character로 받아야 한다, for 문 안에서 초기화 안하면 스택에 요소 값 남아 있을 때 오류 발생함
            int gOrStop = 0;
            StringBuilder sb = new StringBuilder();
            sb.append(s.substring(x,s_len)).append(s.substring(0,x));//주의점2 : StringBuilder로 매번 계산할 문자열 최신화하기
            String new_s = sb.toString();//주의점3: s에 최신화하면 문자열이 계속 바뀌니깐 지금처럼 new_s를 하든 아니면 그냥 x대신 1로 제한시키면서 s값 최신화하는 것도 방법 될듯
            for(int i = 0; i < s_len; i++){
                
                char elem = new_s.charAt(i);//주의점4: 문자열 꺼낼 때는 charAt로
                if(isPush(elem)){
                    deque.push(elem);//주의점5: push pop 스택은 이렇게 하고 queue의 경우에는 add poll 쓰면 됨
                }
                else{
                    if(deque.isEmpty()){
                        gOrStop = 1;
                        break;
                    }
                    char prev_elem = deque.pop();
                    if(!isPair(prev_elem, elem)){
                        gOrStop = 1;
                        break;
                    }
                }
                
            }
            if(gOrStop == 0){
                if(deque.isEmpty()){//주의점6: 비어있지 않다면 닫는 괄호가 안나온 것이므로 result에 추가시키면 안됨
                    result+=1;
                }
            }
        }
        return result;
    }
}