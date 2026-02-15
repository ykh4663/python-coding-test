class Solution {
    public int solution(String s) {
        int n = s.length();
        int result = n;
        
        for(int i = 1; i <= n/2; i++) {
        	StringBuilder ans = new StringBuilder();
        	
        	String prev = s.substring(0,i);
        	int cnt = 1;
        	
        	for(int j = i; j < n; j+=i) {
        		int end = Math.min(j+i, n);
        		String cur = s.substring(j,end);
        		
        		if(!prev.equals(cur)) {
        			if(cnt == 1) {
        				ans.append(prev);
        			}
        			else {
        				ans.append(cnt).append(prev);
        			}
        			prev = cur;
        			cnt = 1;
        		}
        		else {
        			cnt+=1;
        		}
        	}
        	
        	if(cnt == 1) {
        		ans.append(prev);
        	}
        	else {
        		ans.append(cnt).append(prev);
        	}
        	
        	result = Math.min(result, ans.length());
        }
        
        return result;
    }
    
}