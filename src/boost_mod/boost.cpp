#include <boost/python.hpp>

bool has_letter(const char * text, const char letter) {
    const char * ptr = text;
    char c;
    while (true) {
        c = *ptr;
        if (c == letter) {
            return true;
        }
        if (c == '\0') {
            break;
        }
        ptr++;
    }
    return false;
}

BOOST_PYTHON_MODULE(boost)
{
    boost::python::def("has_letter", has_letter);
}
