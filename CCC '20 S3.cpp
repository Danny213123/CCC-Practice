#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	string needle, haystack, current, sorted, next;
	int score = 0;
	vector<string> total;
  cin >> needle >> haystack;
	string fi = needle;

	for (int x = 0; x < haystack.size() - needle.size() + 1; x++){
		bool impossible = false;
		current = haystack.substr(x, x + needle.size() - (1 * x));
		next = current;
		sort(current.begin(), current.end());
		sort(fi.begin(), fi.end());
		if (current == fi){
			for (int y = 0; y < total.size(); y++){
				if (total[y] == next){
					impossible = true;
				}
			}
			if (impossible != true){
				score++;
				total.push_back(next);
			}
		}
	}
	cout << score;
}
