""" Contains  classes that handle data validation """
# Standard imports
import re
from urllib.parse import urlparse


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

    @classmethod
    def validate_url(cls, url):
        """ Validates urls """

        is_valid_url = urlparse(url)
        url_scheme = is_valid_url.scheme

        if url_scheme in ('http', 'https'):
            return url

        raise TypeError
