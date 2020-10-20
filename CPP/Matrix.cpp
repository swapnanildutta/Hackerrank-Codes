//https://www.hackerrank.com/challenges/matrix/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs&isFullScreen=true

/*

The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.

Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, determine the minimum time to stop the attack.

*/

#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

vector<vector<int>> graph;
vector<bool> visited;
unordered_map<int,bool> is_machine;
int cost = 0;

void create_graph(vector<vector<int>>& roads){

    for(int i = 0;i<roads.size();i++){
        graph[roads[i][0]][roads[i][1]] = roads[i][2];
        graph[roads[i][1]][roads[i][0]] = roads[i][2];
    }
}

void dfs(vector<int>& machines, int parent, int dest, int min_weight, int min_parent, int min_dest){

    // cout<<"dfs\n";

    visited[dest] = true;

    if(is_machine.find(dest)!=is_machine.end()){

        if(graph[parent][dest] < min_weight){
            cost += graph[parent][dest];
            graph[parent][dest] = 0;
        }
        else{
            cost += graph[min_parent][min_dest];
            graph[min_parent][min_dest] = 0;
        }
    }

    for(int i = 0;i<graph[dest].size();i++){

        if(graph[dest][i] != 0 && visited[i] == false){

            if(graph[dest][i] < min_weight)
                dfs(machines,dest,i,graph[dest][i],dest,i);
            else
                dfs(machines,dest,i,min_weight,min_parent,min_dest);
        }
    }

}


int minTime(int n, vector<vector<int>> roads, vector<int> machines) {

    graph.clear();
    graph.resize(n,vector<int>(n,0));

    visited.clear();
    visited.resize(n,false);

    cost = 0;
    create_graph(roads);

    for(int i = 0;i<machines.size();i++){
    
        visited[machines[i]] = true;

        for(int j = 0;j<graph[machines[i]].size();j++){

            if(graph[machines[i]][j] != 0 && visited[j] == false){

                dfs(machines, machines[i],j,graph[machines[i]][j], machines[i],j);
            }

        }

    }

    return cost;
}

int main()
{
    freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);

    int n,k;
    cin>>n>>k;

    vector<vector<int>> roads(n-1);

    for (int i = 0; i < n-1; i++){
        roads[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> roads[i][j];
        }
    }

    vector<int> machines(k);

    for (int i = 0; i < k; i++) {
        int machines_item;
        cin >> machines_item;
        is_machine[machines_item] = true;
        machines[i] = machines_item;
    }

    int result = minTime(n, roads, machines);

    cout << result << "\n";


    return 0;
}