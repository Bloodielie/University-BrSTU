#include <string>

class Staff {
    std::string _name;
    int _workshop_number;
    int _discharge;

public:
    Staff();
    Staff(std::string name, int workshop_number, int discharge);
    Staff(Staff& staff);
    ~Staff();

    void display();

    void set_name(std::string value);
    std::string get_name();
    void set_workshop_number(int value);
    int get_workshop_number();
    void set_discharge(int value);
    int get_discharge();
};
