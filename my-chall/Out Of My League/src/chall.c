#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define SIZE 8

char nums[SIZE * 8];
FILE *stding;      // 🎯 pointer perantara (TARGET)
FILE *f = NULL;      // flag file

void init() {
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    stding = stdin;    // default tetap stdin
}

void menu() {
    puts("1. ada");
    puts("2. adalah");
    puts("3. printflag hehe");
    puts("4. Exit");
    printf("> ");
}

void store_data() {
    int idx;
    printf("Index: ");
    scanf("%d", &idx);
    getchar();

    printf("Data: ");
    // ❌ OOB WRITE
    // fgets(&nums[idx * 8], 8, input_fp);
    fread(&nums[idx * 8], 1, 8, stding);

}

void read_data() {
    int idx;
    printf("Index: ");
    scanf("%d", &idx);
    getchar();

    // ❌ OOB READ
    printf("Data: %s\n", &nums[idx * 8]);
}

void print_flag() {
    char buf[100];

    puts("mau flag ga");

    if (!f) {
        puts("No flag file.");
        return;
    }

    fgets(buf, sizeof(buf), stding);
    printf("input kamu: %s\n", buf);

    // hapus newline
    buf[strcspn(buf, "\n")] = 0;

    if (strcmp(buf, "mau") == 0) {
        puts("Flag: XMAS{ini_flag_palsu_ayo_cari_lagi_semangattt:))))))}");
    } else {
        puts("yah ga jadi");
    }
}


int main() {
    char buf[64];
    int choice;

    init();

    while (1) {
        puts("gatau lagi soalnya mau gimana tpi ini udah cukup kok buat belajar heheheheh");
        menu();
        fgets(buf, sizeof(buf), stdin);
        choice = atoi(buf);

        if (choice == 123455) {
            f = fopen("flag.txt", "r");
            puts("Invalid.");
            continue;
        }

        switch (choice) {
            case 1:
                store_data();
                break;
            case 2:
                read_data();
                break;
            case 3:
                print_flag();
                break;
            case 4:
                puts("Bye!");
                exit(0);
            default:
                puts("Invalid.");
        }
    }
}
