

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    # Very first validate the input:
        # - Validate that it is a string
        # - Validate that it only contains appropriate letters (A,B,C,D)
        
    if not isinstance(skus, str):
        return -1
    
    # Check length of string, then do count for each candidate letter, if sum total is different then an incorrect character is present
    total_count_of_skus = 0
    count_of_skus = {}
    length_of_input_string = len(skus)
    
    for sku in ("ABCD"):
        sku_count = skus.count(sku)
        total_count_of_skus += sku_count
        count_of_skus[sku] = sku_count
    if total_count_of_skus != length_of_input_string:
        return -1
    
    # Calculate the offers for A and B
    count_of_skus["A"].
    
    # First gather the number of each letter present in the string provided
    # Then for special cases A and B, find the multiples (if any) this is of the special quantity, create a new category for this and store the value for the remainder
    # For each letter (and new representation for offer values) multiply the value by the number of them in the products in the basket
    raise NotImplementedError()



