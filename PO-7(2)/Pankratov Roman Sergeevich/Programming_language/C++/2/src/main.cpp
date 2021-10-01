#include <iostream>
#include "classes.h"

std::list <Worker*> Worker::objects{};

int main() {
    auto t1 = new Cadrs("test1", "no1", 1);
    auto t2 = new Engineer("test2", "no2", 2);
    auto t3 = new Administration("test3", "no3", 3);

    Worker::print();

    delete t1;
    delete t2;
    delete t3;

    return 0;
}
