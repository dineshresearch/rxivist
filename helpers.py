"""Utilities for interpreting data that arrives in impractical formats.

This module stores helper functions that transform data for the controllers.
"""

class NotFoundError(Exception):
  """
  Helper exception for when we should probably be returning 404s.

  """
  def __init__(self, id):
    """Sets the exception message.

    Arguments:
      - id: The requested ID of the entity that couldn't be found.

    """
    self.message = f"Entity could not be found with id {id}"

def find_new_id(old, connection):
  """If a request comes in for an author of an ID that indicates
  it's part of the old numbering scheme, this will check to see if
  we have an updated number to redirect to."""
  result = connection.read("SELECT new FROM author_translations WHERE old=%s", (old,))
  if len(result) == 0:
    return False
  if len(result[0]) == 0:
    return False
  return result[0][0]

def doi_to_id(doi, connection):
  """If a request comes in for an author of an ID that indicates
  it's part of the old numbering scheme, this will check to see if
  we have an updated number to redirect to."""
  print(f"LOOKIN FOR {doi}")
  result = connection.read("SELECT id FROM articles WHERE doi=%s", (doi,))
  if len(result) == 0:
    return False
  if len(result[0]) == 0:
    return False
  return result[0][0]

def num_to_month(monthnum):
  """Converts a (1-indexed) numerical representation of a month
  of the year into a three-character string for printing. If
  the number is not recognized, it returns an empty string.

  Arguments:
    - monthnum: The numerical representation of a month

  Returns:
    - The three-character abbreviation of the specified month

  """
  months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
  }
  if monthnum is None or monthnum < 1 or monthnum > 12:
    return ""
  return months[monthnum]
