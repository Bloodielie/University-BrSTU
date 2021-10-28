#include "string"

class PreSchooler {
protected:
    std::string _name;

public:
    PreSchooler(std::string name);

    bool operator== (PreSchooler &p);
    bool operator!= (PreSchooler &p);
    PreSchooler& operator= (PreSchooler &p);

    virtual void print();
};

class SchoolBoy: public PreSchooler {
protected:
    int _age;

public:
    SchoolBoy(std::string name, int age);

    void print() override;
};

class Student: public SchoolBoy {
protected:
    int _course;

public:
    Student(std::string name, int age, int course);

    void print() override;
};

class Worker: public Student {
protected:
    float _salary;

public:
    Worker(std::string name, int age, int course, float salary);

    void print() override;
};

class PeopleArray{
    int length = 0;
    PreSchooler** array = new PreSchooler*[length];

public:
    int len();
    void append(PreSchooler* p);

    PreSchooler* operator[](int index);
};
