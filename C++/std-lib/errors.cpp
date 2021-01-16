/* Using returned errors */

#include <cstdio>
#include <cerrno>
#include <cstring> // to use errstr

int main() {
    printf("Erasing file foor.bar \n");
    remove("foo.bar");
    printf("Error is %d\n", errno);
    perror("Cannot erase file");

    // Using errstr from cstring header
    const char * errstr = strerror(errno);
    printf("error (%d): %s\n", errno, errstr);

    return 0;
}