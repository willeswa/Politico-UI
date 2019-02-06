# """ Contains  classes that handle data validation """
# # Standard imports
# import re
# import json
# from urllib.parse import urlparse


# def is_valid_word(word_entity):
#     """ validates strings """

#     pattern = r'[a-zA-Z]'
#     match = re.match(pattern, word_entity)

#     entry_type = isinstance(word_entity, str)

#     if word_entity and entry_type and match:
#         return True
#     return 'Not a valid {}'.format(word_entity)


# def validate_url(url):
#     """ Validates urls """

#     is_valid_url = urlparse(url)
#     url_scheme = is_valid_url.scheme

#     if url_scheme in ('http', 'https'):
#         return url
#     return 'Invalid url'


# def is_empty(json_dict, key):
#     """ Checks for an empty field """

#     _dict = json.dumps(json_dict)

#     if key in _dict.keys():
#         return True

#     return 'You must provide {}'.format(key)
