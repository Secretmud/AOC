#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static void day1a(int arr[2000]);
static void day1b(int arr[2000]);

int main(int argc, char **argv) {
    FILE * file;
    int buffer[2000];
    int i = 0;
    if (argc >= 2) {
        file = fopen(argv[1], "r");
        while (!feof(file)) {
            fscanf(file, "%d", &buffer[i]);
            i++;
        }
        printf("----------DAY 1----------\n");
        day1a(buffer);
        day1b(buffer);
        printf("-------------------------\n");
    } else {
        printf("You need to supply filename...\n");
    }
    return 0;
}

static void day1a(int arr[2000]) {
    printf("Task A:\n\t");
    int counter = 0;
    for (int i = 0; i < 2000 - 1; i++) {
        if (arr[i+1] > arr[i]) counter++;
    }
    printf("%d\n", counter);
}

static void day1b(int arr[2000]) {
    printf("Task B:\n\t");
    int counter = 0;
    for (int i = 0; i < 2000 - 3; i++) {
        int first = arr[i] + arr[i+1] + arr[i+2];
        int second = arr[i+1] + arr[i+2] + arr[i+3];
        if (second > first) counter++;
    }
    printf("%d\n", counter);
}
