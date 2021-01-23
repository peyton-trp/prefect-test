"""Module for all SQL queries
"""

# Description of what the query does
#   more description if necessary, tabbed over once
get_manual_override_rows = """
--sql
SELECT * from manual_override
WHERE yes_no = 'yes'
and text != 'No text - category selected manually';
"""

# Description of what the query does
#   more description if necessary, tabbed over once
get_manual_override_rows_labeled_no = """
--sql
SELECT * from manual_override
WHERE yes_no = 'no'
and text != 'No text - category selected manually';
"""
