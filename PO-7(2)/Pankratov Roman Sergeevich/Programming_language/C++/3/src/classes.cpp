#include "classes.h"
#include <iostream>


PreSchooler::PreSchooler(std::string name) :_name(name) {}

bool PreSchooler::operator==(PreSchooler &p) {
    return _name == p._name;
}

void PreSchooler::print() {
    std::cout << "PreSchooler: " << _name << std::endl;
}

bool PreSchooler::operator!=(PreSchooler &p) {
    return _name != p._name;
}

PreSchooler& PreSchooler::operator=(PreSchooler &p) {
    _name = p._name;
    return *this;
}

SchoolBoy::SchoolBoy(std::string name, int age): PreSchooler(name), _age(age) {}

void SchoolBoy::print() {
    std::cout << "SchoolBoy: " << _name << ", " << _age << std::endl;
}

Student::Student(std::string name, int age, int course): SchoolBoy(name, age), _course(course) {}

void Student::print() {
    std::cout << "Student: " << _name << ", " << _age << ", " << _course << std::endl;
}

Worker::Worker(std::string name, int age, int course, float salary): Student(name, age, course), _salary(salary) {}

void Worker::print() {
    std::cout << "Worker: " << _name << ", " << _age << ", " << _course << ", " << _salary << std::endl;
}

int PeopleArray::len() {
    return length;
}

void PeopleArray::append(PreSchooler *p) {
    auto** new_array = new PreSchooler*[length+1];
    for (int i = 0; i < length; i++) {
        new_array[i] = array[i];
    }
    new_array[length] = p;
    array=new_array;
    length += 1;
}

PreSchooler *PeopleArray::operator[](int index) {
    return array[index];
}
