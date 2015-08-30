#include <boost/python.hpp>
#include <sstream>
#include <string>

using namespace boost::python;

bool has_letter(const char * text, const char letter) {
    const char * ptr = text;
    while (char c = *(ptr++)) {
        if (c == letter) {
            return true;
        }
    }
    return false;
}

struct Native
{
    std::string name;
    long number;
    std::string pointer;

    Native(std::string name, long number, bool yes): name(name), number(number) {
        this->pointer = std::string(yes ? "YES" : "NO");
    }

    std::string summary() {
        std::stringstream ss;
        ss << "Native " << this->name << " number " << this->number << " pointer " << pointer;
        return ss.str();
    }
};

BOOST_PYTHON_MODULE(boost)
{
    def("has_letter", has_letter);

    class_<Native>("Native", init<std::string, long, bool>())
        .def_readwrite("name", &Native::name)
        .def_readwrite("number", &Native::number)
        .def_readonly("pointer", &Native::pointer)
        .def("summary", &Native::summary)
    ;

}
