// Use qsort() in a C++ program to sort array of dates where date is stored in a structure.

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cstdio>

using namespace std;

struct Date {
    int day;
    int month;
    int year;
};

int compare(const void *a, const void *b) {
    Date *x = (Date *) a;
    Date *y = (Date *) b;
    if (x->year != y->year) {
        return x->year - y->year;
    } else if (x->month != y->month) {
        return x->month - y->month;
    } else {
        return x->day - y->day;
    }
}

// Bsearch() to find some of the sorted dates
int bsearch(Date *arr, int n, Date key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid].year == key.year && arr[mid].month == key.month && arr[mid].day == key.day) {
            return mid;
        } else if (compare(&arr[mid], &key) < 0) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}


// Your own version of Bsearch() to find some of the sorted dates
int myBsearch(Date *arr, int n, Date key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid].year == key.year && arr[mid].month == key.month && arr[mid].day == key.day) {
            return mid;
        } else if (arr[mid].year < key.year || (arr[mid].year == key.year && arr[mid].month < key.month) ||
                   (arr[mid].year == key.year && arr[mid].month == key.month && arr[mid].day < key.day)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}


int main() {
    int n;
    cout << "Enter the number of dates: ";
    cin >> n;
    Date *arr = new Date[n];
    srand(time(NULL));
    for (int i = 0; i < n; i++) {
        arr[i].day = rand() % 30 + 1;
        arr[i].month = rand() % 12 + 1;
        arr[i].year = rand() % 100 + 1900;
    }
    cout << "Unsorted dates: " << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i].day << "/" << arr[i].month << "/" << arr[i].year << endl;
    }
    qsort(arr, n, sizeof(Date), compare);
    cout << "Sorted dates: " << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i].day << "/" << arr[i].month << "/" << arr[i].year << endl;
    }
    Date key;
    cout << "Enter the date to search: ";
    cin >> key.day >> key.month >> key.year;
    int index = bsearch(arr, n, key);
    if (index == -1) {
        cout << "Date not found" << endl;
    } else {
        cout << "Date found at index " << index << endl;
    }
    index = myBsearch(arr, n, key);
    if (index == -1) {
        cout << "Date not found" << endl;
    } else {
        cout << "Date found at index " << index << endl;
    }
    return 0;
}

