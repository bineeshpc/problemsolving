#include<iostream>
using namespace std;

// https://practice.geeksforgeeks.org/problems/who-will-win/0

int binary_search(int begin, int end, int target, int count) {
    int mid;
    mid = (begin + end) / 2;
    //cout << begin << " "  << mid << " " << end << " " << target << " " << count << endl;
    // target - 1 is used everywhere because we are 0 indexed. actual target is target - 1
    if (mid == target - 1) {
        return count;
    }else if (target - 1 < mid) {
        // search on LHS
        return binary_search(begin, mid - 1, target, count + 1);
    } else if (target - 1 > mid) {
        // search on RHS
        return binary_search(mid+1, end, target, count + 1);
    }
}

void who_will_win(int array_size, int actual_position, int lookuptime_linear, int lookuptime_binary) {

    int binary_count=0, binary_time, linear_time;
    binary_count = binary_search(0, array_size - 1, actual_position, 0);
    binary_time = binary_count * lookuptime_binary;
    linear_time = actual_position * lookuptime_linear;
    //cout << actual_position << " " << linear_time << " " << binary_count << " " << binary_time << endl;
    if(linear_time < binary_time) {
        cout << 1 << endl;
    } else if (linear_time > binary_time) {
        cout << 2 << endl;
    } else {
        cout << 0 << endl;
    }
}

int main() {
	//code
	int num_cases;
	int array_size, actual_position, lookuptime_linear, lookuptime_binary;
	cin >> num_cases;
	for(int i=0; i<num_cases; i++) {
	    cin >> array_size;
	    cin >> actual_position;
	    cin >> lookuptime_linear;
	    cin >> lookuptime_binary;
	    who_will_win(array_size, actual_position, lookuptime_linear, lookuptime_binary);
	}
	
	return 0;
}
