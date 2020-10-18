//https://www.hackerrank.com/challenges/the-quickest-way-up/problem

/*

Markov takes out his Snakes and Ladders game, stares at the board and wonders: "If I can always roll the die to whatever number I want, what would be the least number of rolls to reach the destination?"

Rules The game is played with a cubic die of
faces numbered to

.

    Starting from square land on square with the exact roll of the die. If moving the number rolled would place the player beyond square

    , no move is made.

    If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.

    If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.



*/

#include <bits/stdc++.h>
#define SIZE 100

using namespace std;

vector<vector<bool>> graph;
unordered_map<int,int> short_circuit;
vector<bool> visited;

void print_graph(){
	for(int i = 0;i<SIZE;i++){
		for(int j = 0;j<SIZE;j++){
			cout<<graph[i][j]<<" ";
		}
		cout<<"\n";
	}
	cout<<"\n";
}

int bfs(){
	
	queue<pair<int,int>> q;
	pair<int,int> p;

	q.push({0,0});
	visited[0] = true;

	int ans = -1;
	bool flag = false;

	while(!q.empty()){

		p = q.front();
		q.pop();

		if(p.first == SIZE - 1){
			ans = p.second;
			break;
		}

		for(int i = 0;i<SIZE;i++){

			if(visited[i]==false && graph[p.first][i] && i != p.first){
				visited[i] = true;
				if(short_circuit.find(i)!=short_circuit.end())
					q.push({short_circuit[i],p.second+1});
				else	
					q.push({i,p.second+1});
			}

		}

		if(flag)
			break;

	}

	return ans;
}

int quickestWayUp(vector<vector<int>> ladders, vector<vector<int>> snakes) {

	short_circuit.clear();

	visited.clear();
	visited.resize(SIZE,false);

	graph.clear();
	graph.resize(SIZE,vector<bool>(SIZE,false));

	for(int i = 0;i<ladders.size();i++){
		graph[ladders[i][0]][ladders[i][1]] = true;
		short_circuit[ladders[i][0]] = ladders[i][1];
	}

	for(int i = 0;i<snakes.size();i++){
		graph[snakes[i][0]][snakes[i][1]] = true;
		short_circuit[snakes[i][0]] = snakes[i][1];
	}

	for(int i = 0;i<SIZE;i++){
		for(int j = i+1;j<SIZE && j <= i+6 ;j++){
			graph[i][j] = true;
		}
	}

	return bfs();
}

int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	graph.clear();
	graph.resize(SIZE,vector<bool>(SIZE,false));
	
	vector<vector<int>> ladders;
	vector<vector<int>> snakes;

	int t,n,m,temp1,temp2;
	cin>>t;

	while(t--){

		cin>>n;

		ladders.clear();
		snakes.clear();
		

		for(int i = 0;i<n;i++){
			cin>>temp1>>temp2;
			ladders.push_back({temp1-1,temp2-1});
		}

		cin>>m;

		for(int i = 0;i<m;i++){
			cin>>temp1>>temp2;
			snakes.push_back({temp1-1,temp2-1});
		}

		cout<<quickestWayUp(ladders,snakes)<<"\n";
	}

	return 0;
}