// http://www.spoj.com/problems/AGGRCOW/
// g++ -std=c++14 Aggressive_Cows.cpp ; ./a.out < Aggressive_Cows.test

#include <bits/stdc++.h>
#include<iostream>
using namespace std;

bool can_all_cows_be_placed(int min_distance, int array[], int num_stalls, int aggressive_cow_count)
{
    // can all cows be placed with the present minimum distance
    int num_cows_placed = 1, last_placed_position = 0;
    int present_distance;
    for (int current_position = 1; current_position < num_stalls; current_position++)
    {
        present_distance = array[current_position] - array[last_placed_position];
        if (present_distance >= min_distance) {
            // place a cow in the position if present distance is greater than or equal to min distance possible
            last_placed_position = current_position;
            num_cows_placed++;
            if (num_cows_placed == aggressive_cow_count) {
                return true;
            }
        }
    }
    return false;
}

int get_largest_minimum_distance(int array[], int num_stalls, int aggressive_cow_count)
{
    /*
    Find the largest minimum distance with which we can place all cows.
    We try this with binary search.
    We Try with the middle of first and iteratively proceed towards the answer
    In successive iterations we attempt the mid values p
    */
    int start = 0, end = array[num_stalls - 1], largest_minimum_distance_so_far = -20;
    sort(array, array + num_stalls);  // sort the array because we need to do binary search on the input
    while (end > start)
    {
        int mid = (start + end) / 2;
        if (can_all_cows_be_placed(mid, array, num_stalls , aggressive_cow_count))
        {
            // I can place all cows with the distance of mid
            // I should try with a higher value in the next iteration
            if (mid > largest_minimum_distance_so_far)
                largest_minimum_distance_so_far = mid;
            start = mid + 1;
        }
        else {
            // I cannot place all the cows with the present mid value
            // I should try with a smaller value next time
            end = mid;
        }
        /* Loop invariant
        After each iteration we will have the largest minimum distance found so far.
        We search left or right depending on whether the given mid value gave us a success or failure in the 
        attempt we make to place all cows with the distance value as mid
        When we exit the loop we get the largest minimum distance
        */
    }
    return largest_minimum_distance_so_far;
}


int main() {
    int num_test_cases, num_stalls, aggressive_cow_count;
    cin >> num_test_cases;
    while (num_test_cases--)
    {
        cin >> num_stalls;
        cin >> aggressive_cow_count;
        int array[num_stalls];
        int value;
        for (int index=0; index < num_stalls; index++) {
            cin >> value;
            array[index] = value;
        }
        int largest_minimum_distance = get_largest_minimum_distance(array, num_stalls, aggressive_cow_count);
        cout << largest_minimum_distance << endl;
    }
    return 0;
}