#include <iostream>
#include <cstdio>

using namespace std;

#define FOR(i, j, k, in) for (int i=j ; i<=k ; i+=in)
#define IF(i, j) if (i == auto j)
#define print(a, b, c) cout << a << " " << b << " " << c << "\n"

int main() {

  ios_base::sync_with_stdio (false);

	int ROW, COL, SIZE;

	// Row and Col of the 2d array

	cin >> ROW;
	cin >> COL;

	// total size of the array, also the target ( end of array )

	SIZE = ROW * COL;

	int graph[ROW+1][ROW+1];

	// Initialize the array with inputed elements

	FOR(x, 1, ROW, 1){
		FOR(y, 1, COL, 1){
			cin >> graph[x][y];
		}
	}

	bool visited[1000001];
	int possible_path[SIZE];
	int current_pos = 0;
	int possible_path_pos = 0;
	int graph_pos;

	// Initialize possible path array
	FOR(x, 0, SIZE+1, 1){
		possible_path[x] = -1;
	}

	// First element in queue is the first element of graph
	possible_path[current_pos++] = graph[1][1];

	// If the first element is the last element, true
	if (possible_path[possible_path_pos] == SIZE){
		cout << "yes";
		return 0;
	}

	// While moving to a new square is possible
	do {

		// Scan 2d array
		FOR (x, 1, ROW, 1){
			if(possible_path[possible_path_pos]%x == 0){
				FOR(y, 1, COL, 1){
					//print(x, y, x * y);

					if (x * y == possible_path[possible_path_pos]){

						graph_pos = graph[x][y];

						if (x * y == SIZE){
							cout << "yes";
							return 0;
						}
						//print(x, y, SIZE);
						//print(graph[x][y], possible_path[possible_path_pos], possible_path_pos);
						if (visited[graph_pos] == false){
							possible_path[current_pos++] = graph[x][y];
							visited[graph_pos] = true;
						}
						//print(graph[x][y], possible_path[possible_path_pos], possible_path_pos);
						if( (y+1) > possible_path[possible_path_pos]/x){
              						break;
						}
					}
				}
			}
		}
		possible_path_pos++;
	} while (possible_path[possible_path_pos] != -1);
		cout << "no";
	return 0;
}
