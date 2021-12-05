# Refactor code before chk4
# Update for chk4
# Very first validate the input:
    # - Validate that it is a string
    # - Validate that it only contains appropriate letters (A,B,C,D,E,F...) 
# Gather the number of each letter present in the string provided
# For special cases like F, we need to find the number of recursively modify the number in F to keep applying the offer, every multiple of 2 removes 1 F from consideration.
# For special case like E, find the multiples first, then reduce the number of B according to it's offer detail.
# Then for special cases like A, B find the multiples (if any) this is of the special quantity, create a new category for this and store the value for the remainder
# For each letter (and new representation for offer values) multiply the value by the number of them in the products in the basket

# TODO: function that can parse the input from the challenge file would make remove effort here.
SKU_PRICE_MAP = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

SKU_OFFER_PRICE_MAP = {
    "A3_offer": 130,
    "A5_offer": 200,
    "B2_offer": 45,
    "E2_offer": 80,
    "F2_offer": 20,
    "H5_offer": 45,
    "H10_offer": 80,
    "K2_offer": 120,
    "N3_offer": 120,
    "P5_offer": 200,
    "Q3_offer": 80,
    "R3_offer": 150,
    "U3_offer": 120,
    "V2_offer": 90,
    "V3_offer": 130,
    "ZSTYX3_offer": 45,
}

SKU_OFFER_TYPES = {
    "self_modifying": [
        {
            "sku": "F",
            "offer_multiple": 2,
            "total_modifier": 1,
        },
        {
            "sku": "U",
            "offer_multiple": 3,
            "total_modifier": 1,
        },
    ],
    "secondary_sku_modifying": [
        {
            "sku": "E",
            "offer_multiple": 2,
            "secondary_sku": "B",
            "number_of_secondary_sku": 1
        },
        {
            "sku": "N",
            "offer_multiple": 3,
            "secondary_sku": "M",
            "number_of_secondary_sku": 1
        },
        {
            "sku": "R",
            "offer_multiple": 3,
            "secondary_sku": "Q",
            "number_of_secondary_sku": 1
        },
    ],
    "multiple": [
        {
            "sku": "A",
            "offer_multiple": 5,
        },
        {
            "sku": "A",
            "offer_multiple": 3,
        },
        {
            "sku": "B",
            "offer_multiple": 2,
        },
        {
            "sku": "H",
            "offer_multiple": 10,
        },
        {
            "sku": "H",
            "offer_multiple": 5,
        },
        {
            "sku": "K",
            "offer_multiple": 2,
        },
        {
            "sku": "P",
            "offer_multiple": 5,
        },
        {
            "sku": "Q",
            "offer_multiple": 3,
        },
        {
            "sku": "V",
            "offer_multiple": 3,
        },
        {
            "sku": "V",
            "offer_multiple": 2,
        },
    ],
    # sort according to value, highest to lowest, and then alphabetically.
    # TODO: if more challenge remained, consider a sorting function.
    "mix_and_match": {
        "skus": "ZSTYX",
        "offer_multiple": 3,
    }
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
    
    _update_for_self_modifying_sku_offers(count_of_skus)
    _update_for_secondary_sku_offers(count_of_skus)
    _update_for_multiple_offers(count_of_skus)
    _update_for_mix_and_match_offers(count_of_skus)

    total_cost_of_basket = _calculate_total(count_of_skus)

    return total_cost_of_basket
    
def _update_for_self_modifying_sku_offers(count_of_skus):
    """Calculate and update all self-modifying offers."""
    for sku_dictionary in SKU_OFFER_TYPES["self_modifying"]:
        number_of_sku = count_of_skus[sku_dictionary["sku"]]
        sku_dictionary.update({"number_of_sku": number_of_sku, "count_of_skus": count_of_skus})
        _calculate_self_modifying_offer(**sku_dictionary)

def _update_for_secondary_sku_offers(count_of_skus):
    """Calculate and update all secondary sku offers."""
    for sku_dictionary in SKU_OFFER_TYPES["secondary_sku_modifying"]:
        sku_dictionary.update({"count_of_skus": count_of_skus})
        _calculate_sku_offer_affecting_secondary_sku(**sku_dictionary)

def _update_for_multiple_offers(count_of_skus):
    """Calculate and update all multiple offers."""
    for sku_dictionary in SKU_OFFER_TYPES["multiple"]:
        sku_dictionary.update({"count_of_skus": count_of_skus})
        _calculate_sku_multiple_offers(**sku_dictionary)

def _update_for_mix_and_match_offers(count_of_skus):
    """Calculate and update all mix and match offers"""
    skus = SKU_OFFER_TYPES["mix_and_match"]["skus"]
    offer_multiple = SKU_OFFER_TYPES["mix_and_match"]["offer_multiple"]
    sub_sku = ""
    # create an ordered subsku for the skus in the offer
    for sku in skus:
        sub_sku = "".join([sub_sku, sku*count_of_skus[sku]])
        count_of_skus[sku] = 0
    shared, remainder =  divmod(len(sub_sku), offer_multiple)
    # create a sub_sku for remainder letters
    skus_to_keep = sub_sku[-remainder:]
    for sku in set(skus_to_keep):
        count_of_skus[sku] = skus_to_keep.count(sku)
    if shared:
        offer_label = _offer_label_composition(skus, offer_multiple)
        count_of_skus[offer_label] = shared
 
def _calculate_total(count_of_skus):
    """Helper function to calculate the total for all offers and SKUs"""
    total_cost_of_basket = 0
    all_sku_prices = {}
    all_sku_prices.update(SKU_PRICE_MAP)
    all_sku_prices.update(SKU_OFFER_PRICE_MAP)
    # Multiply each sku/offer count by its corresponding value
    for priced_item, price in all_sku_prices.items():
        total_cost_of_basket += count_of_skus.get(priced_item, 0)*price
    return total_cost_of_basket

def _offer_label_composition(sku, offer_multiple):
    """Helper function to create offer name strings."""
    sku_offer_label = "".join([sku, str(offer_multiple), "_offer"])
    return sku_offer_label

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
        count_of_skus[offer_label] = total_for_sku_offer
        return None

    remainder = number_of_sku - (offer_multiple + total_modifier)
    total_for_sku_offer += 1
    _calculate_self_modifying_offer(
        sku,
        offer_multiple,
        total_modifier,
        remainder,
        count_of_skus,
        total_for_sku_offer
    )




