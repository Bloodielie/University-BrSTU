#include <iostream>
#include "staff.h"

int main() {
    auto* staff = new Staff();
    staff->display();
    staff->set_name("Ilya");
    staff->display();

    auto* staff2 = new Staff("Igor", 14, 3);
    staff2->display();

    auto* staff3 = new Staff(*staff);
    staff3->display();

    void (Staff::*pointer)();
    pointer = &Staff::display;

    delete staff;
    delete staff2;
    delete staff3;

    return 0;
}
