// http://www.spoj.com/problems/CANDY/

#include <iostream>
using namespace std;

int main() {
	// your code goes here
    int num_candies;

    while (1) {
        cin >> num_candies;
        
        if (num_candies == -1) {
            break;
        }else {
            int all_candies[num_candies];
            int count = 0;
            int candy_size;
            int total_candies = 0;
            while (count < num_candies) {
                cin >>  candy_size;
                all_candies[count] = candy_size;
                total_candies += candy_size;
                count ++;
            }
            int average = total_candies / num_candies;
            if(int(average * num_candies) != total_candies) {
                cout << -1 << endl;
            }
            else {
                int num_moves = 0;
                for(int i = 0; i < num_candies; i++) {
                    if (all_candies[i] > average) {
                        num_moves += all_candies[i] - average;
                    }
                }
                cout << num_moves << endl;
            }
        }

    }
	return 0;
}