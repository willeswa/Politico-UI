""" Contains  classes that handle data validation """
# Third party imports
import re


class Validators:
    """ Handles validation """

    @classmethod
    def validate_word(cls, string_entry):
        """ validates strings """

        pattern = r'[a-zA-Z]'
        match = re.match(pattern, string_entry)

        entry_type = isinstance(string_entry, str)

        if string_entry and entry_type and match:
            return string_entry

        raise TypeError
