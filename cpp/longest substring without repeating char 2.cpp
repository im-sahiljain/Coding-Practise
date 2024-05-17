#include<iostream>
#include<unordered_map>
using namespace std;

int main() {
    string s = "audhfoaeng";
    int maxlen = 0;
    int n = s.length();
    int l = 0, r = 0, len = 0;

    unordered_map<char, int> mpp;

    while (r < n) {
        if (mpp.find(s[r]) != mpp.end()) {
            if (mpp[s[r]] >= l) {
                l = mpp[s[r]] + 1;
            }
        }
        len = r - l + 1;
        maxlen = max(len, maxlen);
        mpp[s[r]] = r;
        r++;
    }
        for (auto it = mpp.begin(); it != mpp.end(); it++) {
        cout << it->first << ": " << it->second << endl;
    }
    cout << maxlen << endl;

    return 0;
}
