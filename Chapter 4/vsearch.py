def search4vowels(word):
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
    
