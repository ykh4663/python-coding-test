class Solution {
    private String convert(int n, int k) {
		StringBuilder sb = new StringBuilder();
		while(n > 0) {
			sb.append(n % k);
			n /=k;
		}
		return sb.reverse().toString();
	}
	
	private boolean isPrime(String part) {
		long elem = Long.parseLong(part);//java는 파이썬과 달리 int long 범위에 따라서 값 변경 안해주면 런타임 에러 뜨기에 주의할 것
		
		if(elem < 2) {
			return false;
		}
		
		for(long i = 2; i*i <= elem; i++) {
			if(elem % i == 0) {
				return false;
			}
		}
		return true;
		
		
	}
	
	
	public int solution(int n, int k) {
		String num = convert(n,k);
		int l = num.length();
		
		int idx = 0;
		int cnt = 0;
		
		for(int i =0; i < l; i++) {
			if(num.charAt(i) == '0') {
				int newIdx = i;
				if(idx != newIdx) {
					String part = num.substring(idx, newIdx);
					if(isPrime(part)) {
						cnt+=1;
					}
				}
				
				idx = newIdx+1;
			}
		}
		
		if(idx < l) {
			String part = num.substring(idx, l);
			if(isPrime(part)) {
				cnt+=1;
			}
		}
		return cnt;
	
	}
	
	
	
	
}