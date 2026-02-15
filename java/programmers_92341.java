import java.io.*;
import java.util.*;
class Solution {
    	private int convertTime(String time) {
    		String[] parts = time.split(":");
    		int h = Integer.parseInt(parts[0]);
    		int m = Integer.parseInt(parts[1]);
    		
    		return h * 60 + m;
    		
    	}


        public int[] solution(int[] fees, String[] records) {
            int defaultTime = fees[0];
            int defaultFee = fees[1];
            int perTime = fees[2];
            int perFee = fees[3];
            
            Map<String, Integer> inMap = new HashMap<>();
            Map<String, Integer> total = new HashMap<>();
            
            for(String r : records) {
            	String[]parts = r.split(" ");
            	String time = parts[0];
            	String carNum = parts[1];
            	String action = parts[2];
            	
            	int cur = convertTime(time);
            	
            	if(action.equals("IN")) {
            		inMap.put(carNum, cur);
            	}
            	else {
            		int prev = inMap.remove(carNum);
            		int diff = cur - prev;
            		total.put(carNum, total.getOrDefault(carNum, 0) + diff);
            		
            	}
            	
            }
            
            int end = convertTime("23:59");
            for(Map.Entry<String, Integer> e : inMap.entrySet()) {
            	String car = e.getKey();
            	int inTime = e.getValue();
            	total.put(car, total.getOrDefault(car, 0) + (end - inTime));
            }
            
            List<String> cars = new ArrayList<>(total.keySet());
            Collections.sort(cars);
            
            int[] answer = new int[cars.size()];
            int idx = 0;
            for(String car: cars) {
            	int cum = total.get(car);
            	if(cum <= defaultTime)
            	{
            		answer[idx++] = defaultFee;
            		
            	}
            	else {
            		int extra = cum - defaultTime;
            		int units = (extra + perTime - 1) / perTime;
            		answer[idx++] = defaultFee + units * perFee;
            	}
            }
            return answer;
            
            
        }
}