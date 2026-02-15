import java.io.*;
import java.util.*;

public class Main {
	static final int[] dx = {1,-1,0,0};
	static final int[] dy = {0,0,1,-1};
	
	private int[][] copy_lab(int [][] lab, int n, int m){
		int[][] tmp = new int[n][m];
		for(int i = 0; i < n; i++) {
			System.arraycopy(lab[i], 0, tmp[i], 0, m);
		}
		return tmp;
	}
	
	private void bfs(int [][] tmp, int [][] visit, int s_x, int s_y, int n, int m) {
		ArrayDeque<int[]>q = new ArrayDeque<>();
		q.add(new int[] {s_x, s_y});
		visit[s_x][s_y] = 1;
		while(!q.isEmpty()) {
			int[]cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			for(int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				
				if(0<=nx && nx < n && 0<=ny && ny<m) {
					if(tmp[nx][ny] == 0) {
						tmp[nx][ny] = 2;
						visit[nx][ny] = 1;
						q.add(new int[] {nx, ny});
					}
				}
			}
			
		}
		
	}
	
	private void spreadVirus(int [][] tmp, int n, int m) {
		
		int [][] visit = new int[n][m];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(tmp[i][j] == 2 && visit[i][j] == 0) {
					bfs(tmp, visit, i, j, n,m);
				}
			}
		}
	}
	
	private int countSafe(int [][] tmp, int n, int m) {
		int count = 0;
	
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(tmp[i][j] == 0) {
					count+=1;
				}
			}
		}
		return count;
	}
	
	public int solution(int n, int m, int[][] lab) {
	
	
		List<int[]> empties = new ArrayList<>();
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(lab[i][j] == 0) {
					empties.add(new int[] {i,j});//왜 set 형태{} 쓰는건
				}
				
			}
		}
		int maxSafe = 0;
		int eSize = empties.size();
		for(int i = 0; i < eSize - 2; i++) {
			for(int j = i+1; j < eSize-1; j++) {
				for(int k = j+1; k < eSize; k++) {
					
					int[][] tmp = copy_lab(lab, n, m);
					
					int[] w1 = empties.get(i);
					int[] w2 = empties.get(j);
					int[] w3 = empties.get(k);
					tmp[w1[0]][w1[1]] = 1;
					tmp[w2[0]][w2[1]] = 1;
					tmp[w3[0]][w3[1]] = 1;
					
					spreadVirus(tmp, n, m);
					int safe = countSafe(tmp, n, m);
					
					if(safe > maxSafe) {
						maxSafe = safe;
					}
					
					
					
				}
			}
		}
		
		return maxSafe;
			
		
	}
	
	public static void main(String[] args) throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st = new StringTokenizer(br.readLine());

	    int n = Integer.parseInt(st.nextToken());
	    int m = Integer.parseInt(st.nextToken());

	    int[][] lab = new int[n][m];
	    for (int i = 0; i < n; i++) {
	        st = new StringTokenizer(br.readLine());
	        for (int j = 0; j < m; j++) {
	            lab[i][j] = Integer.parseInt(st.nextToken());
	        }
	    }

	    Main solver = new Main();
	    int ans = solver.solution(n, m, lab);
	    System.out.println(ans);
	}
}