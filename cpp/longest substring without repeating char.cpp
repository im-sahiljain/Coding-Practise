#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int longestSubstringLength(const string& s) {
    map<char, int> hash;
    int n = s.size();
    int l = 0, r = 0, maxlen = 0;

    while (r < n) {
        if (hash.find(s[r]) != hash.end()) {
            if (hash[s[r]] >= l) {
                l = hash[s[r]] + 1;
            }
        }
        int len = r - l + 1;
        maxlen = max(len, maxlen);
        hash[s[r]] = r;
        r++;
    }
    return maxlen;
}

int main() {
    string str = "afhdbasf";
    int length = longestSubstringLength(str);
    cout << "Length of the longest substring without repeating characters: " << length << endl;
    return 0;
}
