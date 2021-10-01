#include "string"
#include "list"

class Worker {
private:
    static std::list <Worker*> objects;

protected:
    std::string _name;
    std::string _surname;
    int _age;

public:
    Worker(std::string name, std::string surname, int age);
    virtual ~Worker();

    void add();
    static void print();

    virtual void show() = 0;
};

class Cadrs: public Worker {
public:
    Cadrs(std::string name, std::string surname, int age);
    ~Cadrs() override;

    void show() override;
};

class Engineer: public Cadrs {
public:
    Engineer(std::string name, std::string surname, int age);
    ~Engineer() override;

    void show() override;
};

class Administration: Engineer {
public:
    Administration(std::string name, std::string surname, int age);
    ~Administration() override;

    void show() override;
};
