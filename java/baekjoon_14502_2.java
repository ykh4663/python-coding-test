import java.io.*;
import java.util.*;

//※자바 언어는 파이썬 처럼 combinations를 지원하지 않기 때문에 for문을 통해 해결해야 한다

public class Main {
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};//전역변수 설정

    private int count(int [][] graph, int n, int m){
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(graph[i][j] == 0){
                    cnt+=1;
                }
            }
        }
        return cnt;
    }

    private void bfs(int[][] graph, int[][] visit, int sx, int sy, int n, int m){
        ArrayDeque<int[]>deque = new ArrayDeque<>();//poll과 add를 이용 queue이므로
        deque.add(new int[]{sx, sy});//add 시에 다음과 같은 형태로 넣기
        visit[sx][sy] = 1;
        while(!deque.isEmpty()){
            int[] xy = deque.poll();//0번 원소가 x, 1번 원소가 y 좌표
            int x = xy[0];
            int y = xy[1];
            for(int k = 0; k < 4; k++)
            {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(0<=nx && nx < n && 0<=ny && ny<m){
                    if(visit[nx][ny] == 0 && graph[nx][ny] == 0){
                        graph[nx][ny] = 2;
                        visit[nx][ny] = 1;
                        deque.add(new int[]{nx, ny});
                    }
                }
            }

        }
    }
    

    private int count_safe(int [][] graph, int n, int m){
        int [][] visit = new int[n][m];//c언어와 다르게 선언 시 배열 둘 다 값 지정 안해도 ㄱㅊ
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(graph[i][j] == 2 && visit[i][j] == 0){
                    bfs(graph, visit, i, j, n, m);
                }
            }
        }

        return count(graph,n,m);

    }
    
    private int[][] copy_lab(int[][] lab, int n, int m){
    	int[][] tmp = new int[n][m];	
    	for(int i = 0; i < n; i++) {
    		System.arraycopy(lab[i], 0, tmp[i], 0, m);//파이썬과 다르게 행 단위로 arraycopy 해줘야 함
    	}
    	return tmp;
    }

	public int solution(int n, int m, int[][] lab) {
        List<int[]> empties = new ArrayList<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(lab[i][j] == 0){
                    empties.add(new int[]{i,j});//리스트에 값 넣을 때는 add
                }
            }
        }
        
        int result = 0;
        int e_size = empties.size();
        for(int i = 0; i < e_size-2; i++){
            for(int j = i+1; j < e_size-1; j++){
                for(int k = j+1; k< e_size; k++){
                    int [][] tmp = copy_lab(lab, n,m);

                    int [] w1 = empties.get(i);//리스트 값 가져올 때는 get
                    int [] w2 = empties.get(j);
                    int [] w3 = empties.get(k);

                    tmp[w1[0]][w1[1]] = 1;
                    tmp[w2[0]][w2[1]] = 1;
                    tmp[w3[0]][w3[1]] = 1;

                    int local_result = count_safe(tmp, n, m);
                    result = Math.max(result, local_result);


                }
            }
        }

        return result;
		
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