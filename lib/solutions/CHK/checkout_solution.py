# Refactor code before chk4
# Very first validate the input:
    # - Validate that it is a string
    # - Validate that it only contains appropriate letters (A,B,C,D,E,F...) 
# Gather the number of each letter present in the string provided
# For special cases like F, we need to find the number of recursively modify the number in F to keep applying the offer, every multiple of 2 removes 1 F from consideration.
# For special case like E, find the multiples first, then reduce the number of B according to it's offer detail.
# Then for special cases like A, B find the multiples (if any) this is of the special quantity, create a new category for this and store the value for the remainder
# For each letter (and new representation for offer values) multiply the value by the number of them in the products in the basket


SKU_PRICE_MAP = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
}

SKU_OFFER_PRICE_MAP = {
    "A3_offer": 130,
    "A5_offer": 200,
    "B2_offer": 45,
    "E2_offer": 80,
    "F2_offer": 20
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
        Function to calculate total value for skus provided.
    """
   
    if not isinstance(skus, str):
        return -1
    
    # Check length of string, then do count for each candidate letter to get subtotals and total
    # if total is different then an incorrect character is present
    total_count_of_skus = 0
    count_of_skus = {}
    length_of_input_string = len(skus)
    
    for sku in SKU_PRICE_MAP.keys():
        sku_count = skus.count(sku)
        total_count_of_skus += sku_count
        count_of_skus[sku] = sku_count
    if total_count_of_skus != length_of_input_string:
        return -1

    def _calculate_sku_multiple_offers(sku, offer_multiple, count_of_skus):
        """
        Helper function to calculate the number of offers for,
        and decrement the associated count of, a given sku
        """
        # first calculate the amount for an offer
        # find shared items and remainder
        shared, remainder =  divmod(count_of_skus[sku], offer_multiple)
        offer_label = _offer_label_composition(sku, offer_multiple)
        count_of_skus[offer_label] = shared
        count_of_skus[sku] = remainder
        
    def _calculate_sku_offer_affecting_secondary_sku(
            sku,
            offer_multiple,
            secondary_sku,
            number_of_secondary_sku,
            count_of_skus
        ):
        """
            Helper function for the offer case which modifies a secondary SKU.
            i.e. if a number of SKU E yields a free SKU B, reduce number of B when calculating
            number in offer SKU E.
        """
        _calculate_sku_multiple_offers(sku, offer_multiple, count_of_skus)
        offer_label = _offer_label_composition(sku, offer_multiple)
        secondary_sku_modifier = count_of_skus[offer_label]*number_of_secondary_sku
        # reduce secondary quantity, if less than 0 keep 0
        count_of_skus[secondary_sku] = max(count_of_skus[secondary_sku] - secondary_sku_modifier, 0)

    # def _calculate_E_offer(count_of_skus):
    #     """
    #     Helper function for the special E case multiple calculation.
    #     """
    #     _calculate_sku_offers("E", 2, count_of_skus)
    #     # reduce B quantity, if less than 0 keep 0
    #     count_of_skus["B"] = max(count_of_skus["B"]-count_of_skus["E2_offer"], 0)
    
    def _calculate_self_modifying_offer(
        sku,
        offer_multiple,
        total_modifier,
        number_of_sku,
        count_of_skus,
        total_for_sku_offer=0
    ):
        """
            Helper function for the special case of a self-modifying multiple calculation.
            i.e. if a number of SKU F yields a free SKU F, reduce number according to the offer.
        """
        offer_label = _offer_label_composition(sku, offer_multiple)
        if number_of_sku<=offer_multiple:
            count_of_skus[sku] = number_of_sku
            count_of_skus[sku_offer_label] = total_for_sku_offer
            return None
        remainder = number_of_sku - (offer_multiple + total_modifier)
        total_for_sku_offer += 1
        _calculate_self_modifying_offer(remainder, count_of_skus, total_for_sku_offer)
    
    def _calculate_F_offer(number_of_F, count_of_skus, total_for_F_offer=0):
        """
        Helper function for the special F case multiple calculation.
        """
        if number_of_F<=2:
            count_of_skus["F"] = number_of_F
            count_of_skus["F2_offer"] = total_for_F_offer
            return None
        remainder = number_of_F - 3
        total_for_F_offer += 1
        _calculate_F_offer(remainder, count_of_skus, total_for_F_offer)

    _calculate_F_offer(count_of_skus["F"], count_of_skus)

    # Calculate the offers for E
    _calculate_E_offer(count_of_skus)

    # Calculate the offers for A and B
    _calculate_sku_offers("A", 5, count_of_skus)
    _calculate_sku_offers("A", 3, count_of_skus)
    _calculate_sku_offers("B", 2, count_of_skus)
    
    # Calculate total    
    # Multiply each count by the skus corresponding value
    total_cost_of_basket = 0
    total_cost_of_basket += count_of_skus["A"]*50
    total_cost_of_basket += count_of_skus["B"]*30
    total_cost_of_basket += count_of_skus["C"]*20
    total_cost_of_basket += count_of_skus["D"]*15
    total_cost_of_basket += count_of_skus["E"]*40
    total_cost_of_basket += count_of_skus["F"]*10
    total_cost_of_basket += count_of_skus["A3_offer"]*130
    total_cost_of_basket += count_of_skus["B2_offer"]*45
    total_cost_of_basket += count_of_skus["E2_offer"]*80
    total_cost_of_basket += count_of_skus["A5_offer"]*200
    total_cost_of_basket += count_of_skus["F2_offer"]*20

    return total_cost_of_basket

def _offer_label_composition(sku, offer_multiple):
    """Helper function to create offer name strings."""
    sku_offer_label = "".join([sku, str(offer_multiple), "_offer"])
    return sku_offer_label




