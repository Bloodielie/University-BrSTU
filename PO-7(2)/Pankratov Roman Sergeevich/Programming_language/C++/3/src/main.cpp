#include <iostream>
#include "classes.h"

int main() {
    auto pre_schooler = new PreSchooler("Roman");
    auto school_boy = new SchoolBoy("Igor", 15);
    auto student = new Student("Vanya", 19, 2);
    auto worker = new Worker("Dima", 22, 4, 1500.0);

    auto array = new PeopleArray();
    array->append(pre_schooler);
    array->append(school_boy);
    array->append(student);
    array->append(worker);

    for (int i = 0; i < array->len(); i++) {
        (*array)[i]->print();
    }

    *school_boy = *student;
    std::cout << std::endl;

    for (int i = 0; i < array->len(); i++) {
        (*array)[i]->print();
    }

    std::cout << std::endl;

    bool res2 = *pre_schooler == *school_boy;
    bool res3 = *pre_schooler != *worker;

    std::cout << res2 << std::endl;
    std::cout << res3 << std::endl;

    delete pre_schooler;
    delete school_boy;
    delete student;
    delete worker;

    return 0;
}
