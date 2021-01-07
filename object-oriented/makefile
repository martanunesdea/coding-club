CC = clang++
CFLAGS = -Wall -std=c++11
main: main.o
	$(CC) $(CFLAGS) -o main main.o
main.o: main.cpp product.h disc.h
	$(CC) $(CFLAGS) -c main.cpp

clean:
	rm -f *.o *.h.gch main