#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
using namespace std;
 
void run_within_for_each(std::function<void (int)> func)
{
    vector<int> numbers{ 1, 2, 3, 4, 5, 10, 15, 20, 25, 35, 45, 50 };
 
    for_each(numbers.begin(), numbers.end(), func);
}
 
int main()
{
    auto func1 = [](int y)
    {
        cout << y << endl;
    };
 
    auto func2 = [](int z)
    {
        cout << z * 2 << endl;
    };
 
    run_within_for_each(func1);
    run_within_for_each(func2);
}
