#include <iostream>
using namespace std;

int main() {
    int id;
    double price;
    
    while (cin >> id) {  // Loop continues as long as there is valid input
        if (id <= 0) {
            cout << "The value you entered is invalid. The value must be greater than 0. Application will terminate." << endl;
            exit(0);
        }
        
        cin >> price;  // Get the price for this ID
        
        if (price <= 0) {
            cout << "The value you entered is invalid. The value must be greater than 0. Application will terminate." << endl;
            exit(0);
        }
        
        cout << "The inventory item with id=" << id << ", costs $" << price << "." << endl;
    }
    
    return 0;
}