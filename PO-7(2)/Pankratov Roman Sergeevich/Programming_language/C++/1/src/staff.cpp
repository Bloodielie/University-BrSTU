#include <string>
#include <iostream>
#include "staff.h"


Staff::Staff(std::string name, int workshop_number, int discharge) : _name(name), _workshop_number(workshop_number), _discharge(discharge) {
    std::cout << "Created new staff" << std::endl;
}

Staff::Staff(): Staff("Ivan", 12, 5) {}

Staff::Staff(Staff &staff): Staff(staff._name, staff._workshop_number, staff._discharge) {}

Staff::~Staff() {
    std::cout << "Staff disposed" << std::endl;
}

void Staff::display() {
    std::cout << "Staff(name=" << _name << ", workshop_number=" << _workshop_number << ", discharge=" << _discharge << ")" << std::endl;
}

void Staff::set_name(std::string value) {
    _name = value;
}

std::string Staff::get_name() {
    return _name;
}

int Staff::get_discharge() {
    return _discharge;
}

void Staff::set_discharge(int value) {
    _discharge = value;
}

int Staff::get_workshop_number() {
    return _workshop_number;
}

void Staff::set_workshop_number(int value) {
    _workshop_number = value;
}
