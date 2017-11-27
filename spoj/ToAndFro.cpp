// http://www.spoj.com/problems/TOANDFRO/

#include <iostream>
#include <cstring>
using namespace std;

int to_and_fro(int num_columns, char str[201]) {
    int length = strlen(str);
    int num_rows = length / num_columns;
    for(int i=0; i < num_columns; i++) {
        for(int j=0; j < num_rows; j++) {
            if (j % 2 == 0)
                cout << str[j * num_columns + i];
            else
                cout << str[(j + 1) * num_columns - (i + 1) ];
        }
    }
    cout << endl;
}

int main() {
        // your code goes here
    int num_columns;
    char str[201];
    while (1) {
        cin >> num_columns;
        
        if (num_columns == 0) {
            break;
        }else {
            cin >> str;
            // cout << num_columns << endl;
            // cout << str << endl;
            to_and_fro(num_columns, str);
        }

    }
    return 0;
}