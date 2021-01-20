#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

string is_perm (map<char, int> needle, map<char, int> haystack){
	for (int x = 0; x < 26; x ++){
		char letter = 'a' + x;
		if (needle[letter] != haystack[letter]){
			return "false";
		}
	}
	return "true";
}

int main() {
  string needle, haystack, cur_word, sorted_word;
	int correct;
	cin >> needle >> haystack;

	map<char, int> char_needle, char_haystack, empty_stack;
	map<string, bool> used;

	for (int x = 0; x < needle.size(); x++){
		char_needle[needle[x]]++;
	}
	
	for (int i = 0; i <= haystack.size() - needle.size(); i++){
		char_haystack = empty_stack;
		cur_word = haystack.substr(i, needle.size());
		for (int j = 0; j <= cur_word.size(); j++){
			char_haystack[cur_word[j]]++;
		}
		if (!used[cur_word] && is_perm(char_needle, char_haystack) != "false"){
			correct ++;
			used[cur_word] = true;
		}
	}
	cout << correct;
}
