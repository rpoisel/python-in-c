BIN := main

SRC := $(wildcard *.c)
OBJ := $(patsubst %.c,%.o,$(SRC))

CC := gcc
CFLAGS := -g -O0 $(filter-out -g -O3,$(shell python3-config --cflags))
LDFLAGS := $(shell python3-config --ldflags)

all: $(BIN)

$(BIN): $(OBJ)

.PHONY: clean
clean:
	-rm $(OBJ) $(BIN)
