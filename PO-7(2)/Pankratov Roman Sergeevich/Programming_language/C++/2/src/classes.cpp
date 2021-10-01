#include "classes.h"
#include "iostream"

void Worker::add() {
    objects.push_back(this);
}

void Worker::print() {
    for (Worker* object : objects)
        object->show();
}

Worker::Worker(std::string name, std::string surname, int age): _name(name), _surname(surname), _age(age) {
    add();
    std::cout << "Create Worker" << std::endl;
}

Worker::~Worker() {
    std::cout << "Delete Worker" << std::endl;
}

Cadrs::Cadrs(std::string name, std::string surname, int age): Worker(name, surname, age) {
    std::cout << "Create Cards" << std::endl;
}

Cadrs::~Cadrs() {
    std::cout << "Delete Cadrs" << std::endl;
}

void Cadrs::show() {
    std::cout << "Cadrs: " << "name=" << _name << ", surname=" << _surname << ", age=" << _age << std::endl;
}

Engineer::Engineer(std::string name, std::string surname, int age): Cadrs(name, surname, age) {
    std::cout << "Create Engineer" << std::endl;
}

Engineer::~Engineer() {
    std::cout << "Delete Engineer" << std::endl;
}

void Engineer::show() {
    std::cout << "Engineer: " << "name=" << _name << ", surname=" << _surname << ", age=" << _age << std::endl;
}

Administration::Administration(std::string name, std::string surname, int age): Engineer(name, surname, age) {
    std::cout << "Create Administration" << std::endl;
}

Administration::~Administration() {
    std::cout << "Delete Administration" << std::endl;
}

void Administration::show() {
    std::cout << "Administration: " << "name=" << _name << ", surname=" << _surname << ", age=" << _age << std::endl;
}
