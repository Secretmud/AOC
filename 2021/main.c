#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static void day1a(int *arr);
static void day1b(int *arr);
static void readFile(int *p, char *fname);

int main(int argc, char **argv) {
    int *buffer;
    buffer = (int*)malloc(2000 * sizeof(int));
    if (argc >= 2) {
        readFile(buffer, argv[1]);
        printf("----------DAY 1----------\n");
        day1a(buffer);
        day1b(buffer);
        printf("-------------------------\n");
    } else {
        printf("You need to supply filename...\n");
    }
    return 0;
}

static void readFile(int *p, char *fname) {
    FILE * file;
    int i = 0;
    file = fopen(fname, "r");
    while (!feof(file)) {
        fscanf(file, "%d", &p[i]);
        i++;
    }
    
}

static void day1a(int *arr) {
    printf("Task A:\n\t");
    int counter = 0;
    for (int i = 0; i < 2000 - 1; i++) {
        if (arr[i+1] > arr[i]) counter++;
    }
    printf("%d\n", counter);
}

static void day1b(int *arr) {
    printf("Task B:\n\t");
    int counter = 0;
    for (int i = 0; i < 2000 - 3; i++) {
        int first = arr[i] + arr[i+1] + arr[i+2];
        int second = arr[i+1] + arr[i+2] + arr[i+3];
        if (second > first) counter++;
    }
    printf("%d\n", counter);
}
