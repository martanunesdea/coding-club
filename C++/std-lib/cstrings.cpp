/* Using c strings */
#include <cstdio>
#include <cstring>

const size_t max_size = 128;
const char * str1 = "String one";
const char * str2 = "String two";

int main() {
    char sd1[max_size];

    int i = 0;
    char c = 0;
    char * cp = 0;

    // strncpy - copy a string (counts number of items)
    strncpy(sd1, str1, max_size);
    printf("sd1 is %s\n", sd1);

    // strncat -- concatenate string (counts n. of elements)
    strncat(sd1, " - ", max_size - strlen(sd1) - 1);
    strncat(sd1, str2, max_size - strlen(sd1) - 1);
    printf("sd1 is %s\n", sd1);

    //  strnlen -- length of string
    size_t str_length = strnlen(sd1, max_size);
    printf("length of sd1 is %zd\n", str_length);

    // strcmp - compare strings
    i = strcmp(sd1, "String");
    printf("sd1 %s String (%d) \n", (i == 0) ? "==" : "!=", i);

    // strchr - find char in string
    c = 'n';
    cp = strchr(sd1, c);
    printf("Did we find a '%c' in sd1? %s\n", c, cp ? "yes" : "no");
    if (cp)
        printf("This '%c' in sd1 is at position %ld \n", c, cp - sd1);
    
    // strstr - find a string in a string
    cp = strstr(sd1, "String");
    printf("Did we find '%s' in sd1? %s \n", "String", cp ? "yes" : "no");
    if (cp)
        printf("The first '%s' in sd1 is at position %ld \n", "String", cp - sd1);

    return 0;
}